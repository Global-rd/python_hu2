
import pytest
from bank_account import BankAccount

@pytest.fixture
def bank_account_jane():
    #Fixture for creating a bank account instance for Jane.
    return BankAccount("Jane", 20000)

@pytest.fixture
def bank_account_john():
    #Fixture for creating a bank account instance for John.
    return BankAccount("John", 300)

def test_deposit(bank_account_jane):
    bank_account_jane.deposit(450)
    assert bank_account_jane.get_balance() == 20450

def test_withdraw(bank_account_john):
    bank_account_john.withdraw(100)
    assert bank_account_john.get_balance() == 200

@pytest.mark.parametrize("amount, expected_exeption", [
    (-100, ValueError),
    (0, ValueError),
    ])
def test_invalid_deposit(bank_account_jane, amount, expected_exeption):
    with pytest.raises(expected_exeption):
        bank_account_jane.deposit(amount) 


def test_transfer(bank_account_john):
    with pytest.raises(TypeError):
        bank_account_john.transfer(50, "non_existent_account")

def test_withdraw_invalid(bank_account_jane):
    with pytest.raises(ValueError):
        bank_account_jane.withdraw(100000)




