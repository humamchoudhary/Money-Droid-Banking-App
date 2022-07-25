import PySimpleGUI as sg
from SignUp import Signup_Page
import Exceptions
import Login_GUI


def Sign_Win():

    layout = [
        [sg.Text("")],
        [sg.Image(source='logo.png')],
        [sg.Text("")],
        [sg.Text("", key="Notify")],
        [sg.Text("First name"), sg.Text("     "), sg.Text(
            "Middle name"), sg.Text("     "), sg.Text("Last name")],
        [sg.Input("", size=(16, 3), justification='centre', key="fname"), sg.Input("", size=(16, 3), key="mname",
                                                                                   justification='centre'), sg.Input("", size=(16, 3), key="lname", justification='centre')],
        [sg.Text("Username"), sg.Text("     "), sg.Text("      "),
         sg.Text("      "), sg.Text("Gender")],
        [sg.Input("", size=(25, 3), justification='centre', key="Username"),
         sg.Input("", size=(25, 3), justification='centre', key="GEND")],
        [sg.Text("Email")],
        [sg.Input("", size=(50, 3), key="Email", justification="center")],
        [sg.Text("Address")],
        [sg.Input("", size=(50, 3), key="Address", justification="center")],
        [sg.Text("     "), sg.Text("Password"), sg.Text("    "),
         sg.Text("   "), sg.Text("Confirm Password")],
        [sg.Input("", size=(25, 3), key="Password", justification="center", password_char="*"),
         sg.Input("", size=(25, 3), key="ConfPass", justification="center", password_char="*")],
        [sg.Text("")],
        [sg.Button('Sign Up', size=(30, 2))],
        [sg.Button('Login', size=(10, 2))],
    ]

    return sg.Window('Moneydroid - Sign Up', layout, element_justification="center", size=(
        400, 600), resizable=True)


def SignUp():
    signup = Signup_Page()
    window = Sign_Win()
    window.Finalize()
    while True:
        error = False

        event, values = window.read()
        filled = False
        # print(values)
        # print(event)
        if event == "Sign Up":
            for key in values:
                if values[key] == '':
                    window["Notify"].Update(
                        "Please fill all fields!", text_color="Red")
                    filled = False
                elif values["Password"] != values["ConfPass"]:
                    window["Notify"].Update(
                        "Passwords does not match", text_color="Red")
                else:
                    filled = True
            if filled:

                try:
                    if len(values["Password"]) <= 6:
                        raise Exceptions.InvalidPasswordError(
                            "Password to short!")
                    else:
                        signup.Regester(
                            values["fname"], values["mname"], values["lname"], values["Address"], values["GEND"], values["Email"], values["Username"], values["Password"])
                        window["Notify"].Update(
                            "Sign up successful", text_color="Red")
                        window.close()
                        Login_GUI.Login()

                except Exception as e:
                    window["Notify"].Update(f"{e}", text_color="Red")

        if event == "Login":
            window.close()
            Login_GUI.Login()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    window.close()


if __name__ == '__main__':
    SignUp()
