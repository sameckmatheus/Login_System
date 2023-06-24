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
img = PhotoImage(file="log.png")
Label_img = customtkinter.CTkLabel(master=window, image=img)
Label_img.place(x=5, y=5)

# frame-box in window-box setup
frame = customtkinter.CTkFrame(master=window, width=350, height=395)
frame.pack(side=RIGHT)

# frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", text_font=("JetBrains mono", 20))
label.place(x=25, y=5)

username_input = customtkinter.CTkEntry(master=frame, 
    placeholder_text="Username", 
    width=300, 
    text_font=("JetBrains mono", 14)).place(x=25, y=105)

username_label = customtkinter.CTkLabel(master=frame, 
    text="*Preencha o campo acima para continuar",
    text_color="blue", 
    text_font=("JetBrains mono", 8)).place(x=25, y=135)

window.mainloop()                                                