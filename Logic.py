from Bank_services import Bank_Services
from Customer_Info import Customer

Customer_List = []

class StateBankOfIndia(Bank_Services):

    def add_customer(self,cust):

        try:
            if type(cust) ==Customer:
                for l_cust in Customer_List:
                    if l_cust.customer_id == cust.customer_id:
                        raise DuplicateCustomer('Duplicate Customer')  
                Customer_List.append(cust)
                print('--'*60)
                print('Customer Added Succefully...!')
            else:
                print('Invalid Customer...!')
        except DuplicateCustomer as d:
            print(d.error_message)
        

    def delete_customer(self,custid):
        for l_cust in Customer_List:
            if l_cust.customer_id == custid:
                Customer_List.remove(l_cust)
                print('Customer Removed Successfully...!')
                print('--'*60)
                print(Customer_List)
                return

    def update_customer(self,cid,**newvalues):
        for l_cust in Customer_List:          
            if l_cust.customer_id == cid:
                l_cust.customer_id == newvalues.get('id',l_cust.customer_id)
                l_cust.customer_name = newvalues.get('name',l_cust.customer_name)
                l_cust.customer_aacount_type = newvalues.get('acc_type',l_cust.customer_aacount_type)
                l_cust.customer_balance = newvalues.get('balance',l_cust.customer_balance)
                print('Customer Successfully Updated..!')
                print('--'*60)
                print(Customer_List)
                return
        print('No Customer Found So Cannot Update...!')
        

    def get_list_of_customer(self):
        print('--'*60)
        return Customer_List

    def get_balance_of_customer(self, custname):
        for l_cust in Customer_List:
            if l_cust.customer_name == custname:
                print('--'*60)
                print("Account balance of",l_cust.customer_name, "is", l_cust.customer_balance)
                return   

    def search_by_account_type(self,acctype):
        temp_list = []
        for l_cust in Customer_List:
            if l_cust.customer_aacount_type == acctype:
                temp_list.append(l_cust)
                print('--'*60)
                print("Saving account holder list :",temp_list)
                break



    def deposit(self,cid,ammount):
        for l_cust in Customer_List:          
            if l_cust.customer_id == cid:
                l_cust.customer_balance += ammount
                print('--'*60)
                print("Deposit successful. \n New balance:", l_cust.customer_balance)
                print("updated list after deposit ",Customer_List)
                return
        print("Customer not found with the given ID:", cid)



    def withdraw(self, cid, amount):
        for l_cust in Customer_List:
            if l_cust.customer_id == cid:
                if l_cust.customer_balance >= amount:
                    l_cust.customer_balance -= amount
                    print('--' * 60)
                    print("Withdraw successful. \n New balance:", l_cust.customer_balance)
                    print("Updated list after withdraw:", Customer_List)
                else:
                    print("Insufficient Balance..!")
                break  
        else:
            print("Customer not found with the given ID:", cid)


class DuplicateCustomer(Exception):

    def __init__(self,message):
        self.error_message = message


       