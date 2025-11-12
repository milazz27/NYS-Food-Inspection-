import psycopg2
import csv


##connect to the database
conn = psycopg2.connect(database = "food_safety",
                        user = "postgres", password = "postgres",
                        host = "127.0.0.1", port = '5432')

conn.autocommit = True
cursor = conn.cursor()

clear_codes = '''DROP TABLE IF EXISTS violation_codes;'''
clear_depts = '''DROP TABLE IF EXISTS health_depts;'''



setup_violation_code = '''
                        CREATE TABLE violation_codes(
                            code VARCHAR(3) PRIMARY KEY,
                            description TEXT,
                            category TEXT,
                            priority TEXT);
                        '''

#loading code data into db
cursor.execute(clear_codes)
cursor.execute(setup_violation_code)

with open("../Data/code_data.csv", 'r') as code_file:
    next(code_file)
    cursor.copy_from(code_file, 'violation_codes', sep='+')

conn.commit()

setup_health_depts = '''
                        CREATE TABLE health_depts(
                            county TEXT PRIMARY KEY,
                            department_name TEXT,
                            phone_num VARCHAR(12),
                            fax VARCHAR(12),
                            url TEXT);'''

#loading dept data into db
cursor.execute(clear_depts)
cursor.execute(setup_health_depts)

with open("../Data/county_health_departments.csv", 'r') as code_file2:
    next(code_file2)
    cursor.copy_from(code_file2, 'health_depts', sep=',')

conn.commit()

conn.close()
