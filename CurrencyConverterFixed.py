
import code
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import bs4 as bs
import requests
x = 0
y=0
def CurrencyConversion():
    FirstCurrency = ChosenStartingValue.get()
    SecondCurrency = ChosenEndingValue.get()
    Amount = UserInputOfAmount.get()
    global Code

    global ExchangeRateTable
    First = Currency_table.index(FirstCurrency)
    Second= Currency_table.index(SecondCurrency)
    if FirstCurrency == 'Wybierz wartość z listy...' or SecondCurrency == 'Wybierz wartość z listy...':
        messagebox.showinfo("Nie wybrałeś waluty","Wybierz Waluty z listy aby je przekonwertować")    
    if FirstCurrency != 'PLN':
    
        AmountPLN = float(Amount)*float(ExchangeRateTable[First-1])
   
    else: 
        AmountPLN = float(Amount)
    if SecondCurrency != 'PLN':
        ConvertedAmount = float(AmountPLN)/float(ExchangeRateTable[Second-1])
    else:
        ConvertedAmount = AmountPLN

    Spinboxvar2.set(round(ConvertedAmount, 2))
def Swap():
    One = UserInputOfAmount.get()
    Two = UserInputOfAmount2.get()
    Spinboxvar1.set(Two)
    Spinboxvar2.set(One)
window = Tk()
window.title("Currency Converter ")
window.geometry('800x600')


res = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/last/?format=xml').text
try:
    res.raise_for_status()
except:
    print('error %s' %res)

soup = bs.BeautifulSoup(res, 'xml')

SoupData = soup.find_all('Mid')
ExchangeRateTable = []
for i in SoupData:
    ExchangeRateTable.append(i.text )

SoupData = soup.find_all('Code')
Code = []
for i in SoupData:   
    Code.append(i.text)
SoupData = soup.find_all('Currency')
Currency_table = []
for i in SoupData:
    
    Currency_table.append(str(Code[y]) + " " + i.text)
    y = y+1
Currency_table.insert(0,"Wybierz wartość z listy...")
Currency_table.append("PLN polskie złote")
ExchangeRateTable.append("1")
ChosenEndingValue = StringVar()
ChosenStartingValue = StringVar()
ValueBox1 = ttk.Combobox(window,width = 40, textvariable = ChosenStartingValue)
ValueBox1['values'] = (Currency_table)
ValueBox1.current(0)
ValueBox1['state'] = 'readonly'
ValueBox1.grid(column=0,row=0,padx = 5, pady=5)



ValueBox2 = ttk.Combobox(window,width = 40, textvariable = ChosenEndingValue)
ValueBox2['values'] = (Currency_table)
ValueBox2.current(0)
ValueBox2['state'] = 'readonly'
ValueBox2.grid(column=1,row=0,padx=5, pady=5)

Spinboxvar1 = StringVar()
Spinboxvar1.set("0")
UserInputOfAmount = ttk.Spinbox(window,width = 40 ,from_=0.0, to=9999999.0, textvariable= Spinboxvar1)
UserInputOfAmount.grid(column= 0 , row = 1 )    
Spinboxvar2 = StringVar()
Spinboxvar2.set("0")
UserInputOfAmount2 = ttk.Spinbox(window,width = 40 ,from_=0.0, to=9999999.0, textvariable= Spinboxvar2)
UserInputOfAmount2.grid(column= 1 , row = 1 )

ExchangeButton = ttk.Button(window, text = "Convert", command = CurrencyConversion)
ExchangeButton.grid(column=0 , row = 3, pady = 5)
SwapButton = ttk.Button(window,text = "SWAP", command = Swap).grid(column = 0 , row =4 , pady = 5)
window.mainloop()