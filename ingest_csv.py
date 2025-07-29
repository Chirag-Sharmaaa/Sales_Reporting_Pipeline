import pandas as pd
from sqlalchemy import create_engine
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'superstore_sales_data.csv')

df = pd.read_csv(csv_path, encoding='ISO-8859-1')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')

username = 'postgres'
password = '1542'
host = 'localhost'
port = '5432'
database = 'Sales_Reporting'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

df.to_sql('superstore_csv_raw', con=engine, if_exists='replace', index=False)

print("CSV successfully ingested into PostgreSQL!")