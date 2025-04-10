import pytest
from bank_account import BankAccount

# Két teszt fiók létrehozása
@pytest.fixture
def erika_account():
    return BankAccount("Erika", 500)

@pytest.fixture
def norbi_account():
    return BankAccount("Norbi", 300)

# Teszt a befizetésre
def test_deposit_adds_money(erika_account):
    erika_account.deposit(50)
    assert erika_account.get_balance() == 550  # 500 + 50

# Nem lehet a befizetés nulla vagy negatív összeg
@pytest.mark.parametrize("amount", [0, -10])
def test_deposit_invalid_amount(erika_account, amount):
    with pytest.raises(ValueError):
        erika_account.deposit(amount)

# Pénz levétel teszt
def test_withdraw_removes_money(norbi_account):
    norbi_account.withdraw(50)
    assert norbi_account.get_balance() == 250  # 300 - 50

# Túl sok pénz levétele hiba
def test_withdraw_more_than_balance(erika_account):
    with pytest.raises(ValueError):
        erika_account.withdraw(1000)

# Nem lehet negatív vagy nulla összeget levenni
@pytest.mark.parametrize("amount", [0, -5, -0.01])
def test_withdraw_negative_or_zero(erika_account, amount):
    with pytest.raises(ValueError):
        erika_account.withdraw(amount)

# Tranzakció a fiókok között
def test_transfer_between_accounts(erika_account, norbi_account):
    erika_account.transfer(30, norbi_account)
    assert erika_account.get_balance() == 470  # 500 - 30
    assert norbi_account.get_balance() == 330  # 300 + 30

# Nem BankAccount típusú fiók esetén hibát dob
def test_transfer_to_non_account(erika_account):
    with pytest.raises(TypeError):
        erika_account.transfer(10, "invalid_account")

# Saját magának ne utalhasson
def test_transfer_to_self(erika_account):
    with pytest.raises(ValueError):
        erika_account.transfer(10, erika_account)

# Teszteli, hogy a név szöveges típusú-e
def test_invalid_owner_type():
    with pytest.raises(TypeError):
        BankAccount(1212)

# Ellenőrzi, hogy a megadott összeg szám típusú-e deposit esetén
@pytest.mark.parametrize("amount", ["ötszáz", None, [400]])
def test_deposit_with_invalid_type(erika_account, amount):
    with pytest.raises(TypeError):
        erika_account.deposit(amount)

#Ellenőrzi, hogy a megadott összeg szám típusú-e 
@pytest.mark.parametrize("amount", ["ötven", None, {"összeg": 100}])
def test_withdraw_with_invalid_type(erika_account, amount):
    with pytest.raises(TypeError):
        erika_account.withdraw(amount)



