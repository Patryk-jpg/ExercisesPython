from tkinter import *
from tkinter import messagebox
import mysql.connector
from functools import partial
import tkinter as tk
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  password = '',
  database = 'pythonlogin'
)
cursor = dataBase.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS dane(id_dane integer primary key AUTO_INCREMENT,login VARCHAR(10), passwd VARCHAR(15))")
cursor.execute("CREATE TABLE IF NOT EXISTS kontakt(id_kontakt integer primary key AUTO_INCREMENT,id_dane integer unique, imie VARCHAR(10), nazwisko VARCHAR(15),ulica varchar(10),Mieszkanie	varchar(10),Kod_i_miasto varchar(10),nr_telefonu varchar(15),email varchar(20),wiek	int(3))")
dataBase.commit()
window = tk.Tk()
app = Frame(window) 
app.pack()                 
window.geometry('600x600')  
window.title('login')   
def RegisterData():
    haslo = passwddata.get()
    powtorkahasla = passwdCheck.get()
    cursor.execute(f"SELECT login FROM dane WHERE login = '{logindata.get()}'")
    isindatabase =   cursor.fetchall()
    if isindatabase:
        logindata.set('')
        passwdCheck.set('')
        passwddata.set('')
        tk.Label(app,text = 'Użytkownik o takim loginie już istnieje').pack()
        return
    if powtorkahasla != haslo:
        passwdCheck.set('')
        passwddata.set('')
        Label = tk.Label(app,text = "Hasła nie zgadzają się ze sobą spróbuj ponownie")
        Label.pack()   
        return
    if len(powtorkahasla) < 8:
        passwdCheck.set('')
        passwddata.set('')
        Label = tk.Label(app,text = "Hasło musi mieć co najmniej 8 znaków!")
        Label.pack()
        return
    if powtorkahasla == haslo:
        query = f"INSERT INTO dane VALUES(default,'{logindata.get()}','{passwddata.get()}');"
        print(query)
        cursor.execute(query)
        dataBase.commit()
        reset()
        Label1 = tk.Label(app,text='Dziękujemy za rejestrację!!!')
        Label1.pack()    

def reset():
    for child in app.winfo_children():

        child.destroy()
def FormularzDoRejestracji():
    reset()
    login = tk.Entry(app, text='Wpisz login', textvariable= logindata, width= 15)
    passwd = tk.Entry(app, text = 'Wpisz hasło' ,textvariable= passwddata,show = '*')
    passwd_check = tk.Entry(app,text="Potwierdź hasło", textvariable= passwdCheck,show = '*')
    login.pack()
    passwd.pack()
    passwd_check.pack()
    wyslijRejestracje = tk.Button(app, text = 'Wyślij', command=RegisterData)
    wyslijRejestracje.pack()
def zalogujsie():
    query = f"SELECT id_dane,login,passwd FROM dane WHERE login = '{logowanie_login_data.get()}' and passwd = '{logowanie_login_passwd.get()}';"
    

    cursor.execute(query)
    myresult = cursor.fetchall()

    if myresult:
        secondquery = f"INSERT IGNORE INTO kontakt (id_kontakt,id_dane, imie, nazwisko, ulica, Mieszkanie, Kod_i_miasto, nr_telefonu, email, wiek) VALUES  (default, '{myresult[0][0]}', '','','','','','','','')"
        cursor.execute(secondquery)
        dataBase.commit()
        loggedin(myresult)
    else:
        logowanie_login_data.set('')
        logowanie_login_passwd.set('')
        tk.Label(app,text='Nie znaleziono takiego konta').pack()
def FormularzDoLogowania():
    reset()
    logowanie_login  = tk.Entry(app, textvariable= logowanie_login_data)
    logowanie_login_data.set('login')
    #logowanie_text =  tk.Label(app, text = 'Login').place(x=20, y = 20)
    logowanie_haslo = tk.Entry(app ,textvariable= logowanie_login_passwd)
    #haslo_text  = tk.Label(app, text = 'haslo').place(x = 50, y = 10)
    logowanie_login_passwd.set('haslo')
    zaloguj = tk.Button(app,text= 'Wyślij' , command = zalogujsie)
    
    logowanie_login.pack()
    logowanie_haslo.pack()
    zaloguj.pack()

def loggedin(myresult):
    reset()
    print(myresult)
    x,y,z = myresult[0]
    tk.Label(app,text=f'Witaj {y}').pack()
    Signin['state'] = DISABLED
    Register['state'] = DISABLED
  
    cursor.execute(f"select * from kontakt where id_dane ='{x}'")
    temp = ['skip', 'twoje id', 'imie', 'nazwisko','ulica','mieszkanie','kod i miasto', 'numer telefonu','email','wiek']
    c = 0
    data = cursor.fetchall()

    entry_list = []
    for i in data[0]: 
        if c == 0:
            c+=1
            continue   
        tk.Label(app, text=temp[c]).pack()
        my_ent = tk.Entry(app, text=f"Button {c}")
        my_ent.insert(0, i)
        my_ent.pack()
        entry_list.append(my_ent)
        c += 1
    LogoutBT = tk.Button(window, text='wyloguj się', command = partial(Logout, entry_list), width= 15, height= 2)
    LogoutBT.place(x = 10 , y = 100)
    Changebutt = tk.Button(app, command =  partial(modify, entry_list), text = 'Zapisz zmiany')
    Changebutt.pack()
    entry_list[0]['state'] = DISABLED
    
    
def modify(entry_list):
    
    print(entry_list) 
    valuesup = []
    for i in entry_list:
        valuesup.append(i.get())
    print(valuesup)
    finalquery = f"UPDATE kontakt set imie = '{valuesup[1]}',  nazwisko = '{valuesup[2]}', ulica = '{valuesup[3]}', Mieszkanie = '{valuesup[4]}', Kod_i_miasto = '{valuesup[5]}', nr_telefonu = '{valuesup[6]}', email = '{valuesup[7]}', wiek = '{valuesup[8]}' WHERE id_dane = '{valuesup[0]}'"
    cursor.execute(finalquery)
    print(finalquery)
    dataBase.commit()
    tk.Label(app, text= 'Zapisano zmiany').pack()
def Logout(entry_list):
    entry_list[0]['state'] = NORMAL
    for i in entry_list:
        i.delete(0, END)
    reset()
    Signin['state'] = NORMAL
    Register['state'] = NORMAL


Register = tk.Button(window, text='Zarejestruj się', command= FormularzDoRejestracji , width= 15, height= 2)
Register.place(x = 10, y=50)
Signin = tk.Button(window, text='Zaloguj się', command = FormularzDoLogowania, width= 15, height= 2)
Signin.place(x = 10 , y = 0)





logindata = StringVar()
passwddata= StringVar()
passwdCheck = StringVar()
logowanie_login_data = StringVar()
logowanie_login_passwd = StringVar()



window.mainloop()
# Disconnecting from the server
dataBase.close()
