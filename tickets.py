import connexion
import menu

def ajout_tickets(id) :

    titre = connexion.demander_chaine_non_vide("Titre : ")
    description = connexion.demander_chaine_non_vide("Description : ")
    while True:
        niveau_urgence = input("Viveau d'urgence \nVeuillez saisir :\n1 . urgent\n2 . pas urgent")
        if niveau_urgence == '1' :
            niveau_urgence = 'urgent'
            break
        elif niveau_urgence == '2' :
            niveau_urgence = 'pas urgent'
            break
        else :
            print("Choix invalide!!!")

    requete = """INSERT INTO tickets (titre, description, niveau_urgence,id_utilisateur) VALUES (%s, %s, %s,%s)"""
    with connexion.conn.cursor() as curseur :
        curseur.execute(requete,(titre,description,niveau_urgence,id))
        connexion.conn.commit()
        print("Ticket ajoute avec succes!")


# ajout_tickets()
def afficher_ticket(user) :
    if user['profil'] == 'admin' :
        requete = """SELECT t.*, u.prenom prenom,u.nom nom FROM tickets t JOIN utilisateurs u ON u.id = t.id_utilisateur"""
        with connexion.conn.cursor(dictionary=True) as curseur :
            curseur.execute(requete,)
            tickets = curseur.fetchall()
    if user['profil'] == 'user' :
        id = user['id'] 
        requete = """SELECT t.*, u.prenom prenom,u.nom nom FROM tickets t JOIN utilisateurs u ON u.id = t.id_utilisateur WHERE u.id_utlisateur = %s"""
        with connexion.conn.cursor(dictionary=True) as curseur :
            curseur.execute(requete,)
            tickets = curseur.fetchall()
    if tickets != None:
        for ticket in tickets :
            print(f"ID : {ticket['id']} | DEMANDEUR :{ticket['prenom']} {ticket['nom']} | TITRE : {ticket['titre']} | DESCRIPTION : {ticket['description']} | ETAT : {ticket['etat']} | NIVEAU D'URGENCE : {ticket['niveau_urgence']}")
    else :
        print("Aucun tickets pour le moment")
# afficher_ticket()


def modifier_etat_ticket() :
    requete = """SELECT * FROM tickets WHERE etat = 'en attente' OR etat = 'en cours'"""
    with connexion.conn.cursor(dictionary=True) as curseur :
        curseur.execute(requete,)
        tickets = curseur.fetchall()
    if tickets is not None :
        for ticket in tickets :
            print(f"ID : {ticket['id']} | TITRE : {ticket['titre']} | DESCRIPTION : {ticket['description']} | ETAT : {ticket['etat']} | NIVEAU D'URGENCE : {ticket['niveau_urgence']}")

        id = connexion.demander_entier("Veillez entrer l'id du ticket dont vous voulez modifier l'etat : ")
        for ticket in tickets :
            if id == ticket['id'] :
                etat = ticket['etat']
                if ticket['etat'] == 'en attente' :
                    while True :
                        choix = connexion.demander_entier("Veuillez taper 1 pour le mettre en cours")
                        if choix == 1 :
                            etat = 'en cours'
                            break
                        else :
                            print("Choix invalide!!!")

                else :
                    while True :
                        choix = connexion.demander_entier("Veuillez taper 1 pour changer l'etat a termine")
                        if choix == 1 :
                            etat = 'termine'
                            break
                        else :
                            print("Choix invalide!!!")
            

                query_update = """UPDATE tickets SET etat = %s WHERE id = %s""" 
                with connexion.conn.cursor() as curseur :
                    curseur.execute(query_update,(etat,id))
                    connexion.conn.commit()
                    print("Etat mis a jour avec succes!")
                break
            else : 
                print("Ce tickt n'existe pas!!!")

    else :
        print("Aucun tickets pour le moment!!!")
                    

# modifier_etat_ticket()