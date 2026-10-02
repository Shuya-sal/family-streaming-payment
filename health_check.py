#!/usr/bin/env python3
"""
Health Check Script for Family Streaming Payment System
Check if server is running and database is accessible
"""

import sqlite3
from datetime import datetime, timedelta
import os

DATABASE = 'family_payments.db'

def check_database():
    """Check if database is accessible"""
    
    if not os.path.exists(DATABASE):
        return {
            'status': 'error',
            'message': 'Database file not found'
        }
    
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Get table info
        cursor.execute("SELECT COUNT(*) FROM family_members")
        members_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM payments")
        payments_count = cursor.fetchone()[0]
        
        # Get recent activity (last 24 hours)
        yesterday = (datetime.now() - timedelta(days=1)).isoformat()
        cursor.execute('''
            SELECT COUNT(*) FROM payments 
            WHERE payment_date >= ?
        ''', (yesterday,))
        recent_payments = cursor.fetchone()[0]
        
        # Get expired subscriptions
        today = datetime.now().date().isoformat()
        cursor.execute('''
            SELECT COUNT(*) FROM payments 
            WHERE date(end_date) < ? AND status = 'active'
        ''', (today,))
        expired_subs = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'status': 'ok',
            'members_count': members_count,
            'total_payments': payments_count,
            'recent_24h': recent_payments,
            'expired_subscriptions': expired_subs
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

if __name__ == '__main__':
    print("=" * 50)
    print("🔍 Health Check Report")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    result = check_database()
    
    if result['status'] == 'ok':
        print(f"\n✅ Database Status: HEALTHY")
        print(f"👥 Total Members: {result['members_count']}")
        print(f"💳 Total Payments: {result['total_payments']}")
        print(f"📊 Recent (24h): {result['recent_24h']}")
        
        if result['expired_subscriptions'] > 0:
            print(f"⚠️  Expired Subs: {result['expired_subscriptions']} (needs attention)")
        else:
            print(f"✅ No expired subscriptions")
            
    else:
        print(f"\n❌ Database Status: ERROR")
        print(f"Error: {result['message']}")
    
    print("\n" + "=" * 50)
