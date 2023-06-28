import customtkinter as ve # pkg importation
from tkinter import * # pkg call
from PIL import Image, ImageTk # pkg mges support

ve.set_appearance_mode("dark")
ve.set_default_color_theme("dark-blue")

# window-box setup
window = ve.CTk()
window.geometry("700x400")
window.title("Login")
window.iconbitmap("favicon.ico")
window.resizable(False, False)

# img box-selector
img = PhotoImage(file="images/log.png")
Label_img = ve.CTkLabel(master=window, image=img)
Label_img.place(x=25, y=65)
Label_img.configure(text='')

label_title = ve.CTkLabel(master=window, text="Bem Vindos!", font=("JetBrains mono", 20)).place(x=105, y=10)

# frame-box in window-box setup
frame = ve.CTkFrame(master=window, width=350, height=396)
frame.pack(side=RIGHT)

# frame widgets
label = ve.CTkLabel(master=frame, text="Sistema de Login", font=("JetBrains mono", 20))
label.place(x=70, y=5)

username_entry = ve.CTkEntry(master=frame, 
    placeholder_text="Username", 
    width=300, 
    font=("JetBrains mono", 14)).place(x=25, y=105)

username_label = ve.CTkLabel(master=frame, 
    text="*Preencha o campo acima para continuar", 
    text_color="orange", 
    font=("JetBrains mono", 8)).place(x=25, y=135)

password_entry = ve.CTkEntry(master=frame, 
    placeholder_text="Password", 
    width=300, 
    font=("JetBrains mono", 14), show="°").place(x=25, y=175)

password_label = ve.CTkLabel(master=frame, 
    text="*Preencha o campo acima para continuar", 
    text_color="orange", 
    font=("JetBrains mono", 8)).place(x=25, y=205)

checkbox = ve.CTkCheckBox(master=frame, 
    text="Lembre de mim!", 
    font=("JetBrains mono", 10)).place(x=25, y=245)

login_button = ve.CTkButton(master=frame, 
    text="Login", 
    width=300, 
    font=("JetBrains mono", 10)).place(x=25, y=305)

# open window
window.mainloop()                                                