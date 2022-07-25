from weakref import finalize
import PySimpleGUI as sg
import App
from Exceptions import *
import Main_GUI
from SignUp import *
font_small = ("Arial", 13)
font_big = ("Arial", 15)
db = App.DB()


def Trans_Log_win(col_layout):

    layout = [
        [sg.Text("Transection History", font=font_big)],
        [sg.Column(col_layout, scrollable=True,
                   vertical_scroll_only=True, expand_x=True, expand_y=True, key="Col")],
    ]

    return sg.Window('Money Droid - Transection History', layout, size=(
        400, 600), element_justification='center', resizable=True)


def Trans_Log(account):
    col_layout = []
    for i in account.transection_log:
        # {"Type": transaction_type,
        #  "Amount": amount, "Purpose": purpose}

        col_layout.append([sg.Text(i["Type"], font=font_small)])
        col_layout.append([sg.Text(i["Amount"], font=font_small),
                           sg.Text("Rs", font=font_small)])
        col_layout.append([sg.Text(i["Purpose"])])
        col_layout.append([sg.HorizontalSeparator(color="White")])

    col_layout.append([sg.Button("Back", size=(10, 2), expand_x=True)])
    window = Trans_Log_win(col_layout)
    window.Finalize()

    while True:

        event, values = window.read()
        if event == "Back":
            window.close()
            Main_GUI.Main(account)
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()
