from datetime import datetime

from datetime import datetime

def safe_int(val):
    try:
        return int(val)
    except (TypeError, ValueError):
        return 0


class Entry:
    """
    Each object represents a single row of data; used to aid in data cleaning
    and de-duplicating.
    """

    def __init__(self, row, id, violation, code):
        self.id = id
        self.facility_name = row.get('facility', '').strip()
        self.address = row.get('address', '').strip()

        # Inspection date (ISO → SQL)
        orig_date = row.get('date', '').strip()
        try:
            sql_date = datetime.fromisoformat(orig_date.replace("Z", ""))
            self.last_inspected = sql_date.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            self.last_inspected = None

        self.violation_code = code
        self.violation = violation

        # Violation counts
        self.violation_count = safe_int(row.get('total_critical_violations'))
        self.num_crit_not_corrected = safe_int(row.get('total_crit_not_corrected'))
        self.num_non_critical = safe_int(row.get('total_noncritical_violations'))

        self.description = row.get('description', '').strip()
        self.local_health_department = row.get('local_health_department', '').strip()
        self.county = row.get('county', '').strip()
        self.facility_address = row.get('facility_address', '').strip()
        self.city = row.get('city', '').strip()
        self.zipcode = row.get('zip_code', '').strip()
        self.nysdoh = row.get('nysdoh_gazetteer_1980', '').strip()
        self.municipality = row.get('municipality', '').strip()
        self.operation_name = row.get('operation_name', '').strip()

        # Permit expiration date
        orig_date = row.get('permit_expiration_date', '').strip()
        try:
            sql_date = datetime.fromisoformat(orig_date.replace("Z", ""))
            self.permit_expiration_date = sql_date.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            self.permit_expiration_date = None

        self.permitted = row.get('permitted_d_b_a', '').strip()
        self.corp_name = row.get('permitted_corp_name', '').strip()
        self.operator_last_name = row.get('perm_operator_last_name', '').strip()
        self.operator_first_name = row.get('perm_operator_first_name', '').strip()
        self.nys_health_operation_id = row.get('nys_health_operation_id', '').strip()
        self.inspection_type = row.get('inspection_type', '').strip()
        self.comments = row.get('inspection_comments', '').strip()
        self.state = row.get('food_service_facility_state', '').strip()

        # Coordinates
        coords = row.get('location1', '').strip()
        if coords.startswith("(") and coords.endswith(")"):
            lat, lon = coords.strip("()").split(",")
            self.latitude = lat.strip()
            self.longitude = lon.strip()
        else:
            self.latitude = None
            self.longitude = None

        self.row = format_csv_row(self)


def format_csv_row(self):
    return [
        self.id,
        self.facility_name,
        self.address,
        self.last_inspected,
        self.violation_code,
        self.violation,
        self.violation_count,
        self.num_crit_not_corrected,
        self.num_non_critical,
        self.description,
        self.local_health_department,
        self.county,
        self.facility_address,
        self.city,
        self.zipcode,
        self.nysdoh,
        self.municipality,
        self.operation_name,
        self.permit_expiration_date,
        self.permitted,
        #self.business,
        self.corp_name,
        self.operator_last_name,
        self.operator_first_name,
        self.nys_health_operation_id,
        self.inspection_type,
        self.comments,
        self.state,
        self.latitude,
        self.longitude
    ]