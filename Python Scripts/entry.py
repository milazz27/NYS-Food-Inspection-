class Entry:
    """
    Each object represent a single row of data; used to aid in data cleaning
    de-duplicating.
    """
    def __init__(self, row, id, violation, code):
        self.id = id
        self.facility_name = row.get('FACILITY', '').strip()
        self.address = row.get('ADDRESS', '').strip()
        self.last_inspected = row.get('LAST INSPECTED', '').strip()
        self.violation_code = code
        self.violation = violation
        self.num_critical_violations = int(row.get('TOTAL # CRITICAL VIOLATIONS', '').strip())
        self.num_not_corrected = int(row.get('TOTAL #CRIT.  NOT CORRECTED ', '').strip())
        self.num_non_critical_violations = int(row.get('TOTAL # NONCRITICAL VIOLATIONS', '').strip())
        self.description = row.get('DESCRIPTION', '').strip()
        self.local_health_department = row.get(' LOCAL HEALTH DEPARTMENT', '').strip()
        self.county = row.get('COUNTY', '').strip()
        self.facility_address = row.get('FACILITY ADDRESS', '').strip()
        self.city = row.get('CITY', '').strip()
        self.zipcode = row.get('ZIP CODE', '').strip()
        self.nysdoh = row.get('NYSDOH GAZETTEER (1980)', '').strip()
        self.municipality = row.get('MUNICIPALITY', '').strip()
        self.operation_name = row.get('OPERATION NAME', '').strip()
        self.permit_expiration_date = row.get('PERMIT EXPIRATION DATE', '').strip()
        self.business_name = row.get('PERMITTED  (D/B/A)', '').strip()
        self.corp_name = row.get('PERMITTED  CORP. NAME', '').strip()
        self.operator_last_name = row.get('PERM. OPERATOR LAST NAME', '').strip()
        self.operator_first_name = row.get('PERM. OPERATOR FIRST NAME', '').strip()
        self.nys_health_operation_id = row.get('NYS HEALTH OPERATION ID', '').strip()
        self.inspection_type = row.get('INSPECTION TYPE', '').strip()
        self.comments = row.get('INSPECTION COMMENTS', '').strip()
        self.state = row.get('FOOD SERVICE FACILITY STATE', '').strip()
        self.coordinates = row.get('Location1', '').strip()