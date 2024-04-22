import math
import copy
import os

# Récupérer le répertoire de travail actuel
repertoire_travail = os.getcwd()

# Chemins des fichiers d'entrée et de sortie
chemin_entree = os.path.join(repertoire_travail, "poème.txt")
chemin_sortie_resultat = os.path.join(repertoire_travail, "resultat.txt")
chemin_sortie_poeme_modifie = os.path.join(repertoire_travail, "poeme2.txt")

# Lire le contenu du fichier texte d'entrée
with open(chemin_entree, "r", encoding='utf-8') as fichier_entree:
    contenu_original = fichier_entree.read()

# Ponctuations à supprimer
ponctuations = (".", " !", ",", " ?")

# Créer une copie du contenu original
contenu_modifie = copy.deepcopy(contenu_original)

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

# Insérer un point dans la liste des longueurs de mots pour former un nombre
longueurs_mots.insert(1, ".")
nombre_obtenu = float("".join(longueurs_mots))

# Écrire les résultats dans le fichier de sortie
with open(chemin_sortie_resultat, "w", encoding='utf-8') as fichier_sortie:
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

# Écrire le texte modifié dans un fichier séparé
with open(chemin_sortie_poeme_modifie, "w") as fichier_sortie_poeme_modifie:
    fichier_sortie_poeme_modifie.write(contenu_modifie)
