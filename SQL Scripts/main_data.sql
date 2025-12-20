 --Table to drop all data into prior to further parsing into other tables

 DROP TABLE IF EXISTS all_rest_data;

 CREATE TABLE all_rest_data(
    rid VARCHAR(50),
    facility_name TEXT,
    address TEXT,
    last_inspected DATE,
    violation_code VARCHAR(3),
    violation TEXT,
    violation_count INT,
    num_crit_not_corrected INT,
    num_not_critical INT,
    description TEXT,
    local_health_dept TEXT,
    county TEXT,
    facility_addresss TEXT,
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
