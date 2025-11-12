from data import Data
from data import Entry
import csv
import uuid

def create_id():
    """
    creates a unique id for each row of data
    """
    return uuid.uuid4().hex[:8]

def read_from_file(filename, data):
    """
    read each line from the input file and create Entry objects for each row, hold them in dictionary 
    within Data object in dictionary by id.
    """
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            violations = row.get('VIOLATIONS', '')
            indiv_violations = violations.split(';')

            #ensuring that there will be an entry for each individual violation for
            #data modeling purposes
            for v in indiv_violations:
                if v != '':
                    if v.find('No violations found') != -1:
                        entry = Entry(row, create_id(), v, None)
                        data.process_new_entry(entry)
                        break
                    if v.find('Item ') != -1:
                        get_code = v.split('- ')
                        violation_code = get_code[0].strip()
                        violation_str = get_code[1].strip()
                        entry = Entry(row, create_id(), violation_str, violation_code,)
                        data.process_new_entry(entry)

def write_to_csv(data):
    with open("restaurants.csv", "w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["rid", "facility_name","address","last_inspected","violation_code", "violation", \
                         "violation_count","num_crit_not_corrected","num_non_critical","description","local_health_dept", \
                         "county","facility_address","city","zipcode","nysdoh","municipality","operation_name", \
                         "permit_exp_date","permitted","business","corp_name","operator_lname","operator_fname", \
                         "nys_health_id","inspection_type","comments","state","coords"])
        for entry in data.data.values():
            writer.writerow(entry.row)



def main():
    data = Data()
    read_from_file("../Data/rawData.csv", data)
    write_to_csv(data)
    print("done")

if __name__ == "__main__":
    main()

