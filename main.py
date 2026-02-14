import menu



user = menu.menu_connexion()
print(f"Bienvenue {user ['prenom']} {user['nom']}")
menu.menu_principal(user)