import sqlite3
import os
from datetime import datetime
from pathlib import Path

class Database:
    def __init__(self, db_path='app/uploads/detection.db'):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.init_db()
    
    def init_db(self):
        """Create tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Uploads table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS uploads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                upload_id TEXT UNIQUE,
                upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_images INTEGER,
                good_count INTEGER DEFAULT 0,
                bad_count INTEGER DEFAULT 0,
                accuracy_rate REAL DEFAULT 0.0
            )
        ''')
        
        # Detection results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS detections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                upload_id TEXT,
                filename TEXT,
                confidence REAL,
                is_good INTEGER,
                detection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (upload_id) REFERENCES uploads(upload_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_upload(self, upload_id, total_images):
        """Create a new upload record"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO uploads (upload_id, total_images)
                VALUES (?, ?)
            ''', (upload_id, total_images))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating upload: {e}")
            return False
    
    def add_detection(self, upload_id, filename, confidence, is_good):
        """Add a detection result"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO detections (upload_id, filename, confidence, is_good)
                VALUES (?, ?, ?, ?)
            ''', (upload_id, filename, confidence, is_good))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error adding detection: {e}")
            return False
    
    def update_upload_stats(self, upload_id, good_count, bad_count):
        """Update upload statistics"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            total = good_count + bad_count
            accuracy_rate = (good_count / total * 100) if total > 0 else 0
            
            cursor.execute('''
                UPDATE uploads 
                SET good_count = ?, bad_count = ?, accuracy_rate = ?
                WHERE upload_id = ?
            ''', (good_count, bad_count, accuracy_rate, upload_id))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error updating stats: {e}")
            return False
    
    def get_upload_history(self):
        """Get all upload history"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM uploads ORDER BY upload_date DESC
            ''')
            
            uploads = [dict(row) for row in cursor.fetchall()]
            conn.close()
            return uploads
        except Exception as e:
            print(f"Error getting history: {e}")
            return []
    
    def get_upload_details(self, upload_id):
        """Get details of a specific upload"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM detections WHERE upload_id = ? ORDER BY detection_date
            ''', (upload_id,))
            
            detections = [dict(row) for row in cursor.fetchall()]
            conn.close()
            return detections
        except Exception as e:
            print(f"Error getting details: {e}")
            return []
    
    def get_statistics(self):
        """Get overall statistics"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM uploads')
            total_uploads = cursor.fetchone()
            
            cursor.execute('SELECT SUM(good_count) FROM uploads')
            total_good = cursor.fetchone() or 0
            
            cursor.execute('SELECT SUM(bad_count) FROM uploads')
            total_bad = cursor.fetchone() or 0
            
            cursor.execute('SELECT AVG(accuracy_rate) FROM uploads WHERE accuracy_rate > 0')
            avg_accuracy = cursor.fetchone() or 0
            
            conn.close()
            
            return {
                'total_uploads': total_uploads,
                'total_good': total_good,
                'total_bad': total_bad,
                'average_accuracy': round(avg_accuracy, 2)
            }
        except Exception as e:
            print(f"Error getting statistics: {e}")
            return {}
