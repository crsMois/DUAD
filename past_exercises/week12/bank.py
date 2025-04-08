from abc import ABC, abstractmethod
class BankAccount(ABC):

    balance = 0

    def deposit_to_account(self,money):
        self.balance= self.balance+money


    @abstractmethod
    def withdraw_from_account(self,money):
        self.balance= self.balance-money



class SavingsAccount(BankAccount):
    
    min_balance=0

    def __init__(self,min_balance):
        self.min_balance=min_balance

    def withdraw_from_account(self, money):
        if (self.min_balance>(self.balance-money)):
            print(f"\n\n\nYou have insufficient funds to withdraw, the current minimal fund is {self.min_balance}!!!! ")
        else:
            self.balance=self.balance-money 


def main():
    account1= SavingsAccount(1000)
    account1.deposit_to_account(11000)
    account1.withdraw_from_account(9000)
    account1.withdraw_from_account(2000)

    print(f"Current Balance: {account1.balance}")
main()