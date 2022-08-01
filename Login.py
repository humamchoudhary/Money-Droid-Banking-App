from SignUp import *
from tinydb import TinyDB, Query
import pickle
from Exceptions import *
import Main_App


class Login_Page:
    DB = TinyDB("database.json")
    User = Query()

    def __init__(self, username, password):
        self.username = username  # ---Input username
        self.password = password  # ---Input password
        self.account = self.CheckPassword()

    def CheckPassword(self):
        data = self.DB.search(self.User.username == self.username)
        try:
            l = data[0]
            token = l["token"]
            file = open(f'{token}.pkl', 'rb')
            enc_account = pickle.load(file)
        except FileNotFoundError:
            raise AccountNotFoundError("User does not exists!")
        except IndexError:
            raise AccountNotFoundError("User does not exists!")

        account = enc_account.obj
        file.close()
        plaintext = self.password.encode()
        hash = hashlib.sha256(plaintext)
        hashhex = hash.hexdigest()
        if account.password == hashhex:
            return account

        else:
            raise InvalidPasswordError("Invalid password!")

    def Get_Account(self):
        return self.account

