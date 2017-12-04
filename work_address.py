from address import Address


class WorkAddress(Address):

    def __init__(self, person, city, street, house_no, company):
        self.person = person
        self.city = city
        self.street = street
        self.house_no = house_no
        self.company = company

    def get_full_address(self):
        return "{}, {}, {} {}, {}".format(self.person, self.city, self.street, self.house_no, self.company)
