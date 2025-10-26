class Entry:
    """
    Each object represent a single row of data; used to aid in data cleaning
    de-duplicating.
    """
    def __init__(self, row, id):
        self.id = id
        self.facility_name = row[0]
        self.address = row[1]
        self.last_inspected = row[2]
        self.violations = row[3]
        self.num_critical_violations = row[4]
        self.num_not_corrected = row[5]
        self.num_non_critical_violations = row[6]
        self.description = row[7]
        self.local_health_department = row[8]
        self.county = row[9]
        self.facility_address = row[10]
        self.city = row[11]
        self.zipcode = row[12]
        self.nysdoh = row[13]
        self.municipality = row[14]
        self.operation_name = row[15]
        self.permit_expiration_date = row[16]
        self.business_name = row[17]
        self.corp_name = row[18]
        self.operator_last_name = row[19]
        self.operator_first_name = row[20]
        self.nys_health_operation_id = row[21]
        self.inspection_type = row[22]
        self.comments = row[23]
        self.state = row[24]
        self.coordinates = row[25]