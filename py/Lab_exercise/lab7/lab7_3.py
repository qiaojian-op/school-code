class BankAccount:
    def __init__(self,__accountNumber,__accountHolder,__balance):
        self.__accountNumber=__accountNumber
        self.__accountHolder=__accountHolder
        self.__balance=__balance

    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposit successful: RM{amount}")

    def withdraw(self,amount):
        self.__balance-=amount
        print(f"Withdraw successful: RM{amount}")

    def displayAccount(self):
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Holder: {self.__accountHolder}")
        print(f"Balance: RM{self.__balance}")

def main():
    account1=BankAccount(1001,"Ahmed",1000)
    account1.deposit(500)
    account1.withdraw(300)
    account1.displayAccount()

main()
    
