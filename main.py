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
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_id = create_id()
            new_entry = Entry(row, new_id)
            data.process_new_entry(new_entry)



def main():
    data = Data()
    read_from_file("sample_set.csv", data)

if __name__ == "__main__":
    main()

