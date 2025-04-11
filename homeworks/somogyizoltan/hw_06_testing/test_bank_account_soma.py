"""
Másold ezt a file-t a saját
“6_testing” mappádba. Ezt a file-t itt már nyugodtan kommentelheted, ha
szükséges. Értelmezd a kódot, és írj unit test-eket pytest segítségével.
A unit testeknél a következőket vedd figyelembe:
● Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a
tesztjeidben használsz.
● Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak
érdekében, hogy a tesztet több input-ra is lefuttassa (pl: teszteld a
deposit() method-ot pontosan 0 és negatív szám inputtal is).

● Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-
nek).

● Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-
elődik- e a megadott input-ra.

Extra: a BankAccount class nincs felkészülve minden lehetséges hibára
(non-number inputok, küldhetünk e saját magunknak pénzt stb.). Nézd át
alaposan a kódot, azonosítsd ezeket a hiányosságokat és implementáld a
szükséges változtatásokat a saját mappádban lévő file-ban. Ezután írj
teszteket amik ezeknek a kiegészítéseknek a helyességét ellenőrzik.
"""

import pytest
from bank_account_soma import BankAccount

# Csak egy teszt, hogy működik-e a környezet.... 
# (kicsit szenvedősen, de a végén csak sikerült mindent beállítani, hogy lefusson...)
def test_init_for_user_name():
    new_account = BankAccount("User01")
    assert new_account.owner == "User01"



# fixture beállítások
@pytest.fixture
def user1_account_with_balance():
    return BankAccount(owner="User1", balance=1000)

@pytest.fixture
def user2_account_no_balance():
    return BankAccount(owner="User2", balance=0)

# Betét számítás ellenőrzése - megfelelő az input
def test_valid_deposit_input(user2_account_no_balance):
    user2_account_no_balance.deposit(300)
    assert user2_account_no_balance.balance == 300

# paraméterezés több hibás inputra - betét és kivétel
@pytest.mark.parametrize("invalid_input", [0, -100])
def test_invalid_deposit_input(user1_account_with_balance,invalid_input):
    with pytest.raises(ValueError):
        user1_account_with_balance.deposit(invalid_input)

@pytest.mark.parametrize("invalid_input", [0, -100])
def test_invalid_withdraw_input(user2_account_no_balance, invalid_input):
      with pytest.raises(ValueError):
        user2_account_no_balance.withdraw(invalid_input)


# Kivétel logika ellenőrzése - van elég pénz a számlán
def test_withdraw_enough_many(user1_account_with_balance):
    user1_account_with_balance.withdraw(500)
    assert user1_account_with_balance.balance == 500

# Kivétel logika ellenőrzése - nincs elég pénz a számlán
def test_withdraw_not_enough_many(user2_account_no_balance):
    with pytest.raises(ValueError):
        user2_account_no_balance.withdraw(100)

# Átutalás ellenőrzése, ha jók az inputok
def test_transfer_valid_input(user1_account_with_balance, user2_account_no_balance):
    user1_account_with_balance.transfer(100, user2_account_no_balance)
    assert user1_account_with_balance.balance == 900
    assert user2_account_no_balance.balance == 100

# Átutalás nem BankAccount-nak
def test_transfer_invalid_input(user1_account_with_balance):
    with pytest.raises(TypeError):
        user1_account_with_balance.transfer(100, "Nothing")

# EXTRA
# Saját magának nem küldhet pénzt - ha azonos a tulaj
def test_transfer_self_transfer(user1_account_with_balance):
    with pytest.raises(ValueError):
        user1_account_with_balance.transfer(100, user1_account_with_balance)

