import datetime
import pytz


class Account:
    # A simple account class with balance

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Account._current_time(), - amount))
        else:
            print("Amount must be greater than zero and no more than your account balance.")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(5000)

    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.__balance = (200)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_balance()
    steph.show_transactions()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()
