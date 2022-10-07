
from tkinter import *
from tkinter import ttk
import operator
from tkinter import messagebox
operators={
    "+": operator.add,
    "-": operator.sub,
}

def DodajalboOdejmij():
    FirstNumber = float(Value1.get())
    SecondNumber = float(Value2.get())
    MinusPlus = PlusorMinus.get()
    if MinusPlus == 'Wybierz operator':
        messagebox.showinfo("Nie wybrałeś waluty","Wybierz Waluty z listy aby je przekonwertować")   
        return 0
    wynik = operators[MinusPlus](FirstNumber, SecondNumber)
    wyniknaekranie['text'] = 'Wynik: ',wynik
 
window = Tk()
window.title("Add or not ")
window.geometry('800x600')
PlusorMinus = StringVar()
Value1 = StringVar()
Value2 = StringVar()
UserInput1 = ttk.Spinbox(window,width = 40 ,from_=0.0, to=9999999.0, textvariable= Value1)
UserInput1.grid(column= 1 , row = 0 )  
UserInput2 = ttk.Spinbox(window,width = 40 ,from_=0.0, to=9999999.0, textvariable= Value2)
UserInput2.grid(column= 2 , row = 0 )

Startbutton = ttk.Button(window, text = "Oblicz", command = DodajalboOdejmij)
Startbutton.grid(column=2 , row = 3, pady = 5)


ValueBox2 = ttk.Combobox(window,width = 40, textvariable = PlusorMinus)
ValueBox2['values'] = ["Wybierz operator","+","-"]
ValueBox2.set(0)
ValueBox2.current(0)
ValueBox2['state'] = 'readonly'
ValueBox2.grid(column=1,row=3,padx=5, pady=5)
Value1.set("0")
Value2.set("0")
wyniknaekranie = ttk.Label(window, text ='Wynik:' )
wyniknaekranie.grid(column=1, row=4)



window.mainloop()
