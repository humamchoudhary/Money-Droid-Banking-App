import pickle
from tinydb import TinyDB, Query
from Exceptions import *
from SignUp import *


def get_data(token):
    file = open(f'{token}.pkl', 'rb')
    enc_account = pickle.load(file)
    account = enc_account.obj
    file.close()
    return account


def check_card_digits(number):
    invalid = True
    while invalid:
        for i in range(len(number)):
            if number[i] == number[i:4]:
                invalid = True
            else:
                invalid = False


class DB:
    DB = TinyDB("database.json")
    User = Query()

    def Load_Account(self, account):
        self.account = account
        data = self.DB.search(self.User.username == account.username)
        data = data[0]
        self.token = data["token"]

    def Pay_Bill(self, bill_type: str, ref_num: str, amount: float):
        try:
            amount = float(amount)
        except:
            raise InvalidAccountNumberError("Invalid amount")
        if len(ref_num) == 14:
            if self.account.balance - amount >= 0:
                self.account.balance -= amount  # Update account balance  ----update----
                self.Transection_Log("Incoming", amount,
                                     self.account, purpose=f"{bill_type} bill Payment")
                self.Update(self.token, self.account)

            else:
                # Insuff balance ----error----
                raise InsufficientBalanceError(
                    "Insufficient Balance. Please add some funds")
        else:
            raise InvalidRefNumber("Invalid reference number")

    def Deposit(self, card_number: int, amount: float, exp_data: str, cvv: int):
        """ 
        It will start with 4, 5 and 6
        It will be 16 digits long
        Numbers must contain only digits
        It may have digits in four groups separated by '-'
        It must not use any other separator like space or underscore
        It must not have 4 or more consecutive same digits
        """
        try:
            card_number = int(card_number)
        except:
            raise InvalidCardError("Invalid card number")
        try:
            amount = float(amount)

        except:
            raise InvalidAmount("Invalid amount")
        try:
            cvv = int(cvv)

        except:
            raise InvalidCVVError("Invalid CVV")

        transaction = True
        if str(card_number)[0] in "456":
            if len(str(card_number)) == 16:
                if type(card_number) is int:
                    print("Card is valid")

                else:
                    transaction = False
                    # Raise invalid card ----error----
                    raise InvalidCardError(
                        f"Card number can only be int but {type(card_number)} was given")
            else:
                transaction = False
                # Raise invalid card ----error----
                raise InvalidCardError(
                    f"Length of the a card number must be 16 but {len(str(card_number))} was given")
        else:
            transaction = False
            # Raise invalid card ----error----
            raise InvalidCardError("Card number mmust start from 4,5 or 6")
        if len(str(cvv)) == 3:
            print("valid")
        else:
            transaction = False
            # Raise invalid cvv ----error----
            raise InvalidCVVError("Invalid CVV")
        if transaction:
            self.account.balance += amount  # Update account balance  ----update----
            self.Transection_Log("Incoming", amount,
                                 self.account, "Deposit")
            self.Update(self.token, self.account)
        else:

            print("Transction not done")

    def Withdraw(self, account_number: int, amount: float):
        try:
            account_number = int(account_number)
        except:
            raise InvalidAccountNumberError("Invalid account number")
        try:
            amount = float(amount)
        except:
            raise InvalidAccountNumberError("Invalid amount")
        if amount < 10:
            raise InvalidAmount("Minimum amount for withdrawal is 10RS")
        if str(account_number)[0] in "456":
            if len(str(account_number)) == 16:
                if type(account_number) is int:
                    print("Card is valid")
                    transaction = True

                else:
                    # Raise invalid card ----error----
                    raise InvalidAccountNumberError(
                        f"Invalid account number")
            else:
                raise InvalidAccountNumberError(
                    f"Invalid account number")  # Raise invalid card ----error----

        else:
            transaction = False
            # Raise invalid card ----error----
            raise InvalidAccountNumberError(
                "Invalid account number")
        if transaction:
            if self.Check_Bal(amount):
                self.account.balance -= amount  # Update account balance  ----update----
                data = self.DB.search(self.User.email == account_number)
                self.Transection_Log("Outgoing", amount,
                                     self.account, "Withdraw")
                self.Update(self.token, self.account)
            else:
                raise InsufficientBalanceError("Insufficient Balance")

    def Trans_Money(self, account_number: str, amount: float, purpose: str):

        try:
            amount = float(amount)
        except:
            raise InvalidAccountNumberError("Invalid amount")
        if account_number == self.account.email:
            raise InvalidAccountNumberError(
                "Can not send money to the logged in account")

        self.Find_Account(account_number)
        if self.account2 == None:
            # Raise invalid account ----error----
            raise InvalidAccountNumberError("Invalid account")

        else:
            if self.Check_Bal(amount):
                self.account2.balance += amount
                self.account.balance -= amount
                # Update account balance  ----update----
                self.Transection_Log("Outgoing", amount, self.account, purpose)
                self.Update(self.token, self.account)
                # Update account balance  ----update----
                data = self.DB.search(self.User.email == account_number)
                data = data[0]
                token2 = data["token"]
                self.Transection_Log("Incoming", amount,
                                     self.account2, purpose)
                self.Update(token2, self.account2)
            else:
                raise InsufficientBalanceError("Insuffi balance")

    def Check_Bal(self, amount):
        if self.account.balance - amount >= 0:
            return True

        else:
            return False

    def LogOut(self):
        del self.account

    def Print(self):
        print(self.account.balance)

    def Find_Account(self, email):
        try:
            data = self.DB.search(self.User.email == email)
            data = data[0]
            token = data["token"]
            self.account2 = get_data(token)
        except Exception as e:
            raise InvalidAccountNumberError("Account not found")

    def Update(self, token, obj):
        encrypt = Encrypt_Data(token, obj)
        with open(f'{token}.pkl', 'wb') as enc_file:
            pickle.dump(encrypt, enc_file, None)
        enc_file.close()

    def Transection_Log(self, transaction_type, amount, account, purpose=""):
        transection = {"Type": transaction_type,
                       "Amount": amount, "Purpose": purpose}
        account.transection_log.append(transection)
