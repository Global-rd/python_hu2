import pytest
from bank_account import BankAccount


@pytest.fixture
def empty_account():
    """
    Fixture that creates an empty bank account.
    """
    return BankAccount(owner="Test Owner")


@pytest.fixture
def account_with_balance():
    """
    Fixture that creates a bank account with an initial balance.
    """
    return BankAccount(owner="Rich Dude", balance=100000.0)


def test_initial_balance(empty_account, account_with_balance):
    """
    Test that accounts are initialized with the correct balance.
    """
    assert empty_account.get_balance() == 0.0
    assert account_with_balance.get_balance() == 100000.0


# Test the withdraw() method
def test_withdraw(account_with_balance):  # using the fixture, starting with 100k
    """
    Test that withdrawing money will decrease the balance correctly.
    """
    account_with_balance.withdraw(30000.0)
    assert (
        account_with_balance.get_balance() == 70000.0
    )  # after withdrawing 30k we should have 70k left

    # Withdraw additional money and check balance again
    account_with_balance.withdraw(25000)
    assert (
        account_with_balance.get_balance() == 45000.0
    )  # so we've proven that the withdraw method correctly reduces the account balance


# Edge case: withdrawing more money (100001) than the balance (100000)
def test_withdraw_insufficient_balance(account_with_balance):
    """
    Test that withdrawing more money than the balance raises an error.
    """
    with pytest.raises(ValueError):
        account_with_balance.withdraw(100001.0)


# Parameterized test to check multiple invalid inputs: 0 or lower numbers
@pytest.mark.parametrize("amount", [0.0, -200.0])
def test_withdraw_invalid_amount(account_with_balance, amount):
    """
    Test that withdrawing invalid amounts (0 or less) should throw an error.
    """
    with pytest.raises(ValueError):
        account_with_balance.withdraw(amount)


# test the transfer functionality
def test_transfer(empty_account, account_with_balance):
    """
    Test whether sending money from one account to the other works correctly
    """
    # Let's transfer 30k from account_with_balance to an empty_account
    account_with_balance.transfer(30000.0, empty_account)

    # Check that both balances are updates correctly
    assert account_with_balance.get_balance() == 70000.0
    assert empty_account.get_balance() == 30000.0


def test_transfer_insufficient_balance(empty_account, account_with_balance):
    """
    Test that transferring more than the balance raises an error.
    """
    with pytest.raises(ValueError):
        empty_account.transfer(
            1.0, account_with_balance
        )  # empty_account has a balance of 0.0


@pytest.mark.parametrize("amount", [0.0, -100.0])
def test_transfer_invalid_amount(account_with_balance, empty_account, amount):
    """
    Test that transfering zero or negative amounts raises an Error.
    """
    with pytest.raises(ValueError):
        account_with_balance.transfer(amount, empty_account)


def test_transfer_invalid_target(account_with_balance):
    """
    Test that transferring to a non-BankAccount object raises an Error.
    """
    with pytest.raises(TypeError):
        account_with_balance.transfer(1000.0, "not an account")


# Test that initializing the account with wrong input raises an error
def test_init_with_non_numeric_balance():
    """
    Test that initializingg an account with a not-useable balance input raises an error.
    """
    with pytest.raises(TypeError):
        BankAccount(owner="Type Error Tim", balance="not a number")


### Extra Task, let's validate the extended BankAccount class ###
def test_init_with_non_string_owner():
    """
    Test that initializing an account with a non-string owner raises an error.
    """
    with pytest.raises(TypeError):
        BankAccount(owner=123, balance=1000.0)


def test_init_with_empty_owner():
    """
    Test that initializing an account with a null owner raises an error.
    """
    with pytest.raises(ValueError):
        BankAccount(owner="", balance=1000.0)

    with pytest.raises(ValueError):
        BankAccount(owner="   ", balance=10012.0)  # Only whitespace


def test_deposit_non_numeric():
    """
    Test that depositing a non-numeric amount raises an error.
    """
    account = BankAccount(owner="Test Owner")
    with pytest.raises(TypeError):
        account.deposit("százat")  # String instead of number


def test_transfer_to_self():
    """
    Test that transferring money to the same account raises an error.
    """
    account = BankAccount(owner="Test Owner", balance=10000.0)
    with pytest.raises(ValueError):
        account.transfer(50.0, account)  # Trying to send money to self


def test_withdraw_non_numeric():
    """
    Test that withdrawing a non-numeric amount raises an error.
    """
    account = BankAccount(owner="Test Owner", balance=100.0)
    with pytest.raises(TypeError):
        account.withdraw("adjá 50-et")  # String instead of number
