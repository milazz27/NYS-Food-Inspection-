from data import Data
from data import Entry
import csv
import uuid
import requests
from io import StringIO

def create_id():
    return str(uuid.uuid4())

def read_from_file(reader, data):
    """
    Read each line from the input CSV and create Entry objects for each row.
    Each individual violation becomes its own Entry.
    """
    numSkipped = 0
    for row in reader:

        # throw out entries where there is no name listed -- unhelpful
        facility = row.get('facility', '').strip()
        #print(facility)
        if facility == '':
            numSkipped += 1
            continue

        violations = row.get('violations', '').strip()
        indiv_violations = [v.strip() for v in violations.split(';') if v.strip()]
        rid = create_id()

        # If no violations field at all
        if not indiv_violations:
            entry = Entry(row, rid, None, None)
            data.process_new_entry(entry)
            continue

        for v in indiv_violations:
            if 'No violations found' in v:
                entry = Entry(row, rid, v, None)
                data.process_new_entry(entry)
                break

            if v.startswith('Item '):
                try:
                    code_part, desc_part = v.split('- ', 1)
                    violation_code = code_part.replace('Item ', '').strip()
                    violation_str = desc_part.strip()
                except ValueError:
                    # Malformed violation string
                    violation_code = None
                    violation_str = v

                entry = Entry(row, rid, violation_str, violation_code)
                data.process_new_entry(entry)
    return numSkipped


def write_to_csv(data):
    with open("../Data/restaurants2.csv", "w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file,delimiter='^')
        writer.writerow(["rid", "facility_name","address","last_inspected","violation_code", "violation", \
                         "violation_count","num_crit_not_corrected","num_non_critical","description","local_health_dept", \
                         "county","facility_address","city","zipcode","nysdoh","municipality","operation_name", \
                         "permit_exp_date","permitted","corp_name","operator_lname","operator_fname", \
                         "nys_health_id","inspection_type","comments","state","latitude","longitude"])
        for entry in data.data.values():
            for ele in entry:
                writer.writerow(ele.row)

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def drive_cleaning():
    data = Data()
    url = "https://health.data.ny.gov/resource/cnih-y5dw.csv?$limit=50000"
    csv_text = fetch_data(url)
    reader = csv.DictReader(StringIO(csv_text))
    num = read_from_file(reader, data)
    write_to_csv(data)
    print("Data cleaned & written to restaurants2.csv 😈➡️😇")
    print("Number of skipped entries: {}".format(num))


