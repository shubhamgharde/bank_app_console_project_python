from Logic import StateBankOfIndia,Customer,DuplicateCustomer

if __name__ == '__main__':
    Sbi_manager = StateBankOfIndia()

    cust1 = Customer(cid=101,cnm='Shubham Gharde',cbal=500000,ctp='saving')
    Sbi_manager.add_customer(cust1)

    cust2 = Customer(cid=102,cnm='Gaurav Bhonagde',cbal=600000,ctp='current')
    Sbi_manager.add_customer(cust2)

    cust3 = Customer(cid=103,cnm='dattu',cbal=700000,ctp='current')
    Sbi_manager.add_customer(cust3)

    cust3 = Customer(cid=103,cnm='dattu',cbal=700000,ctp='current')
    Sbi_manager.add_customer(cust3)

    # Sbi_manager.add_customer('dattu')

    result = Sbi_manager.get_list_of_customer()
    print('Customer Added Succefully...!',result)


    # Sbi_manager.deposit(101,ammount=500)
    # Sbi_manager.withdraw(102,700000)
    
    # Sbi_manager.delete_customer(102)

    # Sbi_manager.search_by_account_type(acctype="saving")

    # Sbi_manager.get_balance_of_customer(custname="Shubham Gharde")

    # Sbi_manager.update_customer(103, name="pratik", acc_type="Savings", balance=5000)

    # try:
    #     cust1 = Customer(cid=101,cnm='shubham Gharde',cbal=500000,ctp='current')
    #     Sbi_manager.add_customer(cust1)

    # except DuplicateCustomer as d:
    #     print(d.error_message)

    # Sbi_manager.add_customer('Gaurav Bhongade')

    
    