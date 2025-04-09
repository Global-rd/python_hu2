import pytest
from bank_account import BankAccount

@pytest.fixture
def account_1():
    return BankAccount("Thomas",100)

@pytest.fixture
def account_2():
    return BankAccount("Dexter")

def test_basic_inputs(account_1):
    account_1.withdraw(50.0)
    assert account_1.items["balance"] == 50


@pytest.mark.parametrize("account_name, balance, expected_error", [
    ("person1", -10, ValueError),
    ("person2", -10000, ValueError)
])
def test_invalid_account_creation(account_name, balance, expected_error):
    with pytest.raises(expected_error):
        BankAccount(account_name, balance)






# pytest homeworks/varsanyidaniel/hw_06_testing