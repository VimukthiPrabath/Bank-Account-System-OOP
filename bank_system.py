import random

class BankAccount:
    
    def __init__(self,owner_name,initial_balance):
        self.owner = owner_name
        self.__balance = initial_balance
        
        self.accountNumber = random.randint(10000,99999)
        self.history = []
        
        self.history.append(f"{self.owner}account created with initia balance:  Rs: {initial_balance}")
        
        
    def deposite (self,amount):
        self.__balance = self.__balance + amount
        
        self.history.append(f"Deposite amount Rs:{amount}")
        print(f"{self.owner} Rs : {amount} k thenpath kara. Den balace eka:{self.__balance}")
        
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            
            self.history.append(f"Withdraw Rs:{amount}")
            print(f"{self.owner} Acconut eken Rs:{amount} withdraw kara. den thiayana balance eka Rs:{self.__balance}")
        else:
            print(f"{self.owner}account eke salli pramanawath ne ")
            self.history.append(f" {self.owner} Faild withdrawel attempt Rs:{amount}")
            
    def check_balance(self):
        print(f" {self.owner} account eke balance ek Rs:{self.__balance}")
        
        
        
    def show_history(self):
        print(f"transaction History | {self.owner} |")
        for record in self.history:
            print("-" , record)
            
        print("---------------------------\n")
        
    def transfer(self,target_account,amount):
        if self.__balance > amount:
            self.withdraw(amount)
            target_account.deposite(amount)
            self.history.append(f"Transferred Rs:{amount} to {target_account.owner}")
        else:
            print(f"salli madi yawanna")
    
    
    

my_account = BankAccount("Vimukthi", 5000)
frend_account = BankAccount("Sade", 1000)

my_account.check_balance()
frend_account.check_balance()

print("\n--- Transactions ---")
my_account.deposite(5000) 
my_account.withdraw(6000) 
my_account.check_balance()

print("\n--- Transfer Money ---")
my_account.transfer(frend_account, 3000)

my_account.show_history()
frend_account.show_history()
        