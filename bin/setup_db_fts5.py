import os
import sqlite3

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
DB_PATH = os.path.join(PROJECT_ROOT, 'mcp', 'codebase-memory-mcp', 'data', 'codebase_memory.sqlite')

def setup_db():
    print(f"Conectando a SQLite en: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Tabla normal de historial de sesiones
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS session_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            ecosystem TEXT,
            role TEXT,
            message TEXT
        )
    ''')
    
    # 2. Tabla FTS5 virtual para búsqueda súper rápida de texto
    cursor.execute('''
        CREATE VIRTUAL TABLE IF NOT EXISTS session_history_fts 
        USING fts5(message, content='session_history', content_rowid='id');
    ''')
    
    # Triggers para mantener la tabla FTS5 sincronizada con la tabla normal
    cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS session_history_ai AFTER INSERT ON session_history BEGIN
            INSERT INTO session_history_fts(rowid, message) VALUES (new.id, new.message);
        END;
    ''')
    
    # 3. Tabla para el Cron Registry
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cron_registry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT UNIQUE,
            ecosystem TEXT,
            schedule_interval_sec INTEGER,
            last_run DATETIME,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    
    conn.commit()
    conn.close()
    print("[EXITO] Tablas de historial FTS5 y Cron creadas exitosamente.")

if __name__ == "__main__":
    setup_db()
