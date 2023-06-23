import customtkinter # pkg importation
from tkinter import * # pkg call

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# window-box setup
window = customtkinter.CTk()
window.geometry("700x500")
window.title("Login")
window.iconbitmap("imges/favicon.ico")
window.resizable(False, False)

# img box-selector
img = PhotoImage(file="images/background.png")
Label_img = customtkinter.CTkLabel(master=window, image=img)
Label_img.place(x=5, y=65)



window.mainloop()