"""
Értelmezd a kódot a bank_account.py fileban, és írj unit test-eket pytest segítségével.
A unit testeknél a következőket vedd figyelembe:
● Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
● Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak érdekében, hogy a tesztet több input-ra is lefuttassa (pl: teszteld a deposit() method-ot pontosan 0 és negatív szám inputtal is).
● Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-nek).
● Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-elődik- e a megadott input-ra.
"""

import pytest
from bank_account import BankAccount

# --- Fixtures ---
@pytest.fixture
def account_john():
    return BankAccount(owner="John", balance=200.0)

@pytest.fixture
def account_emily():
    return BankAccount(owner="Emily", balance=75.0)

# --- Teszt: Kezdeti egyenleg helyes beállítása ---
def test_starting_balance(account_john):
    assert account_john.get_balance() == 200.0

# --- Teszt: deposit() többféle bemenettel ---
@pytest.mark.parametrize("amount, expected_result", [
    (100.0, 300.0),   # normál befizetés
    (0.0, None),      # nulla összeg – hibát várunk
    (-25.0, None)     # negatív összeg – hibát várunk
])
def test_deposit_behavior(account_john, amount, expected_result):
    if amount <= 0:
        with pytest.raises(ValueError, match="Deposit amount must be positive."):
            account_john.deposit(amount)
    else:
        account_john.deposit(amount)
        assert account_john.get_balance() == expected_result

# --- Teszt: pénzfelvétel ---
def test_withdrawal_scenarios(account_emily):
    account_emily.withdraw(25.0)
    assert account_emily.get_balance() == 50.0

    with pytest.raises(ValueError, match="Insufficient funds."):
        account_emily.withdraw(100.0)

    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_emily.withdraw(-5.0)

# --- Teszt: átutalás ---
def test_transfer_money(account_john, account_emily):
    account_john.transfer(50.0, account_emily)
    assert account_john.get_balance() == 150.0
    assert account_emily.get_balance() == 125.0

    with pytest.raises(ValueError, match="Insufficient funds."):
        account_john.transfer(999.0, account_emily)

    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_john.transfer(10.0, "InvalidAccount")

# --- Teszt: negatív kezdő egyenleg ---
def test_invalid_starting_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("ErrorUser", balance=-100.0)

# --- Teszt: __str__ metódus működése ---
def test_string_output(account_emily):
    assert str(account_emily) == "Account owner: Emily, Balance: 75.00"
    