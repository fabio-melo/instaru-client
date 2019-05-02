from firebase import FirestoreFactory, FIRESTORE_URL
import subprocess
#Python Combobox Application  
import tkinter as tk  
from tkinter import ttk  

def run_thing(profile):
  print(profile)
  profile.build()
  profile.run_all()

def start_gui():
  win = tk.Tk()  
  #Application Name  
  win.title("Instaru ThinGUI")  
  #Label Creation  
  ttk.Label(win, text="Escolha o Perfil").grid(column=0,row=0)  

  #Button Action  
  def click():  
    action.configure(text="Executando Procedimento")
    run_thing(mydata.find_profile(action_button.get()))

  #button Creation  
  action = ttk.Button(win, text="Click", command=click)  
  action.grid(column=1,row=1)  
  #Combobox Creation  
  number= tk.StringVar()  
  action_button= ttk.Combobox(win, width=12, textvariable=number)  
  #Adding Values  

  mydata = FirestoreFactory().build_collection(FIRESTORE_URL)

  action_button['values']=(mydata.profile_list)  
  action_button.grid(column=0,row=1)  
  action_button.current()  
  #Calling Main()  
  win.mainloop() 