
class BankAccount:

    total_money = 0   # class variable to keep track of all money in all accounts

    def __init__(self, account_type, starting_balance=0):
        print('Creating a new account of type', account_type, 'with a balance of', starting_balance)

        self.account_type = account_type
        self.balance = starting_balance
        self.overdraft_fees = 0  # Initialise this to 0 here, even though it's not an argument
        BankAccount.total_money += starting_balance

    def deposit(self, amount):
        self.balance += amount
        BankAccount.total_money += amount
        print('New balance for this account is: $', self.balance, sep='')

    def withdraw(self, amount):
        self.balance -= amount
        BankAccount.total_money -= amount
        if self.balance < 0:
            self.overdraft_fees += 20
            print('Warning! Overdraft fee added. Total fees: $', self.overdraft_fees, sep='')
        print('New balance for this account is: $', self.balance, sep='')

fido = BankAccount('savings', 1000)
ruby = BankAccount('checking')
