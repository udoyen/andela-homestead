class BankAccount:
    def __init__(self):
        pass

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        # minimum balance
        self.balance = 500

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not amount <= 0:
            if not amount > self.balance:
                if not self.balance - amount <= 500:
                    self.balance -= amount
                    return self.balance
                else:
                    return "Cannot withdraw beyond the minimum account balance"
            else:
                return "Cannot withdraw beyond the current account balance"
        else:
            return "Invalid withdraw amount"
        # return self.balance


class CurrentAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdraw amount"
        elif amount > self.balance:
            return "Cannot withdraw beyond the current account balance"

        else:
            self.balance -= amount
            return self.balance


c = SavingsAccount()
# print(c.deposit(23001))
print(c.withdraw(300))
