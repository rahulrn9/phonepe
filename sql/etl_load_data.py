
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Load datasets
transactions_df = pd.read_csv('../data/transactions_aggregated.csv')
insurance_df = pd.read_csv('../data/insurance_aggregated.csv')

# Define DB connection (update these with actual credentials)
user = 'your_username'
password = 'your_password'
host = 'localhost'
port = '5432'
database = 'phonepe_db'

# Create connection engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

# Load data to database
transactions_df.to_sql('aggregated_transaction', engine, if_exists='append', index=False)
insurance_df.to_sql('aggregated_insurance', engine, if_exists='append', index=False)

print("✅ Data inserted successfully.")
