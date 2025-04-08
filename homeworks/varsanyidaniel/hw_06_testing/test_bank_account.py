import pytest
from bank_account import BankAccount

@pytest.fixture
def account_1():
    account_1 = BankAccount("Thomas",100)

@pytest.fixture
def account_2():
    account_1 = BankAccount("Dexter")


@pytest.mark.parametrize("account_name, balance, expected_error", [
    ("person1", -10, ValueError),
    ("person2", -10000, ValueError)
])
def test_invalid_account_creation(account_name, balance, expected_error):
    with pytest.raises(expected_error):
        BankAccount(account_name, balance)


def test_basic_inputs(account_1):
    account_1.withdraw(50)
    assert account_1.items["balance"] == 50





# pytest homeworks/varsanyidaniel/hw_06_testing