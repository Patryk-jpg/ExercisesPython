from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter as tk
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  password = '',
  database = 'testing'
)

cursor = dataBase.cursor()
window = tk.Tk()
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
    login = tk.Entry(app, text='Wpisz login', textvariable= logindata)
    passwd = tk.Entry(app, text = 'Wpisz hasło' ,textvariable= passwddata,show = '*')
    passwd_check = tk.Entry(app,text="Potwierdź hasło", textvariable= passwdCheck,show = '*')
    login.pack()
    passwd.pack()
    passwd_check.pack()
    wyslijRejestracje = tk.Button(app, text = 'Send', command=RegisterData)
    wyslijRejestracje.pack()
def zalogujsie():
 
    query = f"SELECT login,passwd FROM dane WHERE login = '{logowanie_login_data.get()}' and passwd = '{logowanie_login_passwd.get()}';"
    print(query)
    cursor.execute(query)
    myresult = cursor.fetchall()
    if myresult:
        x,y = myresult[0]
        tk.Label(app,text=f'Witaj {x}').pack()
    else:
        logowanie_login_data.set('')
        logowanie_login_passwd.set('')
        tk.Label(app,text='Nie znaleziono takiego konta').pack()
def FormularzDoLogowania():
    reset()
    logowanie_login  = tk.Entry(app, text='Wpisz login', textvariable= logowanie_login_data)
    logowanie_haslo = tk.Entry(app, text = 'Wpisz hasło' ,textvariable= logowanie_login_passwd)
    zaloguj = tk.Button(app,text= 'Send' , command = zalogujsie)
    zaloguj.pack()
    logowanie_login.pack()
    logowanie_haslo.pack()

app = Frame(window) 
app.pack()                 
window.geometry('600x600')  
window.title('login')               

Register = tk.Button(window, text='Zarejestruj się', command= FormularzDoRejestracji)
Register.pack()
Signin = tk.Button(window, text='Zaloguj się', command = FormularzDoLogowania)
Signin.pack()



print(dataBase)

logindata = StringVar()
passwddata= StringVar()
passwdCheck = StringVar()
logowanie_login_data = StringVar()
logowanie_login_passwd = StringVar()



window.mainloop()
# Disconnecting from the server
dataBase.close()
