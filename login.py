import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import database
from tkinter import messagebox

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
        img = PhotoImage(file="images/scene-3.png")
        Label_img = ctk.CTkButton(master=window, image=img, text=None, hover=None, fg_color='transparent')
        Label_img.place(x=-460, y=-360)
        Label_img.configure(text='')

        label_title = ctk.CTkLabel(master=window, text="Bem Vindos!", font=("JetBrains mono", 20)).place(x=105, y=10)

        # frame-box to login
        login_frame = ctk.CTkFrame(master=window, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # frame widgets
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("JetBrains mono", 20)).place(x=85, y=5)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuário", width=300, font=("JetBrains mono", 14)).place(x=25, y=105)

        username_label = ctk.CTkLabel(master=login_frame, text="* Preencha o campo acima para continuar", text_color="orange", font=("JetBrains mono", 10)).place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, font=("JetBrains mono", 14), show="°").place(x=25, y=175)

        password_label = ctk.CTkLabel(master=login_frame, text="* Preencha o campo acima para continuar", text_color="orange", font=("JetBrains mono", 10)).place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre de mim!", font=("JetBrains mono", 10)).place(x=25, y=245)

        def login():
            message = messagebox.showinfo(title="Atenção!", message="Login realizado com sucesso!")

            pass

        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, hover_color='#275fcf', font=("JetBrains mono", 10), command=login).place(x=25, y=285)
        
        register_span = ctk.CTkLabel(master=login_frame, text="Ainda não tem uma conta?", font=("JetBrains mono", 10)).place(x=25, y=325)

        def Register_Screen():
            # go to register
            login_frame.pack_forget()

            # frame-box to register
            register_frame = ctk.CTkFrame(master=window, width=350, height=396)
            register_frame.pack(side=RIGHT)

            label = ctk.CTkLabel(master=register_frame, text="Cadastre-se!", font=("JetBrains mono", 20)).place(x=105, y=5)

            span = ctk.CTkLabel(master=register_frame, text="* Os campos abaixo são obrigatórios.", font=("Jetbrains mono", 10), text_color="gray").place(x=25, y=65)

            username_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Digite seu nome de usuário", width=300, font=("JetBrains mono", 14)).place(x=25, y=105)

            email_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Digte seu email", width=300, font=("JetBrains mono", 14)).place(x=25, y=145)

            password_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Crie uma senha", width=300, font=("JetBrains mono", 14), show="°").place(x=25, y=185)

            confirm_password_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Confirme sua senha", width=300, font=("JetBrains mono", 14), show="°").place(x=25, y=225)

            checkbox = ctk.CTkCheckBox(master=register_frame, text="Li e concordo.", font=("JetBrains mono", 10)).place(x=25, y=265)

            def back():
                # back to login
                register_frame.pack_forget()
                login_frame.pack(side=RIGHT)

                pass

            back_to_login = ctk.CTkButton(master=register_frame, text="Voltar para o login", hover_color='#275fcf', width=145, command=back).place(x=25, y=315)

            # save user
            def save_user():
                message = messagebox.showinfo(title="Atenção!", message="Usuário cadastrado com sucesso!")

                pass
            
            save_rg = ctk.CTkButton(master=register_frame, text="Cadastrar", fg_color='green', hover_color='#40A130', width=145, command=save_user).place(x=185, y=315)

            pass

        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se!", fg_color='green', hover_color='#40A130', width=150, command=Register_Screen , font=("JetBrains mono", 10)).place(x=175, y=325)

        pass

Application()                                              