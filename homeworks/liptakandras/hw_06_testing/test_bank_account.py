import pytest

from bank_account import BankAccount


# FIXTURE-ÖK:

# Üres bankszámla

@pytest.fixture
def empty_account():
    return BankAccount("Andras")

# Bankszámla egy bizonyos összeggel

@pytest.fixture
def account_with_balance():
    return BankAccount("Bob", 8000.0)


# UNIT TESZTEK

# Bankszámla létrehozása

def test_account_creation(empty_account):
    
    assert empty_account.owner == "Andras"
    assert empty_account.balance == 0.0

# Bob bankszámlája

def test_account_creation_with_initial_balance(account_with_balance):

    assert account_with_balance.owner == "Bob"
    assert account_with_balance.balance == 8000.0

# Pozitív deposit

def test_positive_deposit_amount(account_with_balance):

    account_with_balance.deposit(50.0)
    assert account_with_balance.balance == 8050.0

# Deposit method 0 és negatív számmal

@pytest.mark.parametrize("invalid_amount", [0.0, -500.0, -1000.0])  # ez csak lista

def test_deposit_invalid_amounts_raises_error(empty_account, invalid_amount):
    with pytest.raises(ValueError):
        empty_account.deposit(invalid_amount)

# Pénz küldése nem bank account objectnek

def test_transfer_to_invalid_account_object(account_with_balance):
    invalid_target = "not_bank_account"  
    transfer_amount = 2000.0     
    with pytest.raises(TypeError):
        account_with_balance.transfer(transfer_amount, invalid_target)

# Exception-ök

def test_account_with_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Negative", -50.0)

def test_transfer_insufficient_funds_error(account_with_balance, empty_account):
    transfer_amount = account_with_balance.balance + 1000.0  # de ez lehetne + bármi más szám is
    with pytest.raises(ValueError):
        account_with_balance.transfer(transfer_amount, empty_account)

def test_withdraw_insufficient_funds_error(account_with_balance):
    withdraw_amount = 8100  # szintén, de most konkrét összeggel, mivel az account_with_balance értéke adott
    with pytest.raises(ValueError):
        account_with_balance.withdraw(withdraw_amount)