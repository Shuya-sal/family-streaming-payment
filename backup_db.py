#!/usr/bin/env python3
"""
Backup Script for Family Streaming Payment Database
Runs automatically to backup database daily
"""

import sqlite3
import os
from datetime import datetime
import shutil

DATABASE = 'family_payments.db'
BACKUP_DIR = 'backups'

def create_backup():
    """Create a backup of the database"""
    
    # Create backup directory if it doesn't exist
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    # Generate backup filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f'database_backup_{timestamp}.db'
    backup_path = os.path.join(BACKUP_DIR, backup_filename)
    
    try:
        # Copy database to backup location
        shutil.copy2(DATABASE, backup_path)
        
        print(f"✅ Backup created successfully: {backup_filename}")
        
        # List old backups (keep last 7 days)
        cleanup_old_backups()
        
        return True
        
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return False

def cleanup_old_backups(days_to_keep=7):
    """Remove backups older than specified days"""
    
    if not os.path.exists(BACKUP_DIR):
        return
    
    cutoff_time = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
    
    for filename in os.listdir(BACKUP_DIR):
        if filename.startswith('database_backup_'):
            filepath = os.path.join(BACKUP_DIR, filename)
            file_time = os.path.getmtime(filepath)
            
            if file_time < cutoff_time:
                try:
                    os.remove(filepath)
                    print(f"🗑️  Removed old backup: {filename}")
                except Exception as e:
                    print(f"⚠️  Could not remove {filename}: {e}")

if __name__ == '__main__':
    print("Starting database backup...")
    success = create_backup()
    
    if success:
        print("✅ Backup process completed successfully!")
    else:
        print("❌ Backup process failed!")
