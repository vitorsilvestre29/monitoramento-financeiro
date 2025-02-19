import pandas as pd
import pyodbc

def connect_to_db():
    try:
        
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=GPPLOJA03\\DEVITOR;'  
            'DATABASE=Financeiro;'  
            'Trusted_Connection=yes;'  
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None

def fetch_data(query):
    conn = connect_to_db()
    if conn:
        try:
            data = pd.read_sql(query, conn)
            return data
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
        finally:
            conn.close()
    else:
        print("Não foi possível conectar ao banco de dados.")
        return None