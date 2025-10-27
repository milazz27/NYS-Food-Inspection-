class Entry:
    """
    Each object represent a single row of data; used to aid in data cleaning
    de-duplicating.
    """
    def __init__(self, row, id, violation, code):
        self.id = id
        self.facility_name = row.get('FACILITY', '')
        self.address = row.get('ADDRESS', '')
        self.last_inspected = row.get('LAST INSPECTED', '')
        self.violation_code = code
        self.violation = violation
        self.num_critical_violations = row.get('TOTAL # CRITICAL VIOLATIONS', '')
        self.num_not_corrected = row.get('TOTAL #CRIT.  NOT CORRECTED ', '')
        self.num_non_critical_violations = row.get('TOTAL # NONCRITICAL VIOLATIONS', '')
        self.description = row.get('DESCRIPTION', '')
        self.local_health_department = row.get(' LOCAL HEALTH DEPARTMENT', '')
        self.county = row.get('COUNTY', '')
        self.facility_address = row.get('FACILITY ADDRESS', '')
        self.city = row.get('CITY', '')
        self.zipcode = row.get('ZIP CODE', '')
        self.nysdoh = row.get('NYSDOH GAZETTEER (1980)', '')
        self.municipality = row.get('MUNICIPALITY', '')
        self.operation_name = row.get('OPERATION NAME', '')
        self.permit_expiration_date = row.get('PERMIT EXPIRATION DATE', '')
        self.business_name = row.get('PERMITTED  (D/B/A)', '')
        self.corp_name = row.get('PERMITTED  CORP. NAME', '')
        self.operator_last_name = row.get('PERM. OPERATOR LAST NAME', '')
        self.operator_first_name = row.get('PERM. OPERATOR FIRST NAME', '')
        self.nys_health_operation_id = row.get('NYS HEALTH OPERATION ID', '')
        self.inspection_type = row.get('INSPECTION TYPE', '')
        self.comments = row.get('INSPECTION COMMENTS', '')
        self.state = row.get('FOOD SERVICE FACILITY STATE', '')
        self.coordinates = row.get('Location1', '')