import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

login = ctk.CTk()
login.geometry("500x350")

def connexion():
    print("Welcome")

#on crée le mini cadrant et on le positionne
frame = ctk.CTkFrame(master = login)
frame.pack(padx = 60, pady = 20, fill = "both", expand = True)

label = ctk.CTkLabel(master=frame, text = "Se connecter" )
label.pack(padx = 12, pady = 12)

#champ de l'identifiant
champ_connexion = ctk.CTkEntry(master = frame, placeholder_text= "Identifiant")
champ_connexion.pack(pady = 12)

#champ du mdp
champ_mdp = ctk.CTkEntry(master = frame, placeholder_text= "Mot de passe", show = "*")
champ_mdp.pack(pady = 12)

#button de connexion
button_connection = ctk.CTkButton(master= frame, text = "Connexion", command = connexion)
button_connection.pack(padx = 12, pady = 12)

checkbox = ctk.CTkCheckBox(master= frame, text="Se souvenir de moi")
checkbox.pack(padx = 12, pady = 12)

login.mainloop()