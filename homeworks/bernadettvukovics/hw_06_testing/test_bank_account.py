import pytest
from bank_account import BankAccount  # import the BankAccount class

class BankAccount:
    def __init__(self, balance=0):
        if not isinstance(balance, (int, float)):
            raise ValueError("Initial balance must be a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("The recipient must be a BankAccount object.")
        if other_account == self:
            raise ValueError("Cannot transfer money to the same account.")
        if not isinstance(amount, (int, float)):
            raise ValueError("Transfer amount must be a number.")
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer.")
        self.balance -= amount
        other_account.deposit(amount)
        
# Fixture 1: A BankAccount object with an initial balance of 100
@pytest.fixture
def account_with_balance():
    return BankAccount(100)

# Fixture 2: A BankAccount object with an initial balance of 0
@pytest.fixture
def account_with_zero_balance():
    return BankAccount(0)

# Test deposit method with valid inputs
def test_deposit(account_with_balance):
    account_with_balance.deposit(50)
    assert account_with_balance.balance == 150

# Test deposit method with 0 value
@pytest.mark.parametrize("deposit_amount", [0, -10])
def test_deposit_invalid_amount(account_with_balance, deposit_amount):
    with pytest.raises(ValueError):  # Assuming we raise ValueError for invalid deposit
        account_with_balance.deposit(deposit_amount)

# Test withdraw method with valid inputs
def test_withdraw(account_with_balance):
    account_with_balance.withdraw(30)
    assert account_with_balance.balance == 70

# Test withdraw method with insufficient funds
def test_withdraw_insufficient_funds(account_with_balance):
    with pytest.raises(ValueError):  # Assuming ValueError is raised on insufficient funds
        account_with_balance.withdraw(200)

# Test transfer method with valid inputs
def test_transfer(account_with_balance, account_with_zero_balance):
    account_with_balance.transfer(account_with_zero_balance, 50)
    assert account_with_balance.balance == 50
    assert account_with_zero_balance.balance == 50

# Test transfer method to non-BankAccount object
def test_transfer_invalid_account(account_with_balance):
    with pytest.raises(TypeError):  # Assuming TypeError is raised for non-BankAccount objects
        account_with_balance.transfer("Not a BankAccount", 50)

# Test invalid BankAccount object creation (e.g., negative initial balance)
def test_invalid_bank_account_creation():
    with pytest.raises(ValueError):  # Assuming ValueError is raised for invalid initial balance
        BankAccount(-100)