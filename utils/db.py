import sqlite3
import pandas as pd


DB_PATH = "data/sample.db"

def run_query(query: str) -> pd.DataFrame:
    """
    Execute a SQL query and return the results as a pandas DataFrame.
    
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return str(e)
    finally:
        conn.close()