DROP TABLE IF EXISTS facilities;
DROP TABLE IF EXISTS permits;
DROP TABLE IF EXISTS facility_address;
DROP TABLE IF EXISTS inspection_details;
DROP TABLE IF EXISTS facilities_healthdepts;

CREATE TABLE facilities(
    fid VARCHAR(8) PRIMARY KEY,
    name TEXT NOT NULL,
    facility_type TEXT,
    last_inspected DATE -- will need to convert from / to - in between
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

CREATE TABLE facility_address(
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

CREATE TABLE inspection_details(
    fid VARCHAR,
    inspection_date DATE,
    violation_code VARCHAR(3),
    notes TEXT,
    FOREIGN KEY (fid) REFERENCES facilities(fid) ON DELETE CASCADE,
    PRIMARY KEY (fid, inspection_date, violation_code)
);

CREATE TABLE facilities_healthdepts(
    fid VARCHAR(8),
    county TEXT,
    FOREIGN KEY (fid) REFERENCES facilities(fid) ON DELETE CASCADE
);