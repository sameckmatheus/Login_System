import customtkinter # pkg importation
from tkinter import * # pkg call
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# window-box setup
window = customtkinter.CTk()
window.geometry("700x400")
window.title("Login")
window.iconbitmap("favicon.ico")
window.resizable(False, False)

# img box-selector
img = PhotoImage(file="images/log.png")
Label_img = customtkinter.CTkLabel(master=window, image=img)
Label_img.place(x=25, y=65)
Label_img.configure(text='')

label_title = customtkinter.CTkLabel(master=window, text="Bem Vindos!", font=("JetBrains mono", 20)).place(x=105, y=10)

# frame-box in window-box setup
frame = customtkinter.CTkFrame(master=window, width=350, height=396)
frame.pack(side=RIGHT)

# frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", font=("JetBrains mono", 20))
label.place(x=70, y=5)

username_input = customtkinter.CTkEntry(master=frame, 
    placeholder_text="Username", 
    width=300, 
    font=("JetBrains mono", 14)).place(x=25, y=105)

username_label = customtkinter.CTkLabel(master=frame, 
    text="*Preencha o campo acima para continuar", 
    text_color="orange", 
    font=("JetBrains mono", 8)).place(x=25, y=135)

pass_input = customtkinter.CTkEntry(master=frame, 
    placeholder_text="Password", 
    width=300, 
    font=("JetBrains mono", 14)).place(x=25, y=175)

pass_label = customtkinter.CTkLabel(master=frame, 
    text="*Preencha o campo acima para continuar", 
    text_color="orange", 
    font=("JetBrains mono", 8)).place(x=25, y=205)

checkbox = customtkinter.CTkCheckBox(master=frame, 
    text="Lembre de mim!", 
    font=("JetBrains mono", 10)).place(x=25, y=245)

button = customtkinter.CTkButton(master=frame, 
    text="Login", 
    width=300, 
    font=("JetBrains mono", 10)).place(x=25, y=305)

# open window
window.mainloop()                                                