import pytest
from bank_account import BankAccount


@pytest.fixture
def empty_account(): # zero balance
    return BankAccount("Johnny Bravo", 0.0)

@pytest.fixture
def initial_account(): # initial balance 100
    return BankAccount("Peter Parker", 100.0)

def test_account_creation(empty_account): # testing creation with 0 balance
    assert empty_account.owner == "Johnny Bravo"
    assert empty_account.balance == 0.0

def test_account_creation_with_initial_balance(initial_account): # testing creation with 100 balance
    assert initial_account.owner == "Peter Parker"
    assert initial_account.balance == 100.0

def test_negative_initial_balance(): # testing ValueError at negative initial balance
    with pytest.raises(ValueError) as exc_info:
        BankAccount("Invalid", -50.0)
    assert "Initial balance cannot be negative." in str(exc_info.value)

@pytest.mark.parametrize("amount, expected_balance, should_raise", [
    (50.0, 50.0, False),
    (0.0, 0.0, True),
    (-10.0, 0.0, True),
    (100.0, 100.0, False)
])

def test_deposit(empty_account, amount, expected_balance, should_raise): # testing deposit
    if should_raise:
        with pytest.raises(ValueError) as exc_info:
            empty_account.deposit(amount)
        assert "Deposit amount must be positive." in str(exc_info.value)
    else:
        empty_account.deposit(amount)
        assert empty_account.get_balance() == expected_balance

def test_withdraw(initial_account): # testing withdrawal with sufficient funds
    initial_account.withdraw(30.0)
    assert initial_account.get_balance() == 70.0

def test_withdraw_insufficient_funds(initial_account): # testing withdrawal with insufficient funds
    with pytest.raises(ValueError) as exc_info:
        initial_account.withdraw(150.0)
    assert "Insufficient funds." in str(exc_info.value)
    assert initial_account.get_balance() == 100.0  # balance should remain unchanged

@pytest.mark.parametrize("amount", [0.0, -5.0]) # testing withdrawal with negative amount 
def test_withdraw_non_positive_amount(initial_account, amount):
    with pytest.raises(ValueError) as exc_info:
        initial_account.withdraw(amount)
    assert "Withdraw amount must be positive." in str(exc_info.value)

def test_transfer_successful(initial_account, empty_account): # transfer between 2 accounts
    initial_account.transfer(50.0, empty_account)
    assert initial_account.get_balance() == 50.0
    assert empty_account.get_balance() == 50.0

def test_transfer_insufficient_funds(initial_account, empty_account): # transferring insufficient funds must raise ValueError
    with pytest.raises(ValueError) as exc_info:
        initial_account.transfer(150.0, empty_account)
    assert "Insufficient funds." in str(exc_info.value)
    assert initial_account.get_balance() == 100.0
    assert empty_account.get_balance() == 0.0  # Target account balance unchanged

def test_transfer_to_non_bank_account(initial_account): # testing transfer to a non-bank account
    with pytest.raises(TypeError) as exc_info:
        initial_account.transfer(20.0, "not_an_account")
    assert "Target must be a BankAccount instance." in str(exc_info.value)

def test_get_balance(initial_account): # testing get balance
    assert initial_account.get_balance() == 100.0
