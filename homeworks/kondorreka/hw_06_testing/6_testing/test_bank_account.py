import pytest
from bank_account import BankAccount

"""
● Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
"""

#Test számla létrehozása deposit nélkül
@pytest.fixture
def empty_account():
    return BankAccount(owner = "test_owner_1")

#Test számla létrehozása és deposit ráhelyezése
@pytest.fixture 
def account_with_money():
    account = BankAccount(owner = "test_owner_2")
    account.deposit(100)
    return account


"""
● Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak
érdekében, hogy a tesztet több input-ra is lefuttassa (pl: teszteld a
deposit() method-ot pontosan 0 és negatív szám inputtal is).
"""

#Üres számla tesztelése
def test_empty_deposit(empty_account):

    empty_account.deposit(10)
    assert empty_account.get_balance() == 10 

@pytest.mark.parametrize("amount", [
    -100, #negatív deposit
    0 #zero deposit
    ])
def test_empty_deposit_invalid_input(empty_account, amount):
    with pytest.raises(ValueError, match = "Deposit amount must be positive."):
        empty_account.deposit(amount)

#Nem üres számla tesztelése
def test_nonempty_deposit(account_with_money):

    account_with_money.deposit(10)
    assert account_with_money.get_balance() == 110 

#nem tudom, hogy ezt kell-e, nem függ a kezdő egyenlegtől
# @pytest.mark.parametrize("amount", [
#     -100, #negatív deposit
#     0 #zero deposit
#     ])
# def test_nonempty_deposit_invalid_input(account_with_money, amount):
#     with pytest.raises(ValueError, match = "Deposit amount must be positive."):
#         account_with_money.deposit(amount)

"""
● Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-
nek).
● Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-
elődik- e a megadott input-ra.
"""
def test_transfer_successful(account_with_money, empty_account):
    account_with_money.transfer(80, empty_account)

    assert account_with_money.get_balance() == 20
    assert empty_account.get_balance() == 80

#nem BankAccount object
def test_transfer_invalid_target(account_with_money):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_with_money.transfer(10, "valami")

#Utalandó összeg érvényességének tesztelése
@pytest.mark.parametrize("amount, expected_exception", [
    (-100, ValueError), #negative transfer
    ( 0, ValueError), #zero transfer
    ])
def test_transfer_invalid_input(account_with_money, empty_account, amount, expected_exception):
    with pytest.raises(expected_exception, match = "Withdraw amount must be positive."):
        account_with_money.transfer(amount, empty_account)

#Fedezet ellenőrzés
@pytest.mark.parametrize("amount, expected_exception", [
    (1000, ValueError), #nincs fedezet
    (100.01, ValueError), #nincs fedezet
    ])
def test_transfer_funds_control(account_with_money, empty_account, amount, expected_exception):
    with pytest.raises(expected_exception, match="Insufficient funds."):
        account_with_money.transfer(amount, empty_account)

