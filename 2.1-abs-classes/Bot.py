from AddressBook import *
from abc import ABC, abstractmethod


class AbstractBot(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def congratulate(self):
        pass

    def handle(self, action):
        match action:
            case 'add':
                self.add()
            case 'search':
                self.search()
            case 'edit':
                self.edit()
            case 'remove':
                self.remove()
            case 'save':
                self.save()
            case 'load':
                self.load()
            case 'congratulate':
                self.congratulate()
            case 'view':
                self.view()
            case 'exit':
                pass
            case _:
                print("There is no such command!")


class Bot(AbstractBot):
    def __init__(self):
        self.book = AddressBook()

    def add(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        return self.book.add(record)

    def search(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (self.book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)

    def edit(self):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        return self.book.edit(contact_name, parameter, new_value)

    def remove(self):
        pattern = input("Remove (contact name or phone): ")
        return self.book.remove(pattern)

    def save(self):
        file_name = input("File name: ")
        return self.book.save(file_name)

    def load(self):
        file_name = input("File name: ")
        return self.book.load(file_name)

    def view(self):
        print(self.book)

    def congratulate(self):
        print(self.book.congratulate())

    # def handle(self, action):
    #     match action:
    #         case 'add':
    #             self.add()
    #         case 'search':
    #             self.search()
    #         case 'edit':
    #             self.edit()
    #         case 'remove':
    #             self.remove()
    #         case 'save':
    #             self.save()
    #         case 'load':
    #             self.load()
    #         case 'congratulate':
    #             self.congratulate()
    #         case 'view':
    #             self.view()
    #         case 'exit':
    #             pass
    #         case _:
    #             print("There is no such command!")
