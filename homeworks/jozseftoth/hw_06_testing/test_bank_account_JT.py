import pytest
from  bank_account_JT import BankAccount  # import the BankAccount class from bank_account.py



def test_initial_balance():
    account = BankAccount("Alice", 100.0)
    assert account.get_balance() == 100.0

def test_initial_balance_negative():
    with pytest.raises(ValueError):
        BankAccount("Alice", -100.0)

def test_deposit():
    account = BankAccount("Alice", 100.0)
    account.deposit(50.0)
    assert account.get_balance() == 150.0

def test_deposit_negative():
    account = BankAccount("Alice", 100.0)
    with pytest.raises(ValueError):
        account.deposit(-50.0)

def test_withdraw():
    account = BankAccount("Alice", 100.0)
    account.withdraw(50.0)
    assert account.get_balance() == 50.0

def test_withdraw_insufficient_funds():
    account = BankAccount("Alice", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(150.0)

def test_transfer():
    account1 = BankAccount("Alice", 100.0)
    account2 = BankAccount("Bob", 50.0)
    account1.transfer(50.0, account2)
    assert account1.get_balance() == 50.0
    assert account2.get_balance() == 100.0

def test_transfer_invalid_target():
    account = BankAccount("Alice", 100.0)
    with pytest.raises(TypeError):
        account.transfer(50.0, "Not a BankAccount")

        
@pytest.mark.parametrize("amount", [0.0, -50.0])
def test_deposit_invalid(amount):
    account = BankAccount("Alice", 100.0)
    with pytest.raises(ValueError):
     account.deposit(amount)


@pytest.mark.parametrize("amount", [0.0, -50.0])
def test_deposit_invalid(amount):
    account = BankAccount("Alice", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(amount)



@pytest.mark.parametrize("target", [None, 123, "Not a BankAccount", 45.67, []])
def test_transfer_invalid_target(target):
    account = BankAccount("Alice", 100.0)
    with pytest.raises(TypeError):
        account.transfer(50.0, target)


@pytest.mark.parametrize("owner", ["", None])
def test_initial_balance_invalid_owner(owner):
    with pytest.raises(ValueError):
        BankAccount(owner, 100.0)


if __name__ == "__main__":
    pytest.main()
