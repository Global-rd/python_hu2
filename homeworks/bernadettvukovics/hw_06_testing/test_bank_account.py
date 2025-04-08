import pytest
from bank_account import BankAccount  # import the BankAccount class


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