import connexion
import utilisateur
import tickets

def menu_connexion() :
    while True :

        print("Veuillez taper ")
        print("1 . Connexion")
        print("2 . Inscription")
        print("0 . Quitter la programme")
        choix_saisi = connexion.demander_entier("\t : ")
        
        match choix_saisi :
            case 1 :
                user = utilisateur.login()
                return user
            case 2:
                utilisateur.inscription()
            case 0 :
                exit()
            case _:
                print("Choix invalide!!!")

def authentification_par_action(id) :
    requete = """SELECT profil FROM utilisateurs WHERE id = %s"""
    with connexion.conn.cursor() as curseur :
        curseur.execute(requete,(id,))
        profil = curseur.fetchone()
        print(profil)
        if profil[0] == 'admin' :

            return True
        else :
            return False   


def menu_principal(user) :
    while True:
        
        print('~'*20,'GESTION DES INCIDENTS','~'*20,'\n')

        print("Faites votre choix en fonction de ce que vous voulez faire")
        print("1 . Faire une Damande")
        print("2 . Voir la liste des Demandes")
        if user['profil'] == 'admin' :
            print("3 . Changer l'etat d'une demande")

        print("0 . Deconnexion")
        
        choix = input("\t : ")
        id = user['id']
        match choix :
            case '1' :
                tickets.ajout_tickets(id)
            case '2' : 
                tickets.afficher_ticket(user)
            case '3' :
                 if authentification_par_action(id):
                    tickets.modifier_etat_ticket()
            
            case '0' :
                user = ""
                menu_principal()