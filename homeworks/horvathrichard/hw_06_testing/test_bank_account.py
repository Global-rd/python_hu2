import pytest
from bank_account import BankAccount

#------két fixture létrehozása a "fiktív" accountokra------

@pytest.fixture
def empty_account():
    return BankAccount("User1")

@pytest.fixture
def registered_account_with_amount():
    return BankAccount("Test User", balance=1000)

#----------------------------------------------------------
