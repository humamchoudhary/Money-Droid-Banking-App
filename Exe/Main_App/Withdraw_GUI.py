import PySimpleGUI as sg
import App
from Exceptions import *
import Main_GUI
from SignUp import *
font_huge = ("Arial", 20)
font_small = ("Arial", 12)
font_big = ("Arial", 15)
db = App.DB()


def withdraw_win():
    frame_layout = [[sg.Text('Current balance', font=font_big)],
                    [sg.Text("Rs ",  font=font_big), sg.Text(
                        "0.00", font=font_big, key="Bal")], ]
    layout = [
        [sg.Text("")],
        [sg.Text("")],
        [sg.Frame("Withdraw",   frame_layout, font=font_small,
                  element_justification="c", size=(300, 100), title_location="n")],

        [sg.Text("")],
        [sg.Text("", key="Notify")],
        [sg.Text("Receiver's Details", font=font_small)],
        [sg.Text("")],
        [sg.Text('Account Number', font=font_small)],
        [sg.Input("", key="Account_Number", size=(
            70, 3), justification='center')],
        [sg.Text("")],
        [sg.Text('Amount', font=font_small)],
        [sg.Input("", key="Amount",
                  size=(70, 3), justification='center')],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Button('Withdraw', size=(30, 2))],
        [sg.Button('Back', size=(10, 2))],
    ]

    return sg.Window('Money Droid - Withdraw', layout, size=(
        400, 600), element_justification='center', resizable=True)


def Withdraw(account):
    db.Load_Account(account)
    window = withdraw_win()
    window.Finalize()
    window["Bal"].Update("%.2f" % (db.account.balance))
    while True:
        event, values = window.read()
        # print(values)
        # print(event)
        if event == 'Withdraw' and (values['Account_Number'] == '' or values['Amount'] == ''):
            window["Notify"].Update(
                "Please fill all fields!", text_color="Red")
        else:
            try:
                db.Withdraw((values["Account_Number"]),
                            (values['Amount']))
                window["Notify"].Update(
                    "Transection successful", text_color="Light Green")
                window["Bal"].Update(f"{db.account.balance}")

            except Exception as e:
                window['Notify'].Update(f"{e}")
                # window['Notify'].Update(text_color="Red")

        if event == "Back":
            window.close()
            Main_GUI.Main(account)

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    window.close()
