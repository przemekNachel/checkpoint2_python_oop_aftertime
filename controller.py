from address_book import AddressBook
from view import View


class Controller:

    @classmethod
    def start(cls):
        user_input = None
        while user_input != "0":
            View.display_main_menu()
            user_input = View.get_menu_choice()
            if user_input == "1":
                cls.address_book_start(cls.create_new_address_book())
            if user_input == "2":
                cls.address_book_start(cls.open_address_book_from_file())
                
    @classmethod
    def address_book_start(cls, address_book):
        user_input = None
        while user_input != "0":
            View.display_address_book_menu()
            user_input = View.get_menu_choice()
            if user_input == "1":
                cls.display_addresses(address_book)
            if user_input == "2":
                cls.add_address(address_book)
            if user_input == "3":
                cls.remove_address(address_book)
            if user_input == "4":
                cls.search_address(address_book)
            if user_input == "5":
                cls.save_book(address_book)
            

    @staticmethod
    def create_new_address_book():
        name = View.ask_for_adress_book_name()
        return AddressBook(name)

    @staticmethod
    def open_address_book_from_file():
        file_name = View.ask_for_file_name()
        name = file_name[:-4]
        return AddressBook.create_from_csv(name, file_name)

    @staticmethod
    def display_addresses(address_book):
        View.display_addresses(address_book.addresses)

    @staticmethod
    def add_address(address_book):
        address = View.add_address()
        address_book.add_address(address)

    @staticmethod
    def remove_address(address_book):
        address_to_remove = View.remove_address(address_book)
        address_book.remove_address(address_to_remove)

    @staticmethod
    def search_address(address_book):
        pass

    @staticmethod
    def save_book(address_book):
        pass
