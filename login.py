import customtkinter as ctk # pkg importation
from tkinter import * # pkg call
from PIL import Image, ImageTk # pkg mges support

# window-box setup
window = ctk.CTk()

class Application():
    def __init__(self):
        self.window=window
        self.theme()
        Application.screen()
        Application.login_screen()
        window.mainloop()
        
    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
    def screen():
        window.geometry("700x400")
        window.title("Login")
        window.iconbitmap("favicon.ico")
        window.resizable(False, False)

    def login_screen():
        # img box-selector
        img = PhotoImage(file="images/log.png")
        Label_img = ctk.CTkButton(master=window, image=img, text=None, hover=None, fg_color='transparent')
        Label_img.place(x=25, y=65)
        Label_img.configure(text='')

        label_title = ctk.CTkLabel(master=window, text="Bem Vindos!", font=("JetBrains mono", 20)).place(x=105, y=10)

        # frame-box in window-box setup
        login_frame = ctk.CTkFrame(master=window, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # frame widgets
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("JetBrains mono", 20)).place(x=70, y=5)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username", width=300, font=("JetBrains mono", 14)).place(x=25, y=105)

        username_label = ctk.CTkLabel(master=login_frame, text="* Preencha o campo acima para continuar", text_color="orange", font=("JetBrains mono", 10)).place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Password", width=300, font=("JetBrains mono", 14), show="°").place(x=25, y=175)

        password_label = ctk.CTkLabel(master=login_frame, text="* Preencha o campo acima para continuar", text_color="orange", font=("JetBrains mono", 10)).place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre de mim!", font=("JetBrains mono", 10)).place(x=25, y=245)

        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, font=("JetBrains mono", 10)).place(x=25, y=285)
        
        register_span = ctk.CTkLabel(master=login_frame, text="Ainda não tem uma conta?", font=("JetBrains mono", 10)).place(x=25, y=325)
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", fg_color='green', hover_color='#2D9334', width=150, font=("JetBrains mono", 10)).place(x=175, y=325)

Application()                                              