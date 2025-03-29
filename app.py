import customtkinter as cst


class App(cst.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x250",)
        self.title("User Entry")
       
        # Label
        label = cst.CTkLabel(self, text="Username:")
        label.grid(row=0, column=0, padx=10, pady=10)

        label = cst.CTkLabel(self, text="Password:")
        label.grid(row=1,column =0, padx=10,pady=10)

        # Textbox (CTkEntry kullanımı)
        textbox = cst.CTkEntry(self)
        textbox.grid(row=0, column=1, padx=20, pady=20)

        textbox = cst.CTkEntry(self)
        textbox.grid(row=1, column=1, padx=20, pady=20)

        #Buton
        button = cst.CTkButton(self,text="Giriş")
        button.grid(row=2,column=1, padx=10,pady=10)

    def giris(self):
        control_username = "admin"
        control_password = "pass123"

        if self.username == control_username and self.password == control_password:
            return True
        else:
            return False

app = App()
app.mainloop()









































