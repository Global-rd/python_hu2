import pytest
from bank_account import BankAccount

@pytest.fixture
def szamla_peter():
    return BankAccount("Péter", 100.0)

@pytest.fixture
def szamla_anna():
    return BankAccount("Anna", 200.0)

@pytest.mark.parametrize("osszeg", [0, -10, -0.01])
def test_befizetes_ervenytelen_osszeg(szamla_peter, osszeg):
    with pytest.raises(ValueError, match="A befizetés összegének pozitívnak kell lennie!"):
        szamla_peter.deposit(osszeg)

def test_befizetes_sikeres(szamla_peter):
    szamla_peter.deposit(50)
    assert szamla_peter.get_balance() == 150.0

@pytest.mark.parametrize("osszeg", [0, -5])
def test_kivetel_ervenytelen_osszeg(szamla_peter, osszeg):
    with pytest.raises(ValueError, match="A kivétel összegének pozitívnak kell lennie!"):
        szamla_peter.withdraw(osszeg)

def test_kivetel_nincs_fedezet(szamla_peter):
    with pytest.raises(ValueError, match="Nincs elegendő pénz!"):
        szamla_peter.withdraw(200)

def test_kivetel_sikeres(szamla_anna):
    szamla_anna.withdraw(50)
    assert szamla_anna.get_balance() == 150.0

def test_utalas_sikeres(szamla_peter, szamla_anna):
    szamla_peter.transfer(50, szamla_anna)
    assert szamla_peter.get_balance() == 50.0
    assert szamla_anna.get_balance() == 250.0

@pytest.mark.parametrize("cel", [None, "szöveg", 42, 3.14, object()])
def test_utalas_ervenytelen_cel(szamla_peter, cel):
    with pytest.raises(TypeError, match="Rossz száma!"):
        szamla_peter.transfer(10, cel)

def test_utalas_nincs_fedezet(szamla_peter, szamla_anna):
    with pytest.raises(ValueError, match="Nincs eleég pénZ!"):
        szamla_peter.transfer(1000, szamla_anna)


def test_negativ_kezdoegyenleg():
    with pytest.raises(ValueError, match="A kezdő egyenleg nem lehet negatív."):
        BankAccount("Miklós", -100)

def test_szamla_str(szamla_peter):
    assert str(szamla_peter) == "Péter számlája, Egyenleg: 100.00 Ft"