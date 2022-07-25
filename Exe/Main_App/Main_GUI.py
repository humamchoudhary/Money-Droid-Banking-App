import PySimpleGUI as sg
import Bill_Payment_GUI
import Login_GUI
import Transfer_GUI
import Withdraw_GUI
import Deposit_GUI
import Trans_log_GUI
font_huge = ("Arial", 20)
font_small = ("Arial", 12)
font_big = ("Arial", 15)


def Window_Main():
    frame_layout = [[sg.Text('Account Number/email', font=font_small, key="Acc_Num")],
                    [sg.Text('', key="Username", font=font_big)],
                    #[sg.Input("", key="Username", size=(70, 3), justification='center')],
                    [sg.Text("Rs ",  font=font_big), sg.Text(
                        "0.00", key="Bal", font=font_big)], ]
    layout = [
        [sg.Text("")],
        [sg.Frame("Money Droid",  frame_layout,
                  element_justification="c", size=(300, 120), title_location="n",  font=font_small)],
        [sg.Text("")],

        [sg.Button('Withdraw', size=(20, 3)),
         sg.Button('Deposit', size=(20, 3))],
        [sg.Text("")],
        [sg.Button('Bill Payment', size=(20, 3)), sg.Button(
            'Transfer Money', size=(20, 3))],
        [sg.Button('Transection History', size=(30, 2))],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Button('Logout', size=(30, 2))],
    ]

    return sg.Window('Money Droid - Main', layout, size=(
        400, 600), element_justification='center', resizable=True)


def Main(account):
    window = Window_Main()
    window.Finalize()
    window["Bal"].Update("%.2f" % (account.balance))
    window["Username"].Update(f"{account.username}")
    window["Acc_Num"].Update(f"{account.email}")

    while True:
        event, values = window.read()

        if event == "Withdraw":
            window.close()
            Withdraw_GUI.Withdraw(account)

        if event == "Transfer Money":
            window.close()
            Transfer_GUI.transfer(account)

        if event == "Bill Payment":
            window.close()
            Bill_Payment_GUI.PB(account)

        if event == "Deposit":
            window.close()
            Deposit_GUI.Deposit(account)
        if event == "Transection History":
            window.close()
            Trans_log_GUI.Trans_Log(account)
        if event == "Logout":
            window.close()
            Login_GUI.Login()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    window.close()


if __name__ == '__main__':
    Main()
