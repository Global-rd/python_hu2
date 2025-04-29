@pytest.fixture
def account_kratos():
    return BankAccount("Kratos", 500.00)

@pytest.fixture
def account_zelda():
    return BankAccount("Zelda", 850.75)


def test_initial_balance(account_kratos):
    assert account_kratos.get_balance() == 500.00

def test_deposit(account_kratos):
    account_kratos.deposit(200.00)
    assert account_kratos.get_balance() == 700.00

def test_withdraw(account_zelda):
    account_zelda.withdraw(125.75)
    assert account_zelda.get_balance() == 725.00

def test_transfer(account_kratos, account_zelda):
    account_kratos.transfer(100.0, account_zelda)
    assert account_kratos.get_balance() == 400.0
    assert account_zelda.get_balance() == 950.75


@pytest.mark.parametrize("amount", [0, -50.0])
def test_deposit_invalid_amount(account_zelda, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account_zelda.deposit(amount)


def test_transfer_invalid_target(account_kratos):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_kratos.transfer(75.0, "Master Sword")


def test_withdraw_more_than_balance(account_kratos):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_kratos.withdraw(999.0)

def test_withdraw_negative(account_zelda):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_zelda.withdraw(-200.0)

def test_create_account_with_negative_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("GlitchHunter", -9999.99)
