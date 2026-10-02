from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import sqlite3
import os
from datetime import datetime, timedelta
import schedule
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
DATABASE = 'family_payments.db'

# Initialize database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Table for family members
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS family_members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Table for payments
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            platform TEXT NOT NULL,
            duration_months INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            status TEXT DEFAULT 'active',
            reference_code TEXT,
            FOREIGN KEY (member_id) REFERENCES family_members(id)
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_member', methods=['GET', 'POST'])
def register_member():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone', '')
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                'INSERT INTO family_members (name, email, phone) VALUES (?, ?, ?)',
                (name, email, phone)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('dashboard'))
        except sqlite3.IntegrityError:
            conn.close()
            return render_template('error.html', message='Email sudah terdaftar!')
    
    return render_template('register_member.html')

@app.route('/payment/<int:member_id>', methods=['GET', 'POST'])
def make_payment(member_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Get member info
    cursor.execute('SELECT * FROM family_members WHERE id = ?', (member_id,))
    member = cursor.fetchone()
    
    if not member:
        conn.close()
        return "Member not found", 404
    
    platforms = ['Netflix', 'YouTube Premium']
    durations = [1, 2, 3, 6, 12]
    
    if request.method == 'POST':
        platform = request.form['platform']
        duration = int(request.form['duration'])
        price_per_month = {'Netflix': 75000, 'YouTube Premium': 85000}
        
        total_amount = price_per_month[platform] * duration
        
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=duration*30)
        
        reference_code = f"PAY{datetime.now().strftime('%Y%m%d%H%M%S')}{member_id}"
        
        cursor.execute('''
            INSERT INTO payments (member_id, platform, duration_months, amount, 
                                 start_date, end_date, reference_code)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (member_id, platform, duration, total_amount, 
              start_date.isoformat(), end_date.isoformat(), reference_code))
        
        conn.commit()
        conn.close()
        
        return render_template('payment_success.html', 
                              reference_code=reference_code,
                              amount=total_amount,
                              duration=duration,
                              platform=platform,
                              member_name=member[1])
    
    conn.close()
    return render_template('make_payment.html', 
                          member=member,
                          platforms=platforms,
                          durations=durations)

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Get all members with their latest payment
    cursor.execute('''
        SELECT m.*, 
               p.platform, p.duration_months, p.amount, p.end_date, p.status
        FROM family_members m
        LEFT JOIN (
            SELECT * FROM payments 
            WHERE id IN (
                SELECT MAX(id) FROM payments 
                GROUP BY member_id
            )
        ) p ON m.id = p.member_id
        ORDER BY m.name
    ''')
    
    members = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', members=members)

@app.route('/api/members', methods=['GET'])
def get_members():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, phone FROM family_members')
    members = cursor.fetchall()
    conn.close()
    
    data = []
    for member in members:
        data.append({
            'id': member[0],
            'name': member[1],
            'email': member[2],
            'phone': member[3]
        })
    
    return jsonify(data)

@app.route('/api/payment_status/<int:member_id>', methods=['GET'])
def get_payment_status(member_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.*, m.name
        FROM payments p
        JOIN family_members m ON p.member_id = m.id
        WHERE p.member_id = ?
        ORDER BY p.payment_date DESC
    ''', (member_id,))
    
    payments = cursor.fetchall()
    conn.close()
    
    data = []
    for payment in payments:
        data.append({
            'id': payment[0],
            'platform': payment[2],
            'duration': payment[3],
            'amount': payment[4],
            'start_date': payment[6],
            'end_date': payment[7],
            'status': payment[8],
            'reference_code': payment[9],
            'member_name': payment[10]
        })
    
    return jsonify(data)

@app.route('/api/summary', methods=['GET'])
def get_summary():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Total members
    cursor.execute('SELECT COUNT(*) FROM family_members')
    total_members = cursor.fetchone()[0]
    
    # Total payments this month
    current_month = datetime.now().strftime('%Y-%m')
    cursor.execute('''
        SELECT COUNT(*), SUM(amount) FROM payments 
        WHERE strftime('%Y-%m', payment_date) = ?
    ''', (current_month,))
    payment_count, total_amount = cursor.fetchone()
    
    # Active subscriptions
    today = datetime.now().date().isoformat()
    cursor.execute('''
        SELECT COUNT(*), SUM(amount) FROM payments 
        WHERE date(end_date) >= ? AND status = 'active'
    ''', (today,))
    active_subs, subs_value = cursor.fetchone()
    
    conn.close()
    
    return jsonify({
        'total_members': total_members,
        'payments_this_month': payment_count or 0,
        'total_revenue_this_month': total_amount or 0,
        'active_subscriptions': active_subs or 0,
        'subscription_value': subs_value or 0
    })

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
