import PySimpleGUI as sg
import App
import Main_GUI
import Main_App

font_small = ("Arial", 12)
font_big = ("Arial", 15)


def Deposit_Win():
    frame_layout = [[sg.Text('Current balance', font=font_big)],
                    [sg.Text("Rs ",  font=font_big), sg.Text(
                        "0.00", font=font_big, key="Bal")], ]
    layout = [
        [sg.Text("")],
        [sg.Frame("Deposit Money", frame_layout, size=(300, 100),
                  element_justification="center", font=font_small, title_location="n")],
        [sg.Text("")],
        [sg.Text("", key="Notify")],
        [sg.Text("Add cash via credit/debit card", font=("Arial", 10))],
        [sg.Text("Card Number")],
        [sg.Input("", size=(50, 3), key="Card_Num", justification='centre')],
        [sg.Text("")],
        [sg.Text("Amount")],
        [sg.Input("", size=(50, 3), key="Amount", justification='centre')],
        [sg.Text("")],
        [sg.Text("Expiry Date"), sg.Text("       "), sg.Text(
            "         "), sg.Text("CVV"), sg.Text("      ")],
        [sg.Input("", size=(24, 3), key="Exp_Date", justification='centre'),
         sg.Input("", size=(24, 3), key="CVV", justification='centre')],
        [sg.Text("")],

        [sg.Button("Submit", size=(20, 2))],
        [sg.Button("Back", size=(10, 2))],

    ]
    return sg.Window('Moneydroid - Deposit', layout, size=(
        400, 600), element_justification='center', resizable=True)


def Deposit(account):

    db = App.DB()
    db.Load_Account(account)
    window = Deposit_Win()
    window.Finalize()
    # print(type(db.account.balance))

    while True:
        window["Bal"].Update("%.2f" % (db.account.balance))
        event, values = window.read()
        # print(values)
        # print(event)
        filled = False
        if event == "Submit":
            for key in values:
                if values[key] == "":
                    window["Notify"].Update(
                        "Please fill all fields!", text_color="Red")
                    filled = False
                    break
                else:
                    filled = True

            if filled:
                try:
                    db.Deposit(values['Card_Num'], values['Amount'],
                               values['Exp_Date'], values['CVV'])
                    window["Notify"].Update(
                        "Transfer successfull!", text_color="Light Green")
                    window["Bal"].Update("%.2f" % (db.account.balance))

                except Exception as e:
                    window["Notify"].Update(f"{e}", text_color="Red")

        if event == "Back":
            window.close()
            Main_GUI.Main(account)

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    window.close()

