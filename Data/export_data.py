import psycopg2

##connect to the database
conn = psycopg2.connect(database = "food_safety",
                        user = "postgres", password = "postgres",
                        host = "127.0.0.1", port = '5432')

conn.autocommit = True
cursor = conn.cursor()

setup_violation_code = '''
                        CREATE TABLE violation_codes(
                            code VARCHAR(3) PRIMARY KEY,
                            description TEXT,
                            category TEXT,
                            priority TEXT);
                        '''

grab_code_data = '''
                        COPY violation_codes(code, description, category, priority)
                        FROM 'code_data.csv'
                        DELIMITER ','
                        CSV HEADER;
                '''

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
cursor.execute(setup_violation_code)
cursor.execute(grab_code_data)

#loading dept data into db
cursor.execute(setup_health_depts)
cursor.execute(grab_dept_data)

conn.commit()
conn.close()
