from entry import Entry

class Data:
    def __init__(self):
        """
        Contains the overall details from the data, frequency relates to unique members of
        each of the categories.
        """
        self.data = {}
        self.inspection_type = {}
        self.nysdoh = {}
        self.description = {}
        self.inspection_type = {}
    
    def insert_inspection_type(self, type):
        """
        adds new inspection type to dictionary and updates frequency
        """
        if type not in self.inspection_type:
            self.inspection_type[type] = 0
        self.inspection_type[type] += 1

    def insert_nysdoh(self, title):
        """
        inserts new nysdoh data to dictionary and updates frequency
        """
        if title not in self.nysdoh:
            self.nysdoh[type] = 0
        self.nysdoh[type] += 1

    def insert_description(self, desc):
        """
        inserts new description to dictionary and updates frequency
        """
        if desc not in self.description:
            self.description[desc] = 0
        self.description[desc] += 1

    def insert_inspection_type(self, type):
        """
        inserts new inspection type to the dictionary and updates the frequency
        """
        if type not in self.inspection_type:
            self.inspection_type[type] = 0
        self.insert_description[type] += 1

    def process_new_entry(self, entry):
        """
        completes the updating process for a new entry object in dataset
        """
        #adding in new entry by its id
        self.data[entry.id] = entry

        #updating analysis metrics
        self.insert_inspection_type(self, entry.inspection_type)
        self.insert_nysdoh(self, entry.nysdoh)
        self.insert_description(self, entry.description)
        self.insert_inspection_type(self, entry.inspection_type)

