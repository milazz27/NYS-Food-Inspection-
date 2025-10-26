from entry import Entry

class Data:
    def __init__(self):
        """
        Contains the overall details from the data.
        Each dictionary stores frequencies of categories.
        """
        self.data = {}
        self.inspection_type_freq = {}
        self.nysdoh_freq = {}
        self.description_freq = {}

    def insert_inspection_type(self, inspection_type):
        """
        Adds or updates the frequency of an inspection type.
        """
        self.inspection_type_freq[inspection_type] = self.inspection_type_freq.get(inspection_type, 0) + 1

    def insert_nysdoh(self, nysdoh_code):
        """
        Adds or updates the frequency of an NYSDOH code.
        """
        self.nysdoh_freq[nysdoh_code] = self.nysdoh_freq.get(nysdoh_code, 0) + 1

    def insert_description(self, desc):
        """
        Adds or updates the frequency of a description.
        """
        self.description_freq[desc] = self.description_freq.get(desc, 0) + 1

    def process_new_entry(self, entry):
        """
        Completes the updating process for a new Entry object.
        """
        # Add the entry itself
        self.data[entry.id] = entry

        # Update analysis metrics
        self.insert_inspection_type(entry.inspection_type)
        self.insert_nysdoh(entry.nysdoh)
        self.insert_description(entry.description)
