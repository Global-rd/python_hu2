import pytest
from bank_account import BankAccount

#------két fixture létrehozása a "fiktív" accountokra------

@pytest.fixture
def empty_account():
    return BankAccount("User1")

@pytest.fixture
def registered_account_with_amount():
    return BankAccount("Test User", balance=1000)

#----------------------------------------------------------

# parametrizált tesztek 0 és negatív depositra
@pytest.mark.parametrize("deposit_amount", [0, -100])
def test_deposit_invalid_amount_raises(deposit_amount, empty_account):
    with pytest.raises(ValueError):
        empty_account.deposit(deposit_amount)

# edge case: nem BankAccount object-nek pénz küldés
def test_transfer_to_invalid_target_raises(empty_account):
    with pytest.raises(TypeError):
        empty_account.transfer(100, "invalid_account")

#----megfelelő exceptionok tesztelése----

# negatív kezdőegyenlegre
def test_account_with_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("User",-100)

# negatív mennyiség befizetése
def test_deposit_with_negative_amount(registered_account_with_amount):
    with pytest.raises(ValueError):
        registered_account_with_amount.deposit(-100)

# negatív értékű pénzfelvétel
def test_withdraw_with_negative_amount(registered_account_with_amount):
    with pytest.raises(ValueError):
        registered_account_with_amount.withdraw(-100)

# egyenlegnél több pénz kivételére
def test_for_insufficient_funds(empty_account):
    with pytest.raises(ValueError):
        empty_account.withdraw(100)


