import PySimpleGUI as sg
import App
import Main_GUI
font_small = ("Arial", 12)
font_big = ("Arial", 15)


def PB_Win():
    frame_layout = [
        [sg.Text('Current balance', font=font_big)],
        [sg.Text("Rs ",  font=font_big), sg.Text(
            "0.00", font=font_big, key="Bal")],
    ]
    layout = [
        [sg.Text("")],

        [sg.Frame("Bill Payment", frame_layout, size=(300, 100),
                  element_justification="center", title_location="n", font=font_small)],
        [sg.Text("")],

        [sg.Text("", key="Notify")],
        [sg.Text("Bill Type")],
        [sg.Input("", size=(50, 3), justification='centre', key="Bill_Type")],
        [sg.Text("")],
        [sg.Text("Reference Number")],
        [sg.Input("", size=(50, 3), justification='centre', key="Ref_Num")],
        [sg.Text("")],
        [sg.Text("Amount")],
        [sg.Input("", size=(50, 3), justification='centre', key="Amount")],
        [sg.Text("")],
        [sg.Button("Pay", size=(30, 2))],
        [sg.Button("Back", size=(10, 2))],
    ]
    return sg.Window('Moneydroid - Bill Payment', layout, size=(
        400, 600), element_justification='center')


def PB(account):
    window = PB_Win()
    window.Finalize()

    db = App.DB()
    db.Load_Account(account)
    window["Bal"].Update("%.2f" % (db.account.balance))

    while True:
        # print(type(db.account.balance))

        event, values = window.read()
        # print(values)
        # print(event)
        filled = False
        if event == "Pay":
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
                    db.Pay_Bill(values["Bill_Type"],
                                values["Ref_Num"], values["Amount"])
                    window["Bal"].Update("%.2f" % (db.account.balance))
                    window["Notify"].Update(
                        "Transection successful", text_color="Light Green")

                except Exception as e:
                    window["Notify"].Update(f"{e}", text_color="Red")
        if event == "Back":
            window.close()
            Main_GUI.Main(account)

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    window.close()


if __name__ == '__main__':
    PB()
