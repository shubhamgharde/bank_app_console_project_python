class Customer:
    def __init__(self,cid,cnm,cbal,ctp):
        self.customer_id = cid
        self.customer_name = cnm
        self.customer_balance = cbal
        self.customer_aacount_type = ctp
        # self.customer_deposit_amount = depoamt
        # self.customer_withdraw_amount = withamt

    def __str__(self):
        return f'''\n {self.__dict__}'''
    
    def __repr__(self):
        return str(self)
    
