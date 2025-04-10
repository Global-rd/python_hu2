from bank_account import BankAccount
import pytest

@pytest.fixture
def account_01():
    return BankAccount(owner="Margit", balance=1500)

@pytest.fixture
def account_02():
    return BankAccount(owner="Dávid", balance=225)

def test_invalid_account_creation():
    with pytest.raises(ValueError):
        BankAccount(owner="Sanyi", balance=-200)

@pytest.mark.parametrize("amount", [-225, -75, 0])
def test_deposit_invalid_amount(account_01, amount):
    with pytest.raises(ValueError):
        account_01.deposit(amount)

def test_account_01_deposit(account_01):
    account_01.deposit(500)
    assert account_01.get_balance() == 2000

def test_account_02_withdraw(account_02):
    account_02.withdraw(25)
    assert account_02.get_balance() == 200

def test_account_02_invalid_withdraw(account_02):
    with pytest.raises(ValueError):
        account_02.withdraw(226)

def test_transfer(account_01, account_02):
    account_01.transfer(500, account_02)
    assert account_01.get_balance() == 1000
    assert account_02.get_balance() == 725

def test_invalid_account_transfer(account_01):
    with pytest.raises(TypeError):
        account_01.transfer("invalid name", 2000)