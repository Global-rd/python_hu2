import pytest
from bank_account import BankAccount

@pytest.fixture
def account_1():
    return BankAccount("Thomas" , 100)

@pytest.fixture
def account_2():
    return BankAccount("Dexter")

def test_basic_inputs(account_1,account_2):
    account_1.withdraw(50)
    account_1.deposit(25)
    assert account_1.get_balance() == 75
    account_1.transfer(25,account_2)
    assert account_2.get_balance() == 25
    assert account_1.get_balance() == 50


def test_invalid_basic_inputs(account_1,account_2):
    with pytest.raises(ValueError):
        account_1.withdraw(200)
        account_2.withdraw(-200)
        account_2.deposit(-200)
        account_2.deposit(0)
        account_1.transfer(-50,account_2)
    with pytest.raises(TypeError):
        account_1.transfer(50, "nobody")


def test_incorrect_input_types(account_1,account_2):
    with pytest.raises(TypeError):
        account_1.withdraw("a")
        account_2.deposit([1])


@pytest.mark.parametrize("account_name, balance, expected_error", [
    ("person1", -10, ValueError),
    ("person2", -10000, ValueError)
])
def test_invalid_account_creation(account_name, balance, expected_error):
    with pytest.raises(expected_error):
        BankAccount(account_name, balance)





# pytest homeworks/varsanyidaniel/hw_06_testing