class BankAccount:
    def __init__(
        self, owner: str, balance: float = 0.0
    ):  # constructor that initializes the bank account with an owner and a balance
        # validate that the owner is not null
        if not isinstance(owner, str):
            raise TypeError("The Owner must be a string.")
        if not owner.strip():
            raise ValueError("Owner name cannot be empty")
        # Validate that the account is not initialized with negative amount
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):  # adding money to the account
        # Validate non-number input
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number")
        # Validate for non-negative number input
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

    def withdraw(self, amount: float):  # remove money from the account
        # Validate for non-negative number input
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        # Validate for sufficient balance
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        # Validate for non-number inputs
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number")
        self.balance -= amount

    def transfer(
        self, amount: float, target_account: "BankAccount"
    ):  # transfer money to another account
        # Validate if the target is a bankaccount
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        # validate if trying to tranfer to self
        if target_account is self:
            raise ValueError("Cannot transfer money to the same account.")

        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):  # get the current balance
        return self.balance

    def __str__(self):  # get the current state of the account
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
