import connexion
import bcrypt



def inscription() :
    nom  = connexion.demander_chaine_non_vide("Veuillez saisir votre nom : ")
    prenom  = connexion.demander_chaine_non_vide("Veuillez saisir votre prenom : ")
    email = connexion.demander_mail()
    mot_de_passe = connexion.demander_mot_de_passe()
    mot_de_passe = connexion.hasher_mot_de_passe(mot_de_passe)
    requete = """INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"""
    with connexion.conn.cursor() as curseur :
        curseur.execute(requete,(nom,prenom,email,mot_de_passe))
        connexion.conn.commit()
        print("Utilsateur ajoute avec succes!")


def login() :
    while True :
        email = connexion.demander_mail()
        mot_passe = connexion.demander_mot_de_passe()
        # mot_passe = mot_passe.encode()
        
        requete = """SELECT * FROM utilisateurs WHERE email = %s"""
        with connexion.conn.cursor(dictionary=True) as curseur :
            curseur.execute(requete,(email,))
            user = curseur.fetchone()
            mot_de_passe = user['mot_de_passe']
        
        if bcrypt.checkpw(mot_passe.encode("utf-8"),mot_de_passe.encode("utf-8")) :
            return user
        else :
            print("Email ou mot de passe incorrect!!!")
    

# inscription()    