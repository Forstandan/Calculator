import tkinter as tk

DIGITS_FONT_STYLE = ("Arial", 15)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)

BUTTON_FRAME_COLOR = "#161a20"
MISC_BUTTON_BACKGROUND = "#363e4c"
OPERATOR_BUTTON_BACKGROUND = "#0060e5"
BUTTON_BACKGROUND = "#242933"
FRAME_COLOR = "#161A20"
BUTTON_TEXT = "#a7b9d3"
CALCULATION_LABEL_BACKGROUND = "#20252e"
WHITE="#ffffff"
BROWN="#e28743"

class Interface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("240x430")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.currentExpression = ''
        self.totalExpression = ''

        self.window.configure(bg=FRAME_COLOR)

        self.labelFrame = self.createLabelFrame()
        self.bottomFrame = self.createBottomFrame()
        self.operatorFrame = self.createOperatorFrame()

        self.digitFrame1 = self.createDigitFrame()

        self.digitFrame2 = self.createDigitFrame()

        self.digitFrame3 = self.createDigitFrame()

        self.digitFrame4 = self.createDigitFrame()

        self.digitFrame5 = self.createDigitFrame()

        self.zeroButtonFrame = self.createZeroButtonFrame()
        self.decimalButtonFrame = self.createDecimalButtonFrame()

        self.createMiscButtons()
        self.createDigitButtons()
        self.createOperationButtons()

        self.totalLabel = self.createTotalLabel()
        self.inputLabel = self.createInputLabel()

    def createDigitButtons(self):
        num = 7
        for i in range(3):
            button = tk.Button(self.digitFrame2, text=num, font=('Proxima Nova', 20), bg=BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                               command=lambda x=num: self.addToExpression(str(x)))
            button.pack(side='left', padx=1.5, pady=0.5)
            num += 1

        num = 4
        for i in range(3):
            button = tk.Button(self.digitFrame3, text=num, font=('Proxima Nova', 20), bg=BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                               command=lambda x=num: self.addToExpression(str(x)))
            button.pack(side='left', padx=1.5, pady=0.5)
            num += 1

        num = 1
        for i in range(3):
            button = tk.Button(self.digitFrame4, text=num, font=('Proxima Nova', 20), bg=BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                               command=lambda x=num: self.addToExpression(str(x)))
            button.pack(side='left', padx=1.5, pady=0.5)
            num += 1

    def createOperationButtons(self):
        button = tk.Button(self.operatorFrame, text='÷', font=('Proxima Nova', 20), bg=OPERATOR_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                           command=lambda x='/': self.appendOperator(x))
        button.pack(padx=1.5, pady=1.5)

        button = tk.Button(self.operatorFrame, text='×', font=('Proxima Nova', 20), bg=OPERATOR_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                           command=lambda x='*': self.appendOperator(x))
        button.pack(padx=1.5, pady=1.5)

        button = tk.Button(self.operatorFrame, text='+', font=('Proxima Nova', 20), bg=OPERATOR_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                           command=lambda x='+': self.appendOperator(x))
        button.pack(padx=1.5, pady=1.5)

        button = tk.Button(self.operatorFrame, text='-', font=('Proxima Nova', 20), bg=OPERATOR_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                           command=lambda x='-': self.appendOperator(x))
        button.pack(padx=1.5, pady=1.5)

        button = tk.Button(self.operatorFrame, text='=', font=('Proxima Nova', 20), bg=OPERATOR_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                           command=self.evaluate)
        button.pack(padx=1.5, pady=1.5)

    def createMiscButtons(self):
        ac_button = tk.Button(self.digitFrame1, text="AC", font=('Proxima Nova', 20), bg=MISC_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                              command=self.clear)
        ac_button.pack(side='left', padx=1.5, pady=0.5)

        plus_minus_button = tk.Button(self.digitFrame1, text='⁺∕₋', font=('Proxima Nova', 20), bg=MISC_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                                      command=self.makeNegative)
        plus_minus_button.pack(side='left', padx=1.5, pady=0.5)

        backspace_button = tk.Button(self.digitFrame1, text='⌫', font=('Proxima Nova', 20), bg=MISC_BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                                     command=self.removeLastCharacter)
        backspace_button.pack(side='left', padx=1.5, pady=0.5)

        zero_button = tk.Button(self.zeroButtonFrame, text='0', font=('Proxima Nova', 20), bg=BUTTON_BACKGROUND, borderwidth=0, fg=BUTTON_TEXT,
                                command=lambda x=0: self.addToExpression(str(x)))
        zero_button.pack(side='left', fill='both', expand=True)

        decimal_button = tk.Button(self.decimalButtonFrame, text='.', font=('Proxima Nova', 20), bg=BUTTON_BACKGROUND, width=3, borderwidth=0, fg=BUTTON_TEXT,
                                   command=lambda x='.': self.addToExpression(x))
        decimal_button.pack(side='left', padx=2, pady=1)

    def evaluate(self):
        self.totalExpression += self.currentExpression
        self.updateTotalLabel()
        try:
            self.currentExpression = str(eval(self.totalExpression))

            self.totalExpression = ""
        except Exception as e:
            self.currentExpression = "Error"
        finally:
            self.updateInputLabel()

    def addToExpression(self, value):
        self.currentExpression += value
        self.updateInputLabel()

    def makeNegative(self):
        value = int(self.currentExpression)*-1
        self.currentExpression = ""
        self.updateInputLabel()
        self.currentExpression += str(value)
        self.updateInputLabel()

    def removeLastCharacter(self):
        self.currentExpression = self.currentExpression.rstrip(self.currentExpression[-1])
        if len(self.currentExpression) > 0:
            if self.currentExpression[len(self.currentExpression) - 1] == '-':
                self.currentExpression = self.currentExpression.rstrip(self.currentExpression[-1])
        self.updateInputLabel()

    def clear(self):
        self.currentExpression = ""
        self.totalExpression = ""
        self.updateInputLabel()
        self.updateTotalLabel()

    def updateInputLabel(self):
        self.inputLabel.config(text=self.currentExpression[:11])

    def updateTotalLabel(self):
        self.totalLabel.config(text=self.totalExpression[:11])

    def appendOperator(self, operator):
        self.currentExpression += operator
        self.totalExpression += self.currentExpression
        self.currentExpression = ""
        self.updateTotalLabel()
        self.updateInputLabel()

    def createTotalLabel(self):
        label = tk.Label(self.labelFrame, bg=CALCULATION_LABEL_BACKGROUND, height=1, font=SMALL_FONT_STYLE, fg=WHITE, anchor=tk.SE)
        label.pack(expand=True, fill='x', side='bottom')
        return label

    def createInputLabel(self):
        label = tk.Label(self.labelFrame, bg=FRAME_COLOR, height=1, font=LARGE_FONT_STYLE, fg=WHITE, anchor=tk.SE)
        label.pack(expand=True, fill='both')
        return label

    def createLabelFrame(self):
        frame = tk.Frame(self.window, height=140, bg=BUTTON_FRAME_COLOR)
        frame.pack_propagate(0)
        frame.pack(side="top", fill="x")
        return frame

    def createBottomFrame(self):
        frame = tk.Frame(self.window, bg=BUTTON_FRAME_COLOR)
        frame.pack(fill='both', expand=True)
        return frame

    def createDigitFrame(self):
        frame = tk.Frame(self.bottomFrame, bg=BUTTON_FRAME_COLOR, height=50, width=180)
        frame.pack(pady=1)
        return frame

    def createOperatorFrame(self):
        frame = tk.Frame(self.bottomFrame, bg=FRAME_COLOR, height=320, width=60)
        frame.pack_propagate(0)
        frame.pack(side='right', padx=1)
        return frame

    def createZeroButtonFrame(self):
        frame = tk.Frame(self.digitFrame5, bg=WHITE, height=50, width=112)
        frame.pack_propagate(0)
        frame.pack(side='left', expand=True, padx=3, pady=2)
        return frame

    def createDecimalButtonFrame(self):
        frame = tk.Frame(self.digitFrame5, bg=BUTTON_BACKGROUND, height=50, width=53)
        frame.pack_propagate(0)
        frame.pack(expand=True, padx=2)
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Interface()
    calc.run()
