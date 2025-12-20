import psycopg2
import csv

def drive_data_export():
    ##connect to the database
    conn = psycopg2.connect(database = "food_safety",
                            user = "postgres", password = "postgres",
                            host = "127.0.0.1", port = '5432')

    conn.autocommit = True
    cursor = conn.cursor()

    clear_codes = '''DROP TABLE IF EXISTS violation_codes;'''
    clear_depts = '''DROP TABLE IF EXISTS health_depts;'''
    clear_raw = '''DROP TABLE IF EXISTS all_rest_data;'''

    #violation code data
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


    #health dept code
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


    setup_raw_table = '''
                        CREATE TABLE all_rest_data(
                            rid VARCHAR(50),
                            fullname TEXT,
                            address TEXT,
                            last_inspected DATE,
                            violation_code VARCHAR(8),
                            violation TEXT,
                            violation_count INT,
                            num_crit_not_corrected INT,
                            num_not_critical INT,
                            description TEXT,
                            local_health_dept TEXT,
                            county TEXT,
                            facility_address TEXT,
                            city TEXT,
                            zipcode TEXT,
                            nysdoh TEXT,
                            municipality TEXT,
                            operation_name TEXT,
                            permit_exp_date DATE,
                            permitted TEXT,
                            business TEXT,
                            corp_name TEXT,
                            operator_lname TEXT,
                            operator_fname TEXT,
                            nys_health_id TEXT,
                            inspection_type TEXT,
                            comments TEXT,
                            state TEXT,
                            latitude DOUBLE PRECISION,
                            longitude DOUBLE PRECISION
                        );
    
                        '''

    cursor.execute(clear_raw)
    cursor.execute(setup_raw_table)

    with open("../Data/restaurants2.csv", 'r', encoding="utf-8", errors="ignore") as raw_file:
        reader = csv.reader(raw_file, delimiter='^')
        next(reader)  # skip header

        insert_sql = """
                     INSERT INTO all_rest_data (rid, fullname, address, last_inspected, violation_code, \
                                                violation, violation_count, num_crit_not_corrected, \
                                                num_not_critical, description, local_health_dept, county, \
                                                facility_address, city, zipcode, nysdoh, municipality, \
                                                operation_name, permit_exp_date, permitted, \
                                                corp_name, operator_lname, operator_fname, nys_health_id, \
                                                inspection_type, comments, state, latitude, longitude)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); \
                     """

        for rowvals in reader:
            # Convert empty strings → None so PostgreSQL stores NULL
            if len(rowvals) != 29:
                print("BAD ROW LENGTH:", len(rowvals))
                print(rowvals)
                raise Exception("Row length mismatch")
            rowvals = [val if val.strip() != "" else None for val in rowvals]

            cursor.execute(insert_sql, rowvals)

    conn.commit()

    print("Data sent to violation_codes, health_depts, & all_rest_data 👹⚡")

    conn.close()
