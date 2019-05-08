from firebase import FirestoreFactory
import subprocess
#Python Combobox Application  
import tkinter as tk  
from tkinter import ttk  
import logging as log

def run_thing(profile):
  print(profile)
  profile.build()
  profile.run_all()

def start_gui():
  win = tk.Tk()  
  #Application Name  
  win.title("Instaru")  
  win.resizable(0,0)
  #Label Creation  
  ttk.Label(win, text="Selecione Perfil").grid(column=0,row=0)  

  #Button Action  
  def click():  
    action.configure(text="Executando")
    run_thing(mydata.find_profile(action_button.get()))

  #button Creation  
  action = ttk.Button(win, text="Executar", command=click)  
  action.grid(column=1,row=1)  
  #Combobox Creation  
  number= tk.StringVar()  
  action_button= ttk.Combobox(win, width=12, textvariable=number)  
  #Adding Values  

  mydata = FirestoreFactory().build_collection()

  action_button['values']=(mydata.find_profile_for_this_os())  
  action_button.grid(column=0,row=1)  
  action_button.current()  
  #Calling Main()  
  win.mainloop() 