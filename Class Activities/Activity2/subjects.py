class Subject:
    def __init__(self, name, year_level, code, enrolled):
        self.name = name
        self.year_level = year_level
        self.code = code
        self.enrolled = enrolled

    def display_details(self):
        print(f"Code: {self.code} | Name: {self.name} | Year: {self.year_level} | Enrolled: {self.enrolled}")