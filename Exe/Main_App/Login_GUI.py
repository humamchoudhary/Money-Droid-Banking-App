from Login import Login_Page
import PySimpleGUI as sg
import Main_GUI
from SignUp import *
import SignUp_GUI
# import main_be
font_big = ("Arial", 15)
font_small = ("Arial", 12)


def Window_Login():
    layout = [
        [sg.Text("")],
        [sg.Text("")],
        [sg.Image(source="logo.png")],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Text("", key="Notify", text_color="Green")],
        [sg.Text('User Name', font=font_small)],
        [sg.Input("", key="Username", size=(50, 3), justification='center')],
        [sg.Text("")],
        [sg.Text('Password', font=font_small)],
        [sg.Input("", key="Password", size=(50, 3),
                  justification='center', password_char="*")],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Button('Login', size=(30, 2))],
        [sg.Button('Register', size=(10, 2))],
    ]

    window = sg.Window('Money Droid - Login', layout, size=(
        400, 600), element_justification='center', resizable=True)
    return window


def Login():
    window = Window_Login()
    window.Finalize()

    while True:
        event, values = window.read()

        # print(values)
        # print(event)
        if event == 'Login':
            try:
                if len(values["Password"]) <= 6:
                    raise InvalidPasswordError("Password to short!")
                else:
                    login = Login_Page(
                        values["Username"], values["Password"])

                    account = login.Get_Account()
                # print(account.__dict__)
                # print(account)

            except Exception as e:
                window['Notify'].Update(f"{e}", text_color="Red")

            else:
                window.close()
                Main_GUI.Main(account)

        if event == "Register":
            window.close()
            SignUp_GUI.SignUp()

        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    Login()
