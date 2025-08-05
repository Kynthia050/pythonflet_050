import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1, on_click=None):
        super().__init__(text=text, expand=expand, on_click=on_click)


class DigitButton(CalcButton):
    def __init__(self, text, expand=1, on_click=None):
        super().__init__(text=text, expand=expand, on_click=on_click)
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text, on_click=None):
        super().__init__(text=text, on_click=on_click)
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.WHITE


class ExtraActionButton(CalcButton):
    def __init__(self, text, on_click=None):
        super().__init__(text=text, on_click=on_click)
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.color = ft.Colors.BLACK


class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()

        self.current_input = ""
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=32)

        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),
                ft.Row(
                    controls=[
                        ExtraActionButton("AC", on_click=self.button_clicked),
                        ExtraActionButton("+/-", on_click=self.button_clicked),
                        ExtraActionButton("%", on_click=self.button_clicked),
                        ActionButton("/", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("7", on_click=self.button_clicked),
                        DigitButton("8", on_click=self.button_clicked),
                        DigitButton("9", on_click=self.button_clicked),
                        ActionButton("*", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("4", on_click=self.button_clicked),
                        DigitButton("5", on_click=self.button_clicked),
                        DigitButton("6", on_click=self.button_clicked),
                        ActionButton("-", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("1", on_click=self.button_clicked),
                        DigitButton("2", on_click=self.button_clicked),
                        DigitButton("3", on_click=self.button_clicked),
                        ActionButton("+", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("0", expand=2, on_click=self.button_clicked),
                        DigitButton(".", on_click=self.button_clicked),
                        ActionButton("=", on_click=self.button_clicked),
                    ]
                ),
            ]
        )

    def button_clicked(self, e):
        text = e.control.text

        if text == "AC":
            self.current_input = ""
            self.result.value = "0"

        elif text == "=":
            try:
                expression = self.current_input.replace("×", "*").replace("÷", "/")
                value = eval(expression)
                self.result.value = str(value)
                self.current_input = str(value)
            except Exception:
                self.result.value = "Error"
                self.current_input = ""

        elif text == "+/-":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.result.value = self.current_input

        elif text == "%":
            try:
                value = float(self.current_input) / 100
                self.current_input = str(value)
                self.result.value = self.current_input
            except:
                self.result.value = "Error"
                self.current_input = ""

        else:
            self.current_input += text
            self.result.value = self.current_input

        self.update()


def main(page: ft.Page):
    page.title = "Cal App"
    calc = CalculatorApp()
    page.add(calc)


ft.app(target=main)
