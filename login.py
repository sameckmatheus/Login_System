import customtkinter as ve # pkg importation
from tkinter import * # pkg call
from PIL import Image, ImageTk # pkg mges support

# window-box setup
window = ve.CTk()

class Login():
    def __init__(self):
        self.theme()
        self.window()
        self.login_screen()
        
    def theme(self):
        ve.set_appearance_mode("dark")
        ve.set_default_color_theme("dark-blue")
        
    def window():
        window.geometry("700x400")
        window.title("Login")
        window.iconbitmap("favicon.ico")
        window.resizable(False, False)

    def login_screen():
        # img box-selector
        img = PhotoImage(file="images/log.png")
        Label_img = ve.CTkLabel(master=window, image=img)
        Label_img.place(x=25, y=65)
        Label_img.configure(text='')

        label_title = ve.CTkLabel(master=window, text="Bem Vindos!", font=("JetBrains mono", 20)).place(x=105, y=10)

        # frame-box in window-box setup
        login_frame = ve.CTkFrame(master=window, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # frame widgets
        label = ve.CTkLabel(master=login_frame, text="Sistema de Login", font=("JetBrains mono", 20))
        label.place(x=70, y=5)

        username_entry = ve.CTkEntry(master=login_frame, placeholder_text="Username", width=300, font=("JetBrains mono", 14)).place(x=25, y=105)

        username_label = ve.CTkLabel(master=login_frame, text="*Preencha o campo acima para continuar", text_color="orange", font=("JetBrains mono", 8)).place(x=25, y=135)

        password_entry = ve.CTkEntry(master=login_frame, placeholder_text="Password", width=300, font=("JetBrains mono", 14), show="°").place(x=25, y=175)

        password_label = ve.CTkLabel(master=login_frame, text="*Preencha o campo acima para continuar", text_color="orange", font=("JetBrains mono", 8)).place(x=25, y=205)

        checkbox = ve.CTkCheckBox(master=login_frame, text="Lembre de mim!", font=("JetBrains mono", 10)).place(x=25, y=245)

        login_button = ve.CTkButton(master=login_frame, text="Login", width=300, font=("JetBrains mono", 10)).place(x=25, y=305)

window.mainloop()                                                