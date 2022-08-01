import PySimpleGUI as sg
import App
import Main_GUI
from Exceptions import *
from SignUp import *
import Main_App

font_big = ("Arial", 15)
font_small = ("Arial", 12)
db = App.DB()


def Trans_win():
    # Gui element location
    frame_layout = [[sg.Text("Current Balance:",  font=font_big)], [sg.Text("RS", font=font_big), sg.Text(
        f"{db.account.balance}", key="Bal", font=font_big)], ]
    layout = [
        [sg.Text("")],
        [sg.Frame("Transfer Money", frame_layout, size=(300, 100),
                  element_justification="center", font=font_small, title_location="n")],
        [sg.Text("")],
        [sg.Text("", key="Notifi", font=font_small)],
        [sg.Text("Account Number/Email", font=font_small)],
        [sg.Input("", key="ACCNUM", size=(50, 2), justification="center")],
        [sg.Text("")],
        [sg.Text("Amount", font=font_small)],
        [sg.Input("", key="AMOUNT", size=(50, 2), justification="center")],
        [sg.Text("")],
        [sg.Text("Purpose of transfer (optional)", font=font_small)],
        [sg.Input("",  key="POT",
                  size=(50, 2), justification="center")],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Button("Send", size=(20, 2))],
        [sg.Button("Back", size=(10, 2))],
    ]

    return sg.Window('Moeny Droid - Transfer', layout, size=(
        400, 600), element_justification='center', resizable=True)


def transfer(account):
    db.Load_Account(account)    # -Get account from the login-
    window = Trans_win()
    window.Finalize()
    while True:
        event, values = window.Read()
        if event == "Send":

            if (values["ACCNUM"] == '' or values["AMOUNT"] == ''):
                window['Notifi'].Update('Please fill all fields',
                                        text_color="Red")

            else:
                account_num = values["ACCNUM"]
                amount = values["AMOUNT"]
                pot = values["POT"]
                try:
                    db.Trans_Money(account_num, int(amount), pot)
                    window["Bal"].Update("%.2f" % (db.account.balance))

                except Exception as e:
                    window['Notifi'].Update(f'{e}', text_color="Red")

                else:
                    window['Notifi'].Update('Transection Successful',
                                            text_color="Light Green")
        if event == "Back":
            window.close()
            Main_GUI.Main(account)

        if event == sg.WIN_CLOSED:
            break

    window.close()
