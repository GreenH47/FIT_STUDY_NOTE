# importing random library
import random


class BankAccount:
    account_list = []

    def __init__(self, username="", user_email="",
                 user_mobile="", balance=0.0, account_status=False):
        self.username = username
        self.user_email = user_email
        self.user_mobile = user_mobile
        self.balance = balance
        self.account_status = account_status
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        selected_number = random.randint(1000000.9999999)
        all_account_number = [account.account_number for account in self.account_list]

        while selected_number in all_account_number:
            selected_number = random.randint(1000000.9999999)
        return selected_number

    # return total number of account
    def get_total_num_account(self):
        return len(self.account_list)

    def deposit(self, deposit_amt):  # add validation
        if self.account_status and deposit_amt >= 0:
            self.balance += deposit_amt
        else:
            print("account status wrong plz check ")

    def withdraw(self, withdraw_amt):  # add validation
        if self.account_status and withdraw_amt <= self.balance:
            self.balance -= withdraw_amt
        else:
            print("")

    def search_accounts_by_username(self, username):
        return [acc for acc in self.account_list if acc.username == username]

    def __str__(self):
        return f"{self.account_number} | {self.username} | {self.balance}"

    def display(self):
        for acc in BankAccount.account_list:
            print(acc)


if __name__ == "__main__":
    # your test code

    b1 = BankAccount(username="Jack", user_email="Jack@gmail.com",
                     user_mobile="011111111", balance=500.0, account_status=True)
    b2 = BankAccount(username="Jack", user_email="Jack@gmail.com",
                     user_mobile="011111111", balance=1500.0, account_status=True)
    b3 = BankAccount(username="Peter", user_email="Peter@gmail.com",
                     user_mobile="02222222", balance=5500.0, account_status=True)

    BankAccount.account_list.append(b1)
    BankAccount.account_list.append(b2)
    BankAccount.account_list.append(b3)
    print("--------------------------------------------")

    b1.display()
    print("total_num_account=", b1.get_total_num_account())
    print("--------------------------------------------")
    b1.deposit(10000)
    b1.withdraw(50000)
    print("--------------------------------------------")
    for item in b1.search_accounts_by_username("Jack"):
        print(str(item))

    BankAccount.account_list.clear()
