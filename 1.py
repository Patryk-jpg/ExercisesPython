from tkinter import *
import mysql.connector
import tkinter as tk
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  database = 'pythonlogin'
)

cursor = dataBase.cursor()
window = tk.Tk()
def RegisterData():
    query = f"INSERT INTO dane VALUES(default,{logindata.get()},{passwddata.get()});"
    print(query)
    cursor.execute(query)
def reset():
    for child in app.winfo_children():
        child.destroy()
def FormularzDoRejestracji():
    reset()
    login = tk.Entry(app, text='Wpisz login', textvariable= logindata)
    passwd = tk.Entry(app, text = 'Wpisz hasło' ,textvariable= passwddata)
    login.pack()
    passwd.pack()
    wyslijRejestracje = tk.Button(app, text = 'Send', command=RegisterData)
    wyslijRejestracje.pack()

def FormularzDoLogowania():
    reset()
    logowanie_login  = tk.Entry(app, text='Wpisz login', textvariable= logowanie_login_data)
    logowanie_haslo = tk.Entry(app, text = 'Wpisz hasło' ,textvariable= logowanie_login_passwd)
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
logowanie_login_data = StringVar()
logowanie_login_passwd = StringVar()



window.mainloop()
# Disconnecting from the server
dataBase.close()