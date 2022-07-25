from tinydb import TinyDB, Query
import uuid
import pickle
from Exceptions import *
import hashlib


class Person:
    def __init__(self, first_name, mid_name, last_name, gender):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.gender = gender

    def __str__(self):
        pass
        return f"Name: {self.first_name} {self.mid_name} {self.last_name} \n Gender: {self.gender}"


class Account:
    def __init__(self, first_name, mid_name, last_name, gender, address, email, username, password):
        self.owner = Person(first_name, mid_name, last_name, gender)
        self.email = email
        self.username = username
        self.address = address
        self.password = password
        self.balance = 0
        self.transection_log = []

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


class Encrypt_Data:
    def __init__(self, token, obj):
        self.token = token
        self.obj = obj


class Signup_Page:
    DB = TinyDB("database.json")
    User = Query()
    __account_details = {}

    def Regester(self, f_name, m_name, l_name, address, gender, email, username, password):
        accounts = {}
        Signup = False
        email = email.lower()
        password = password.encode()
        hash = hashlib.sha256(password)
        hashhex = hash.hexdigest()
        account = Account(f_name, m_name, l_name, gender,
                          address, email, username, hashhex)
        if self.DB.search(self.User.username == username):
            raise AccountExistsError("This Account already Exits")
            del account
        else:
            token = account.GenToken()
        encrypt = Encrypt_Data(token, account)
        with open(f'{token}.pkl', 'wb') as enc_file:
            pickle.dump(encrypt, enc_file, None)
        accounts["username"] = username
        accounts["token"] = token
        accounts["email"] = email
        self.DB.insert(accounts)
        Signup = True  # .....signup done....
        current_user = account

    def Print_Account_Details(self):
        search_name = input("Enter the username to search: ")
        data = self.DB.search(self.User.username == search_name)
        for entry in data:
            for key in entry:
                print(f"{key}: {entry[key]}")


if __name__ == '__main__':
    signup = Signup_Page()
    signup.Regester()
