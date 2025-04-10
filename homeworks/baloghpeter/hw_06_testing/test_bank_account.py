import pytest
from bank_account import BankAccount  

@pytest.fixture
def account1():
    return BankAccount(owner="Alice", balance=100.0)

@pytest.fixture
def account2():
    return BankAccount(owner="Bob", balance=50.0)

@pytest.mark.parametrize("amount", [0, -10, -0.01])
def test_deposit_invalid_amount_raises(account1, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account1.deposit(amount)

def test_withdraw_valid(account1):
    account1.withdraw(30)
    assert account1.get_balance() == 70.0

def test_withdraw_more_than_balance_raises(account1):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account1.withdraw(150)

def test_withdraw_negative_amount_raises(account1):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account1.withdraw(-5)

def test_transfer_valid(account1, account2):
    account1.transfer(40, account2)
    assert account1.get_balance() == 60.0
    assert account2.get_balance() == 90.0

def test_transfer_to_invalid_target_raises(account1):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account1.transfer(10, "NotABankAccount")

def test_transfer_insufficient_funds_raises(account1, account2):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account1.transfer(999, account2)

def test_initial_negative_balance_raises():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Charlie", -100)

def test_str_method(account1):
    assert str(account1) == "Account owner: Alice, Balance: 100.00"