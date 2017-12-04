from address import Address
from work_address import WorkAddress


class AddressBook:

    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        if isinstance(address, Address) or isinstance(address, WorkAddress):
            self.addresses.append(address)
        else:
            raise TypeError

    def find(self, search_phrase):
        self.sort()
        matching_addresses = []
        for address in self.addresses:
            address_attributes = [address.person, address.city, address.street, address.house_no]
            if isinstance(address, WorkAddress):
                address_attributes.append(address.company)
            if search_phrase.lower() in " ".join(address_attributes).lower():
                matching_addresses.append(address)
        return matching_addresses
    
    def sort(self):
        for i in range(len(self.addresses)):
            value = self.addresses[i]
            j = i - 1
            while j >= 0 and self.addresses[j] > value:
                    self.addresses[j+1] = self.addresses[j]
                    j -= 1
            self.addresses[j+1] = value

    @staticmethod
    def create_from_csv(list_name, csv_path):
        address_book = AddressBook(list_name)
        list_of_addresses = []
        with open(csv_path) as file:
            for line in file:
                list_of_addresses.append(line[:-1].split(","))
            list_of_addresses.pop(0)
        for address in list_of_addresses:
            if address[-1] == "":
                address_book.addresses.append(Address(*address[:-1]))
            else:
                address_book.addresses.append(WorkAddress(*address))
        return address_book

    def save_to_csv(self):
        with open(self.name + ".csv", "w") as file:
            file.write("person,city,street,house_no,company\n")
            for address in self.addresses:
                address_data = [address.person, address.city, address.street, address.house_no]
                if isinstance(address, WorkAddress):
                    address_data.append(address.company)
                else:
                    address_data.append("")
                file.write(",".join(address_data)+"\n")

    def remove_address(self, address):
        self.addresses.remove(address)

    
