import customtkinter as cst


class App(cst.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x250")
        self.title("User Entry")

        # Label
        cst.CTkLabel(self, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        cst.CTkLabel(self, text="Password:").grid(row=1, column=0, padx=10, pady=10)

        # Textbox (CTkEntry kullanımı)
        self.username_entry = cst.CTkEntry(self)
        self.username_entry.grid(row=0, column=1, padx=20, pady=20)

        self.password_entry = cst.CTkEntry(self, show="*")  # Şifreyi gizlemek için
        self.password_entry.grid(row=1, column=1, padx=20, pady=20)

        # Giriş Butonu
        button = cst.CTkButton(self, text="Giriş", command=self.giris)
        button.grid(row=2, column=1, padx=10, pady=10)

        # Sonuç Label'ı
        self.result_label = cst.CTkLabel(self, text="")
        self.result_label.grid(row=3, column=1, padx=10, pady=10)

    def giris(self):
        control_username = "admin"
        control_password = "pass123"

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == control_username and password == control_password:
            self.result_label.configure(text="Giriş Başarılı!", text_color="green")
            self.open_data_window()
            self.destroy()
        else:
            self.result_label.configure(text="Hatalı Giriş. Tekrar Deneyin.", text_color="red")

    def open_data_window(self):
        data_window = cst.CTk()
        data_window.geometry("400x300")
        data_window.title("Data Window")
        
        cst.CTkLabel(data_window, text="Hoşgeldiniz, admin!").pack(pady=20)
        cst.CTkLabel(data_window, text="Burada veriler görüntülenecek.").pack(pady=10)

        data_window.mainloop()


app = App()
app.mainloop()
