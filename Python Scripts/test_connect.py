import psycopg2
import boto3

conn = None
try:
    conn = psycopg2.connect(
        host='3.12.59.134',
        port=5432,
        database='foodsafety',
        user='postgres',
        password='Hamilton1776!',
        sslmode='require'
    )
    cur = conn.cursor()
    cur.execute('SELECT version();')
    print(cur.fetchone()[0])
    cur.close()
except Exception as e:
    print(f"Database error: {e}")
    raise
finally:
    if conn:
        conn.close()