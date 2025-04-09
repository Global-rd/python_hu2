import pytest
from extra import BankAccount

@pytest.fixture
def account_1():    
    return BankAccount(owner = "Jimmy Jimmerson", amount = 3000.0)

@pytest.fixture
def account_2():
    return BankAccount(owner = "Jack Jackerson", amount = 5000.0)

@pytest.mark.parametrize("balance, withdraw, expected_exception", [
    (300, 500, ValueError), #negative balance
    (0, 500, ValueError), #zero balance
    (-500, 300, ValueError), #attempt from negative balance    
])

def test_withdraw(account_1, withdraw, balance, expected_exception):
    if expected_exception:
        with pytest.raises(ValueError, match="Withdraw amount must be positive." if withdraw <= 0 else "Insufficient funds."):
            account_1.withdraw(withdraw)
    else:
        account_1.withdraw(withdraw)
        assert account_1.get_balance() == balance

def test_transfer_invalid_target(account_1):
    with pytest.raises(TypeError, match="It is not a bank avvount"):
        account_1.transfer(200, "Not a bank account") 
