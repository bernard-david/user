class User:
    bank_name = "Bank of America"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, amount, destination):
        self.account_balance -= amount
        destination.account_balance += amount
        self.display_user_balance()
        destination.display_user_balance()

david = User("David Bernard", "dpbernard18@gmail.com")
monty = User("Monty Python", "monty@python.com")
steph = User("Steph Rodriguez", "stephrod@gmail.com")
# First user activity
david.make_deposit(1000)
david.make_deposit(1000)
david.make_deposit(1000)
david.make_withdrawal(1500)
david.display_user_balance()
# Second user activity
monty.make_deposit(400)
monty.make_deposit(900)
monty.make_withdrawal(100)
monty.make_withdrawal(500)
monty.display_user_balance()
# Third user activity
steph.make_deposit(10000)
steph.make_withdrawal(300)
steph.make_withdrawal(1000)
steph.make_withdrawal(600)
steph.display_user_balance()
# Bonus
david.transfer_money(500, steph)