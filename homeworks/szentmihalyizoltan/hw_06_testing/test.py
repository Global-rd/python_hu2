import pytest
from bank_account import BankAccount

@pytest.fixture
def account_1():    
    return BankAccount(owner = "Jimmy Jimmerson", balance = 300.0)

@pytest.fixture
def account_2():
    return BankAccount(owner = "Jack Jackerson", balance = 500.0)

@pytest.mark.parametrize("deposit_money", [20, 0, -40])
def test_deposit(account_1, deposit_money):
    if deposit_money <= 0:
        with pytest.raises(ValueError, match="Deposit amount must be positive."):
            account_1.deposit(deposit_money)
    else:
        starting_balance = account_1.get_balance()
        account_1.deposit(deposit_money)
        assert account_1.get_balance() == starting_balance + deposit_money

def test_transfer_invalid_target(account_1):
    with pytest.raises(TypeError, match="It is not a bank account"):
        account_1.transfer(200, "Not a bank account") 

def test_str(account_1):
    assert str(account_1) == "This account belongs to: Jimmy Jimmerson, Balance: 300.0"