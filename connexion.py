import mysql.connector
import getpass
import bcrypt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Binetougueye@2",
    database="gestion_incidents"
)



def demander_entier(message):
    while True :
        valeur = input (message)
        try :
            if int(valeur) >= 0 :
                return int(valeur)
        except (ValueError,TypeError) as e :
            print("Vous devez saisir un nombre entier positif!!!")


def demander_chaine_non_vide(message):
    while True:
        valeur = input(message).strip()
        if valeur == "" :
            print("Ce champs est obligatoire!!!")
        elif valeur.isdigit() :
            print("Ce champs ne doit pas contenir que des chiffres!!!")
        else :
            return valeur


def demander_mail() : 
    while True :
        valeur = demander_chaine_non_vide("Veuillez saisir votre email(example@gmail.com) : ")
        if '@' in valeur and '.' in valeur and ' ' not in valeur :
            return valeur
        else : 
            print("Erreur!!! Veuillez respecter le format!!!")


def demander_mot_de_passe() :
    motdepasse = getpass.getpass("Veuillez saisir un mot de passe : ").strip()
    if motdepasse == "" :
        print("Le mot de passe ne doit pas etre vide!!!")
    elif len(motdepasse) < 8 :
        print("Le mot de passe doit contenir au minimum huit(8) carateres!!!")
    else :
        return motdepasse


def hasher_mot_de_passe(mdp) :
    return bcrypt.hashpw(mdp.encode("utf-8"),bcrypt.gensalt())










