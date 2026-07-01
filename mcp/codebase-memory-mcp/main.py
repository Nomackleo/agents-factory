from mcp.server.fastmcp import FastMCP
import sqlite3
import os
import json

mcp = FastMCP("codebase-memory-mcp")

# Configurar SQLite
db_dir = os.path.join(os.getcwd(), 'data')
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, 'codebase_memory.sqlite')

def init_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS codebase_index (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT UNIQUE,
            description TEXT,
            ecosystem TEXT,
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS file_relations (
            source_file TEXT,
            target_file TEXT,
            relation_type TEXT,
            PRIMARY KEY (source_file, target_file, relation_type)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@mcp.tool()
def query_architecture_db(sql: str) -> str:
    """
    Permite a los agentes consultar el índice relacional de la arquitectura usando SQL para máxima precisión.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = [dict(row) for row in rows]
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error SQL: {e}"
    finally:
        conn.close()

@mcp.tool()
def register_architectural_change(file_path: str, ecosystem: str, description: str) -> str:
    """
    Registra o actualiza de manera segura el índice cuando un agente crea un nuevo nodo.
    """
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO codebase_index (file_path, ecosystem, description) 
            VALUES (?, ?, ?) 
            ON CONFLICT(file_path) 
            DO UPDATE SET description=excluded.description, last_updated=CURRENT_TIMESTAMP
        ''', (file_path, ecosystem, description))
        conn.commit()
        return f"Cambio arquitectónico registrado con éxito para {file_path}"
    except Exception as e:
        return f"Error de inserción: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    # Inicia el servidor usando Standard Input/Output
    mcp.run(transport='stdio')
