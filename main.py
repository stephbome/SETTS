class Account:
    def _init_(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Invalid withdrawal amount."

    def get_balance(self):
        return self.balance
class CurrentAccount(Account):
    def _init_(self, account_number, balance=0):
        super()._init_(account_number, balance)
        # No specific restrictions for Current Account
# Create an instance of CurrentAccount
current_account = CurrentAccount("CA12345", 10000)

print(current_account.deposit(5000))
print("Current Account Balance:", current_account.get_balance())


print(current_account.withdraw(3000))
print("Current Account Balance:", current_account.get_balance())


print(current_account.withdraw(20000))
print("Current Account Balance:", current_account.get_balance())