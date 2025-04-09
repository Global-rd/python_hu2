import pytest
from bank_account import BankAccount

@pytest.fixture
def account_peter():
    return BankAccount("Péter", 100.0)

@pytest.fixture
def account_anna():
    return BankAccount("Anna", 200.0)

@pytest.mark.parametrize("amount", [0, -10, -0.01])
def test_deposit_error(account_peter, amount):
    with pytest.raises(ValueError):
        account_peter.deposit(amount)

def test_deposit_success(account_peter):
    account_peter.deposit(50)
    assert account_peter.get_balance() == 150.0

@pytest.mark.parametrize("amount", [0, -5])
def test_withdraw_error(account_peter, amount):
    with pytest.raises(ValueError):
        account_peter.withdraw(amount)

def test_withdraw_insufficent_funds(account_peter):
    with pytest.raises(ValueError):
        account_peter.withdraw(200)

def test_withdraw_success(account_anna):
    account_anna.withdraw(50)
    assert account_anna.get_balance() == 150.0

def test_transfer_success(account_peter, account_anna):
    account_peter.transfer(50, account_anna)
    assert account_peter.get_balance() == 50.0
    assert account_anna.get_balance() == 250.0

@pytest.mark.parametrize("target", [None, "type", 42, 3.14, object()])
def test_transfer_error(account_peter, target):
    with pytest.raises(TypeError):
        account_peter.transfer(10, target)

def test_transfer_insufficent_funds(account_peter, account_anna):
    with pytest.raises(ValueError):
        account_peter.transfer(1000, account_anna)

def test_negative_opening_balance():
    with pytest.raises(ValueError):
        BankAccount("Péter ", -100.0)

def test_account_str(account_peter):
    assert str(account_peter)