import os
import duckdb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_DIR = os.path.join(BASE_DIR, "Datasets")
DB_PATH = os.path.join(BASE_DIR, "crm_dw.duckdb")

def ingest_data():
    print(f"Connecting to DuckDB database at: {DB_PATH}")
    conn = duckdb.connect(DB_PATH)
    
    
    tables = {
        "raw_accounts": "accounts.csv",
        "raw_products": "products.csv",
        "raw_sales_pipeline": "sales_pipeline.csv",
        "raw_sales_teams": "sales_teams.csv"
    }

    print("Starting data ingestion into 'main' schema...")
    
    for table_name, file_name in tables.items():
        file_path = os.path.join(DATASETS_DIR, file_name)
        if os.path.exists(file_path):
            clean_path = file_path.replace('\\', '/')
            
            query = f"""
                CREATE OR REPLACE TABLE {table_name} AS 
                SELECT * FROM read_csv_auto('{clean_path}');
            """
            conn.execute(query)
            count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
            print(f" Loaded '{table_name}' with {count} rows.")
        else:
            print(f" File not found: {file_path}")

    conn.close()
    print("Ingestion completed successfully!")

if __name__ == "__main__":
    ingest_data()