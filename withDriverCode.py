from tkinter import *
from currency_converter import CurrencyConverter

app = Tk()
c = CurrencyConverter()
app.title('Конвертер валют')
app.configure(bg='lavender', padx=20, pady=20)

var1 = StringVar(app)
var2 = StringVar(app)
var1.set('Валюта')
var2.set('Валюта')

amountField1 = Entry(app)
amountField2 = Entry(app)

CurrenyCodes = ["USD", "EUR", "GBP", "JPY", "RUB", "CAD"]


def conversion():
    amount = float(amountField1.get())
    fromCurrency = var1.get()
    toCurrency = var2.get()

    calculate = round(c.convert(amount, fromCurrency, toCurrency), 3)
    result = amountField2.insert(0, str(calculate))


def clearAll():
    amountField1.delete(0, END)
    amountField2.delete(0, END)


if __name__ == '__main__':
    headlabel = Label(app, text='Конвертер валют', font=('Helvetica', 24, 'bold'), bg='lavender', fg='#4b0082').grid(
        row=0, column=1, padx=5, pady=5)
    label1 = Label(app, text="Сколько денег переводим: ", font=('Helvetica', 12, 'bold'), bg='lavender',
                   fg='#4b0082').grid(row=1, column=0)
    label2 = Label(app, text="Из какой валюты:", font=('Helvetica', 12, 'bold'), bg='lavender', fg='#4b0082').grid(
        row=2, column=0)
    label3 = Label(app, text="В какую валюту:", font=('Helvetica', 12, 'bold'), bg='lavender', fg='#4b0082').grid(row=3,
                                                                                                                  column=0)
    label4 = Label(app, text="После перевода вы получите:", font=('Helvetica', 12, 'bold'), bg='lavender',
                   fg='#4b0082').grid(row=5, column=0)

    amountField1.grid(row=1, column=1, ipadx=25)
    amountField2.grid(row=5, column=1, ipadx=25)

    FromCurrency_option = OptionMenu(app, var1, *CurrenyCodes).grid(row=2, column=1, ipadx=50)
    ToCurrency_option = OptionMenu(app, var2, *CurrenyCodes).grid(row=3, column=1, ipadx=50)

    buttonConvert = Button(app, text="Конвертировать", font=('Helvetica', '14', 'bold'),
                     highlightbackground='lightgreen', width=26, height=2, command=conversion).grid(row=4, column=1, padx=5, pady=5)
    buttonClear = Button(app, text="Очистить оба поля (!!!)", font=('Helvetica', '14', 'bold'),
                     highlightbackground='yellow', width=26, height=2, command=clearAll).grid(row=6, column=1, padx=5, pady=5)
    buttonQuit = Button(app, text='X Выход', font=('Helvetica', '14', 'bold'),
                     highlightbackground='red', width=10, height=2, command=app.destroy).grid(row=7, column=0, padx=5, pady=5)

    app.mainloop()
