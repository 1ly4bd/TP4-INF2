import os
import math

# Les noms des fichiers et du répertoire de travail peuvent être modifiés ici, le reste du code suivra.

repertoire_travail = os.getcwd() # Récupère le répertoire de travail actuel

# Chemins des fichiers d'entrée et de sortie
chemin_entree = os.path.join(repertoire_travail, "poème.txt")
chemin_resultat = os.path.join(repertoire_travail, "resultat.txt")

"""
Le fichier `resultat.txt` contiendra une analyse du poème original, comprenant le texte original, 
une version modifiée sans ponctuations ni apostrophes, un dictionnaire des longueurs de chaque mot, 
une liste des longueurs de mots, un nombre déduit en fonction des longueurs des mots, 
et un rapport entre ce nombre et π.

Une fonction permet de le supprimer directement depuis ce script à la fin.
"""

# Fonction pour traiter le fichier texte
def traiter_fichier_texte():
    # Vérifier si le fichier de résultat existe déjà
    fichier_existe = os.path.exists(chemin_resultat)

    # Lire le contenu du fichier texte d'entrée
    with open(chemin_entree, "r", encoding='utf-8') as fichier_entree:
        contenu_original = fichier_entree.read()

    # Ponctuations à supprimer
    ponctuations = (".", " !", ",", " ?")

    # Créer une copie du contenu original
    contenu_modifie = contenu_original

    # Supprimer les apostrophes et les ponctuations du contenu modifié
    for ponctuation in ponctuations:
        contenu_modifie = contenu_modifie.replace(ponctuation, "")
    contenu_modifie = contenu_modifie.replace("'", " ")

    # Diviser le contenu modifié en mots
    mots = contenu_modifie.split()

    # Créer une liste contenant la longueur de chaque mot
    longueurs_mots = [str(len(mot)) for mot in mots]

    # Créer un dictionnaire avec chaque mot et sa longueur
    dictionnaire_longueurs_mots = {}
    for mot in mots:
        dictionnaire_longueurs_mots[mot] = len(mot)

    # Insérer un point dans la liste des longueurs de mots pour former un nombre, sans ca on a une valeur incorrect
    longueurs_mots.insert(1, ".")
    nombre_obtenu = float("".join(longueurs_mots))

    # Écrire les résultats dans le fichier de sortie
    with open(chemin_resultat, "w", encoding='utf-8') as fichier_sortie:
        fichier_sortie.write(f"Texte original:\n\n{contenu_original}"
                             f"\n\n{'-'*50}\n\n"
                             f"Nouveau texte après suppression des ponctuations et apostrophes:\n\n{contenu_modifie}"
                             f"\n\n{'-'*50}\n\n"
                             f"Dictionnaire avec la longueur de chaque mot:\n{dictionnaire_longueurs_mots}"
                             f"\n\n{'-'*50}\n\n"
                             f"Liste des longueurs de mots: {longueurs_mots}"
                             f"\n\n{'-'*50}\n\n"
                             f"Nombre déduit: {nombre_obtenu}"
                             f"\n\n{'-'*50}\n\n"
                             f"Rapport Nombre déduit / π : {nombre_obtenu/math.pi}")

        if fichier_existe:
            print(f"Fichier {chemin_resultat} modifié avec succès.")
        else:
            print(f"Fichier {chemin_resultat} créé avec succès.")


# Fonction pour supprimer le fichier
def supprimer_fichier(chemin):
    try:
        os.remove(chemin)
        print(f"Fichier {chemin} supprimé avec succès.")
    except FileNotFoundError:
        print(f"Le fichier {chemin} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression du fichier {chemin}: {e}")

if __name__ == "__main__": # Mettre en commentaire la fonction à ne pas exécuter
    # Appeler la fonction pour traiter le fichier texte
    traiter_fichier_texte()

    # Appel de la fonction pour supprimer le fichier créé
    supprimer_fichier(chemin_resultat)
