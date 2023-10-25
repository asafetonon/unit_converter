from tkinter import *
from tkinter import messagebox

class ConverterApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("400x200")
        self.title("Conversor de Unidades")

        self.label1 = Label(self, text="Insira a temperatura em Celsius:")
        self.label1.pack()

        self.entry1 = Entry(self)
        self.entry1.pack()

        self.button1 = Button(self, text="Converter", command=self.converter_celsius)
        self.button1.pack()

        self.label2 = Label(self, text="")
        self.label2.pack()

    def converter_celsius(self):
        try:
            celsius = float(self.entry1.get())
            fahrenheit = celsius * 9/5 + 32
            self.label2.config(text=f"{celsius}°C é igual a {fahrenheit}°F")
        except ValueError:
            messagebox.showerror("Erro", "Insira um valor numérico.")

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()