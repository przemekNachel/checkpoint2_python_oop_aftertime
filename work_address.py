class WorkAddress:

    def __init__(self, person, city, street, house_no, company):
        self.person = person
        self.city = city
        self.street = street
        self.house_no = house_no
        self.company = company

    def get_full_address(self):
        return "{}, {}, {} {}, {}".format(self.person, self.city, self.street, self.house_no, self.company)

    def __gt__(self, other):
        return self.get_full_address() > other.get_full_address()

    def __ge__(self, other):
        return self.get_full_address() >= other.get_full_address()

    def __lt__(self, other):
        return self.get_full_address() < other.get_full_address()

    def __le__(self, other):
        return self.get_full_address() <= other.get_full_address()

    def __eq__(self, other):
        return self.get_full_address() == other.get_full_address()

    def __ne__(self, other):
        return self.get_full_address() != other.get_full_address()

    def __str__(self):
        address = self.get_full_address()
        return address
