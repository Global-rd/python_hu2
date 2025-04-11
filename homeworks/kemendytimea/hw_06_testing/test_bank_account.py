import pytest
from bank_account import BankAccount

@pytest.fixture
def account_momi():
    return BankAccount(owner="Momi", balance=100.0)

@pytest.fixture
def account_lili():
    return BankAccount(owner="Lili", balance=50.0)

@pytest.mark.parametrize("amount", [0, -10, -0.01])
def test_deposit_invalid_amount(account_momi, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account_momi.deposit(amount)

def test_deposit_valid(account_momi):
    account_momi.deposit(25.0)
    assert account_momi.get_balance() == 125.0

@pytest.mark.parametrize("amount", [0, -20])
def test_withdraw_invalid_amount(account_lili, amount):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_lili.withdraw(amount)

def test_withdraw_insufficient_funds(account_lili):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_lili.withdraw(100.0)

def test_withdraw_valid(account_lili):
    account_lili.withdraw(20.0)
    assert account_lili.get_balance() == 30.0

def test_transfer_to_invalid_target(account_momi):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_momi.transfer(20, "not_account")

def test_transfer_insufficient_funds(account_momi, account_lili):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_lili.transfer(100, account_momi)

def test_transfer_valid(account_momi, account_lili):
    account_momi.transfer(40.0, account_lili)
    assert account_momi.get_balance() == 60.0
    assert account_lili.get_balance() == 90.0

def test_initial_negative_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Pomi", -5.0)

def test_str_method(account_momi):
    assert str(account_momi) == "Account owner: Momi, Balance: 100.00"