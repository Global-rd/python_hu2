import pytest
from bank_account import BankAccount, Person

# Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
@pytest.fixture
def account_with_postive_balance():
    return BankAccount("111111112222222233333333", "Bruce Wayne", 100)

def test_deposit_into_positive_balance_account(account_with_postive_balance):
    account_with_postive_balance.deposit(50)
    assert account_with_postive_balance.balance == 150.0 # check if the balance increase correctly

@pytest.fixture
def account_with_zero_balance():
    return BankAccount("123456780000000011223344", "Peter Parker", 0)

def test_withdraw_from_zero_balance_account(account_with_zero_balance):
    with pytest.raises(ValueError):
        account_with_zero_balance.withdraw(50) # check insufficient funds.

# teszt, ami @pytest.mark.parametrize-t használ
@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),  # test with zero value
    (-1, ValueError),  # test with negative value
    (-50, ValueError)  # test with another negative value
])
def test_deposit_invalid_input(account_with_postive_balance, amount, expected_exception):
    with pytest.raises(expected_exception):
        account_with_postive_balance.deposit(amount)

# BankAccount létrehozása nem megfelelő számlaszámokkal
@pytest.mark.parametrize("account_number, expected_exception", [
    ("12345678123456781234567", ValueError),  # test with less than 24 digits
    ("HU0212345678945612000000", ValueError),  # test with alphanumeric characters
    ("", ValueError),  # test with empty string value
    (None, ValueError)  # test with empty string value
])
def test_account_init_with_account_number(account_number, expected_exception):
    with pytest.raises(expected_exception):
        account = BankAccount(account_number, "Gombóc Artúr", 100.00)

# fixture nem BankAccount class-ra
@pytest.fixture
def owner():
   return Person("Gombóc Artúr", "1088 Budapest, Népszínház utca 675.", "+36201234567", "g.artur@chocolatefactory.com")

#Edge case: transfer BankAccount-ról nem BankAccount-ra
def test_transfer_to_non_bank_account(account_with_postive_balance, owner):
    
    # A cél a fenti "owner" fixture, ami nem BankAccount típusú
    with pytest.raises(TypeError):
        account_with_postive_balance.transfer(20, owner)

# Transfer ugyanarra a számlaszámra
def test_transfer_to_the_same_account():
    src_account = BankAccount("111111112222222233333333","Gombóc Artúr",100.00)
    dest_account = BankAccount("111111112222222233333333","Festéktüsszentő Hapcibenő",100.00)

    with pytest.raises(ValueError):
        src_account.transfer(55.50, dest_account)