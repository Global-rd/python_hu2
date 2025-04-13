class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        if not account_number or not account_number.strip():
            raise ValueError("Account number cannot be empty.")
        
        if not account_number.isdigit():
            raise ValueError("Account number must contain only digits.")
    
        if len(account_number) != 24:
            raise ValueError("Account number must be exactly 24 digits long.")
        
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        
        if len(owner) > 150:
            raise ValueError("Account owner name cannot be longer than 150 characters.")
        
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")

        if self == target_account:
            raise ValueError("Cannot transfer to the same account.")            
        
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
    
    def __repr__(self):
        return (f"BankAccount(account_number='{self.account_number}', "
                f"owner='{self.owner}', balance={self.balance})")
    
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.account_number == other.account_number
        return False
    
class Person:
    def __init__(self, name: str, address: str, phone: str, email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}" 
