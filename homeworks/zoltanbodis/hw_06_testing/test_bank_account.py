import pytest
from bank_account import BankAccount, Person

# Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
@pytest.fixture
def account_with_postive_balance():
    return BankAccount("Bruce Wayne", 100)

def test_deposit_into_positive_balance_account(account_with_postive_balance):
    account_with_postive_balance.deposit(50)
    assert account_with_postive_balance.balance == 150.0 # check if the balance increase correctly

@pytest.fixture
def account_with_zero_balance():
    return BankAccount("Peter Parker", 0)

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

# fixture nem BankAccount class-ra
@pytest.fixture
def owner():
   return Person("Gombóc Artúr", "1088 Budapest, Népszínház utca 675.", "+36201234567", "g.artur@chocolatefactory.com")

#Edge case: transfer BankAccount-ról nem BankAccount-ra
def test_transfer_to_non_bank_account(account_with_postive_balance, owner):
    
    # A cél a fenti "owner" fixture, ami nem BankAccount típusú
    with pytest.raises(TypeError):
        account_with_postive_balance.transfer(20, owner)

