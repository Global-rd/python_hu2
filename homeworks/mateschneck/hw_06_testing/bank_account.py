class BankAccount:
        # az osztály definiálása

    def __init__(self, owner: str, balance: float = 0.0):

        # inicializálás

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner # tulajdonos
        self.balance = balance # egyenleg
    
    def deposit(self, amount: float):  #betét befizetés
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float): #kifizetés
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.") # nem lehet pozitív
        if amount > self.balance:
            raise ValueError("Insufficient funds.") # hiba, ha túl sokat akar levenni
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'): # átutalás
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.") # hiba ha nem jó a számlaszám típus
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance # visszaadja a balance-t

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}" # szövegként visszaadja a főbb adatokat

