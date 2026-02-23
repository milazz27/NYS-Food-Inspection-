import psycopg2
import csv
import boto3

def drive_data_export():
    ##connect to the database
    conn = psycopg2.connect(
        database = "food_safety",
        user = "postgres",
        password = "postgres",
        host = "127.0.0.1",
        port = "5432"
    )
    print("Connected to PostgreSQL")

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
    print("Codes cleared")

    cursor.execute(setup_violation_code)
    print("Violation Codes Created")

    with open("../Data/code_data.csv", 'r') as code_file:
        next(code_file)
        cursor.copy_from(code_file, 'violation_codes', sep='+')

    conn.commit()
    print("Violation Codes Table Filled Successfully")


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
    print("Depts cleared")

    cursor.execute(setup_health_depts)
    print("Health Depts Table Created")


    with open("../Data/county_health_departments.csv", 'r') as code_file2:
        next(code_file2)
        cursor.copy_from(code_file2, 'health_depts', sep=',')

    conn.commit()
    print("Health Depts Table Filled Successfully")


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
    print("Raw Data cleared")

    cursor.execute(setup_raw_table)
    print("all_rest_data Table Created")

    copy_sql = """
    COPY all_rest_data (
     rid, fullname, address, last_inspected, violation_code,
     violation, violation_count, num_crit_not_corrected,
     num_not_critical, description, local_health_dept, county,
     facility_address, city, zipcode, nysdoh, municipality,
     operation_name, permit_exp_date, permitted,
     corp_name, operator_lname, operator_fname, nys_health_id,
     inspection_type, comments, state, latitude, longitude
    )
    FROM STDIN WITH (FORMAT csv, HEADER true, DELIMITER '^', NULL '');
    """

    with open("../Data/restaurants2.csv", "r", encoding="utf-8", errors="ignore") as f:
        cursor.copy_expert(copy_sql, f)

    conn.commit()
    print("All Rest Data Inserted Successfully")

    print("Data sent to violation_codes, health_depts, & all_rest_data 👹⚡")

    conn.close()

drive_data_export()