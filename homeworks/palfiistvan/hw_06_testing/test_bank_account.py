import pytest
from bank_account import BankAccount

# Fixtures:
@pytest.fixture
def bank_account1():
    return BankAccount(owner="Alice", balance=100.0)

@pytest.fixture
def bank_account2():
    return BankAccount(owner="Bob", balance=50.0)

# Testing that the opening balance is set correctly
def test_initial_balance(bank_account1):
    assert bank_account1.get_balance() == 100.0

# Testing for deposit() method work
@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (50.0, 150.0),  # positive amount
    (-10.0, 100.0), # negative amount, which should throw ValueError
    (0.0, 100.0)    # zero amount
])

def test_deposit(bank_account1, deposit_amount, expected_balance):
    if deposit_amount <= 0:
        with pytest.raises(ValueError, match="Deposit amount must be positive."):
            bank_account1.deposit(deposit_amount)
    else:
        bank_account1.deposit(deposit_amount)
        assert bank_account1.get_balance() == expected_balance

# Testing for withdraw() method work
def test_withdraw(bank_account1):
    bank_account1.withdraw(50.0)
    assert bank_account1.get_balance() == 50.0

    with pytest.raises(ValueError, match="Insufficient funds."):
        bank_account1.withdraw(100.0)

    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        bank_account1.withdraw(-10.0)

# Testing for transfer() method work
def test_transfer(bank_account1, bank_account2):
    bank_account1.transfer(30.0, bank_account2)
    assert bank_account1.get_balance() == 70.0
    assert bank_account2.get_balance() == 80.0

    with pytest.raises(ValueError, match="Insufficient funds."):
        bank_account1.transfer(100.0, bank_account2)

    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        bank_account1.transfer(50.0, "Not a BankAccount")

# Testing that exceptions are passed correctly
def test_invalid_initial_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount(owner="Charlie", balance=-10.0)

# Testing that string representation is correct
def test_str(bank_account1):
    assert str(bank_account1) == "Account owner: Alice, Balance: 100.00"