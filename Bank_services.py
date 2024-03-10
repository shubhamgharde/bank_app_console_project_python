from abc import ABC,abstractmethod

class Bank_Services(ABC):

    @abstractmethod
    def add_customer(self):
        pass

    @abstractmethod
    def delete_customer(self):
        pass

    @abstractmethod
    def update_customer(self):
        pass

    @abstractmethod
    def get_list_of_customer(self):
        pass

    @abstractmethod
    def get_balance_of_customer(self):
        pass

    @abstractmethod
    def search_by_account_type(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass