from bank_account import BankAccount
import pytest

@pytest.fixture
def account_01():
    return BankAccount(owner="Margit", balance=1500)

@pytest.fixture
def account_02():
    return BankAccount(owner="Dávid", balance=225)

def invalid_account_creation_test():
    with pytest.raises(ValueError):
        BankAccount(owner="Sanyi", balance=-200)

@pytest.mark.parametrize("amount", [-225, -75, 0])
def deposit_invalid_amount_test(account_01, amount):
    with pytest.raises(ValueError):
        account_01.deposit(amount)

def account_01_deposit_test(account_01):
    account_01.deposit(500)
    assert account_01.get_balance() == 2000

def account_02_withdraw_test(account_02):
    account_02.withdraw(25)
    assert account_02.get_balance() == 200

def account_02_invalid_withdraw_test(account_02):
    with pytest.raises(ValueError):
        account_02.withdraw(226)

def transfer_test(account_01, account_02):
    account_01.transfer(account_02, 500)
    assert account_01.get_balance() == 1000
    assert account_02.get_balance() == 725

def invalid_account_transfer_test(valid_account):
    with pytest.raises(TypeError):
        valid_account.transfer("invalid name", 2000)