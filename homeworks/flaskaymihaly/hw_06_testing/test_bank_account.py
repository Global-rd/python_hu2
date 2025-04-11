import pytest
from bank_account import BankAccount


@pytest.fixture
def account_one():
    return BankAccount("owner_1", 100)

@pytest.fixture 
def account_two():
    return BankAccount("owner_2", 50)
    
@pytest.mark.parametrize("amount", [-10,0 ])
def test_invalid_deposit(account_one, amount):
    with pytest.raises(ValueError, match = "Deposit amount must be positive."):
        account_one.deposit(amount)

def test_unknown_target(account_two):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_two.transfer(10, "unknown")

def test_transfer_successful(account_one, account_two):
    account_one.transfer(10, account_two )

    assert account_one.get_balance() == 90
    assert account_two.get_balance() == 60



