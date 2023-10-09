import PySimpleGUI as SG

SG.theme("Black")

STYLE = {"color": ('Black', 'AliceBlue'),
         "size": (6, 3),
         "font": ("Helvetica", 11, "bold"),
         "relief": SG.RELIEF_RIDGE}


def create_button(text: str, button_color: str = None) -> SG.Button:
    """ Creates a button """
    if not button_color:
        return SG.Button(button_text=text, button_color=STYLE["color"], size=STYLE["size"], font=STYLE["font"],
                         key=text)
    else:
        return SG.Button(button_text=text, button_color=button_color, size=STYLE["size"], font=STYLE["font"], key=text)


def create_column(button_one: SG.Button, button_two: SG.Button,
                  button_three: SG.Button, button_four: SG.Button) -> SG.Column:
    """ Creates and returns a colum of buttons """
    return SG.Column([[button_one], [button_two], [button_three], [button_four]])


button1 = create_button(text="1")
button2 = create_button(text="2")
button3 = create_button(text="3")
button4 = create_button(text="4")
button5 = create_button(text="5")
button6 = create_button(text="6")
button7 = create_button(text="7")
button8 = create_button(text="8")
button9 = create_button(text="9")
button0 = create_button(text="0")

button_plus = create_button(text="+")
button_minus = create_button(text="-")
button_divide = create_button(text="/")
button_multiply = create_button(text="*")

button_reset = create_button(text="R", button_color="Red")
button_equal = create_button(text="=", button_color="Green")

column1 = create_column(button7, button4, button1, button_reset)
column2 = create_column(button8, button5, button2, button0)
column3 = create_column(button9, button6, button3, button_equal)
column4 = create_column(button_plus, button_minus, button_multiply, button_divide)


WINDOW = SG.Window(title="Calculator", layout=[[column1, column2, column3, column4]])

mathematical_expression = ""

while True:
    event, _ = WINDOW.read()
    if event == SG.WIN_CLOSED:
        break
    else:
        mathematical_expression += event

        match event:
            case "=":
                result = eval(mathematical_expression[:-1])
                print(result)
                SG.popup(f"The result is: \n{result}", text_color="white", font=("Helvetica", 12, "bold"))
                mathematical_expression = ""
                continue
            case "R":
                mathematical_expression = ""
                continue

WINDOW.close()
