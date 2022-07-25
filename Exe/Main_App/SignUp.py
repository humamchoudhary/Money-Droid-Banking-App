from tinydb import TinyDB, Query
import uuid
import pickle
from Exceptions import *
import hashlib
from abc import ABC


class Person(ABC):
    def __init__(self, first_name, mid_name, last_name, gender):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.gender = gender
        return self

    def __str__(self):
        return f"Name: {self.first_name} {self.mid_name} {self.last_name} \n Gender: {self.gender}"


class Account(Person):
    def __init__(self, first_name, mid_name, last_name, gender, address, email, username, password, acc_type):
        self.owner = super().__init__(first_name, mid_name, last_name, gender)
        self.email = email
        self.username = username
        self.address = address
        self.password = password
        self.balance = 0
        self.transection_log = []
        self.account_type = acc_type

    def GenToken(self):
        uuid_str = uuid.uuid1().urn
        self.__token = uuid_str[9:]
        return self.__token

    @property
    def token(self):
        self.__token

    def __str__(self):
        self.GenToken()
        return self.__token


class Savings_Account(Account):
    intrest = 0.05

    def Transection(self):
        self.balance += self.balance * self.intrest


class Current_Account(Account):
    fee = 100

    def Transection(self):
        self.balance -= self.fee


class Encrypt_Data:
    def __init__(self, token, obj):
        self.token = token
        self.obj = obj


class Signup_Page:
    DB = TinyDB("database.json")
    User = Query()
    __account_details = {}

    def Regester(self, f_name, m_name, l_name, address, gender, email, username, password, acc_type):
        accounts = {}
        Signup = False
        email = email.lower()
        password = password.encode()
        hash = hashlib.sha256(password)
        hashhex = hash.hexdigest()
        if acc_type == "Savings":
            account = Savings_Account(f_name, m_name, l_name, gender,
                                      address, email, username, hashhex, acc_type)
        else:
            account = Current_Account(f_name, m_name, l_name, gender,
                                      address, email, username, hashhex, acc_type)

        if self.DB.search(self.User.username == username):
            raise AccountExistsError("This Account already Exits")
        else:
            token = account.GenToken()
        encrypt = Encrypt_Data(token, account)
        with open(f'{token}.pkl', 'wb') as enc_file:
            pickle.dump(encrypt, enc_file, None)
        accounts["username"] = username
        accounts["token"] = token
        accounts["email"] = email
        self.DB.insert(accounts)

    def Print_Account_Details(self):
        search_name = input("Enter the username to search: ")
        data = self.DB.search(self.User.username == search_name)
        for entry in data:
            for key in entry:
                print(f"{key}: {entry[key]}")
