DROP TABLE IF EXISTS facilities_healthdepts;
DROP TABLE IF EXISTS violation_details;
DROP TABLE IF EXISTS inspection_comments;
DROP TABLE IF EXISTS facility_addresses;
DROP TABLE IF EXISTS permits;
DROP TABLE IF EXISTS facilities;

-- add a violations summary table

CREATE TABLE facilities(
    fid VARCHAR(8) PRIMARY KEY,
    fullname TEXT NOT NULL,
    facility_type TEXT,
    last_inspected DATE
);

CREATE TABLE permits(
    fid VARCHAR(8),
    expiration_date DATE,
    nys_op_id TEXT,
    operator_fname TEXT,
    operator_lname TEXT,
    FOREIGN KEY(fid) REFERENCES facilities(fid) ON DELETE CASCADE,
    PRIMARY KEY(fid, expiration_date)
);

CREATE TABLE facility_addresses(
    fid VARCHAR(8),
    street_address TEXT,
    county TEXT,
    city TEXT,
    zip TEXT,
    nysdoh TEXT,
    latitude REAL,
    longitude REAL,
    FOREIGN KEY (fid) REFERENCES facilities(fid) ON DELETE CASCADE,
    PRIMARY KEY (fid)
);

CREATE TABLE violation_details(
    fid VARCHAR(8),
    inspection_date DATE,
    inspection_type TEXT,
    violation_code VARCHAR(3),
    violation_description TEXT,
    FOREIGN KEY (fid) REFERENCES facilities(fid) ON DELETE CASCADE,
    PRIMARY KEY (fid, inspection_date, violation_code)
);

CREATE TABLE inspection_comments(
    fid VARCHAR(8),
    comments TEXT,
    FOREIGN KEY (fid) REFERENCES facilities(fid) ON DELETE CASCADE,
    PRIMARY KEY (fid)
);

CREATE TABLE facilities_healthdepts(
    fid VARCHAR(8),
    county TEXT,
    FOREIGN KEY (fid) REFERENCES facilities(fid) ON DELETE CASCADE
);

--- Code for inserting data to tables

-- Inserting into facilities
INSERT INTO facilities(fid, fullname, facility_type, last_inspected)
SELECT
    a.rid,
    a.fullname,
    a.description,
    a.last_inspected
FROM
    all_rest_data a
GROUP BY
    a.rid, a.fullname, a.description, a.last_inspected
;

-- Insert into permits
INSERT INTO permits(fid, expiration_date, nys_op_id, operator_fname, operator_lname)
SELECT
    a.rid,
    a.permit_exp_date,
    a.nys_health_id,
    a.operator_fname,
    a.operator_lname
FROM
    all_rest_data a
WHERE
    a.permit_exp_date IS NOT NULL
    and a.nys_health_id IS NOT NULL
GROUP BY
    a.rid, a.permit_exp_date, a.nys_health_id, a.operator_fname, a.operator_lname
;

-- Insert into facility addresses
INSERT INTO facility_addresses(fid, street_address, county, city, zip, nysdoh, latitude, longitude)
SELECT
    a.rid,
    a.address,
    a.county,
    a.city,
    a.zipcode,
    a.nysdoh,
    a.latitude,
    a.longitude
FROM
    all_rest_data a
GROUP BY
    a.rid, a.address, a.county, a.city, a.zipcode, a.nysdoh, a.latitude, a.longitude
;

-- Insert into inspection details
INSERT INTO violation_details(fid, inspection_date, inspection_type, violation_code, violation_description)
SELECT
    a.rid,
    a.last_inspected,
    a.inspection_type,
    a.violation_code,
    a.violation
FROM
    all_rest_data a
WHERE
    a.violation_code IS NOT NULL
GROUP BY
    a.rid, a.last_inspected, a.inspection_type, a.violation_code, a.violation
;

-- Insert into inspection comments table
INSERT INTO inspection_comments(fid, comments)
SELECT
    a.rid,
    a.comments
FROM
    all_rest_data a
GROUP BY
    a.rid, a.comments
;

-- Insert into facilities_health_depts
INSERT INTO facilities_healthdepts(fid, county)
SELECT
    a.rid,
    a.county
FROM
    all_rest_data a
GROUP BY
    a.rid, a.county
;

