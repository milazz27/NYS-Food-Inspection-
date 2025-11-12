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

with open('../Data/codes_data.csv', 'r') as code_file:
    reader = csv.reader(code_file)
    next(reader)
    for row in reader:
        cursor.execute(
            '''
            INSERT INTO violation_codes VALUES(row);
            ''')
    conn.commit()

setup_health_depts = '''
                        CREATE TABLE health_depts(
                            county TEXT PRIMARY KEY,
                            department_name TEXT,
                            phone_num VARCHAR(12),
                            fax VARCHAR(12),
                            url TEXT);'''

grab_dept_data = '''
                    COPY health_depts(County, Department, Phone, Fax, Website)
                    FROM 'county_health_departments.csv'
                    DELIMITER ','
                    CSV HEADER;
                '''

#loading code data into db
cursor.execute(clear_codes)
cursor.execute(setup_violation_code)

#loading dept data into db
cursor.execute(clear_depts)
cursor.execute(setup_health_depts)
cursor.execute(grab_dept_data)

conn.commit()
conn.close()
