import os
import string


class View:

    @staticmethod
    def clear_terminal():
        os.system("clear")

    @staticmethod
    def display_main_menu():
        View.clear_terminal()
        print("1. Create new address book\n2. Open address book from file\n\n0. Exit\n")

    @staticmethod
    def display_address_book_menu():
        View.clear_terminal()
        print("1. List addresses\n2. Add a new address\n3. Remove an address\n4. Search for an address")
        print("5. Save this address book\n\n0. Back to main menu\n")

    @staticmethod
    def get_menu_choice():
        return input("Choice: ")

    @staticmethod
    def ask_for_adress_book_name():
        View.clear_terminal()
        return input("Type adress book name\n")

    @staticmethod
    def ask_for_file_name():
        correct_file_name = 0
        while not correct_file_name:
            View.clear_terminal()
            file_name = input("Type file name\n")
            try:
                open(file_name)
                correct_file_name = 1
            except FileNotFoundError:
                pass
        return file_name

    @staticmethod
    def display_addresses(addresses):
        View.clear_terminal()
        if addresses:
            for address in addresses:
                print(address)
        else:
            print("No addreses to show.")
        input("\nPress enter to continue...\n")

    @staticmethod
    def remove_address(address_book):
        addresses = address_book.addresses
        if addresses:
            while True:
                View.clear_terminal()
                i = 1
                for address in addresses:
                    print(str(i) + ". " + str(address))
                    i += 1
                index = input("\nType index of address to remove: ")
                if index.isdigit():
                    if int(index) > 0 and int(index) <= len(addresses):
                        return addresses[int(index) - 1]

    @classmethod
    def add_address(cls):
        address = []
        ask_address_messages = ("Type name of person: ", "Type city: ", "Type street: ", "Type house number: ", "Type company or leave blank: ")
        i = 0
        while len(address) < 5:
            cls.clear_terminal()
            data = (input(ask_address_messages[i]))
            if i == 3:
                data = cls.format_number(data)
            else:
                data = cls.capitalize_data(data)
            if not data:
                if i == 4:
                    break
                continue
            address.append(data)
            i += 1
        if not address[-1]:
            address.pop()
        return address

    @staticmethod
    def capitalize_data(data):
        allowed_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [",", ".", " "]
        no_digits_string = ''.join([i for i in data if not i.isdigit()])
        only_allowed_chars_from_string = ''.join([i for i in data if i in allowed_chars])
        return " ".join([string.capitalize() for string in only_allowed_chars_from_string.split(" ")])

    def format_number(data):
        allowed_chars = ["/"]
        digits_string = ''.join([i for i in data if i.isdigit() or i in allowed_chars])
        return digits_string

    @staticmethod
    def search_address():
        View.clear_terminal()
        return input("Type what you want to search: ")

