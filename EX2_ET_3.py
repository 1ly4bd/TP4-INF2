import csv
import pickle
import os

class Etudiant:
    def __init__(self, nom: str, annee_naissance: int, gpa: float, connais_python: bool):
        self.nom = nom
        self.annee_naissance = annee_naissance
        self.gpa = gpa
        self.connais_python = connais_python

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, n):
        if not isinstance(n, str):
            raise TypeError("Le nom doit être une chaîne de caractères")
        self._nom = n

    @property
    def annee_naissance(self):
        return self._annee_naissance

    @annee_naissance.setter
    def annee_naissance(self, a):
        if not isinstance(a, int):
            raise TypeError("L'année de naissance doit être un entier")
        if a < 2000 or a > 2006:
            raise ValueError("L'année de naissance doit être comprise entre 2000 et 2006")
        self._annee_naissance = a

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, a):
        if not isinstance(a, float):
            raise TypeError("Le GPA doit être un nombre flottant")
        if a < 0 or a > 5:
            raise ValueError("Le GPA doit être compris entre 0 et 5")
        self._gpa = a

    @property
    def connais_python(self):
        return self._connais_python

    @connais_python.setter
    def connais_python(self, a):
        if not isinstance(a, bool):
            raise TypeError("La connaissance de Python doit être un booléen")
        self._connais_python = a

    def to_dict(self):
        # Utilise la fonction vars() pour récupérer un dictionnaire contenant les attributs de l'objet
        return vars(self)

    @classmethod
    def from_dict(cls, donnees):
        # Utilise le constructeur de classe pour créer une nouvelle instance de la classe Etudiant en utilisant les données fournies sous forme de dictionnaire
        return cls(**donnees)

    def __str__(self):
        connais_python_str = "Oui" if self.connais_python else "Non"
        return f"Nom: {self.nom} - Année de naissance: {self.annee_naissance} - GPA: {self.gpa} - Connais python: {connais_python_str}"

class Groupe:
    def __init__(self, etudiants: list[Etudiant]):
        self.etudiants = etudiants

    @property
    def etudiants(self):
        return self._etudiants

    @etudiants.setter
    def etudiants(self, l):
        if not isinstance(l, list):
            raise TypeError("Les étudiants doivent être fournis sous forme de liste")
        self._etudiants = l

    def sauvegarder_csv(self, chemin):
        # Ouvre un fichier CSV en mode écriture
        with open(chemin, "w", newline='', encoding='utf-8') as f:
            # Vérifie s'il y a des étudiants à sauvegarder
            if self.etudiants:
                # Récupère les noms de colonnes à partir du premier étudiant
                fieldnames = self.etudiants[0].to_dict().keys()
                # Crée un objet DictWriter pour écrire dans le fichier CSV avec les noms de colonnes récupérés
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                # Écrit l'en-tête du fichier CSV avec les noms de colonnes
                writer.writeheader()
                # Écrit chaque étudiant dans le fichier CSV en utilisant la méthode to_dict() pour obtenir ses données sous forme de dictionnaire
                for student in self.etudiants:
                    writer.writerow(student.to_dict())

    @classmethod
    def charger_csv(cls, chemin):
        etudiants = []  # Liste pour stocker les étudiants chargés depuis le fichier CSV
        # Ouvre le fichier CSV en mode lecture
        with open(chemin, newline='', encoding='utf-8') as f:
            # Crée un lecteur CSV basé sur le fichier ouvert
            reader = csv.DictReader(f)
            # Parcourt chaque ligne du fichier CSV
            for row in reader:
                try:
                    # Crée un dictionnaire contenant les données de l'étudiant à partir de la ligne actuelle du fichier CSV
                    etudiant_data = {
                        'nom': row['_nom'],
                        'annee_naissance': int(row['_annee_naissance']),
                        'gpa': float(row['_gpa']),
                        # Rendre le test insensible à la casse peu importe si la valeur est écrite en majuscules, minuscules ou mixte
                        'connais_python': row['_connais_python'].lower() == 'true' #
                    }
                    # Ajoute un nouvel objet Etudiant à la liste des étudiants en utilisant les données du dictionnaire créé
                    etudiants.append(Etudiant.from_dict(etudiant_data))
                # Gère les erreurs potentielles lors de la création de l'objet Etudiant à partir des données du fichier CSV
                except (ValueError, KeyError, TypeError) as e:
                    print(f"Erreur lors du chargement de l'étudiant: {e}")
        # Retourne une nouvelle instance de la classe Groupe contenant les étudiants chargés depuis le fichier CSV
        return cls(etudiants)

    def __str__(self):
        tous_etudiants = "\n".join(str(etudiant) for etudiant in self.etudiants)
        return f"\nEtudiants dans le groupe: \n{tous_etudiants}"

def sauvegarder_groupe_pickle(groupe, nom_fichier):
    # Ouvre un fichier binaire en mode écriture pour la sauvegarde des données en format pickle
    with open(nom_fichier, "wb") as f:
        # Utilise pickle.dump() pour sauvegarder l'objet groupe dans le fichier
        pickle.dump(groupe, f)


def charger_groupe_pickle(nom_fichier):
    # Ouvre un fichier binaire en mode lecture pour charger les données en format pickle
    with open(nom_fichier, "rb") as f:
        # Utilise pickle.load() pour charger l'objet groupe depuis le fichier
        return pickle.load(f)


# Exemples d'utilisation
if __name__ == "__main__":
    e1 = Etudiant('Abdul', 2004, 3.0, True)
    e2 = Etudiant('Juliette', 2001, 3.9, True)
    e3 = Etudiant('Matthieu', 2006, 4.5, False)
    e4 = Etudiant('Sandra', 2001, 4.0, True)
    donnees_e5 = {'nom': 'Sarah', 'annee_naissance': 2004, 'gpa': 3.7, 'connais_python': False}
    e5 = Etudiant.from_dict(donnees_e5)
    donnees_e6 = {'nom': 'Pierre', 'annee_naissance': 2003, 'gpa': 3.0, 'connais_python': True}
    e6 = Etudiant.from_dict(donnees_e6)

    G1 = Groupe([e1, e2, e3, e4, e5, e6])

    # Chemin relatif pour les fichiers CSV et pickle
    path = os.getcwd()

    # Charger depuis un fichier CSV
    G2 = Groupe.charger_csv(os.path.join(path, "csvacharger.csv"))

    # Sauvegarder dans un fichier CSV
    G1.sauvegarder_csv(os.path.join(path, "etudiants.csv"))

    # Sauvegarder et charger depuis un fichier pickle
    sauvegarder_groupe_pickle(G1, os.path.join(path, "picklegroupe.pkl"))
    G3 = charger_groupe_pickle(os.path.join(path, "picklegroupe.pkl"))

    #Affichage d'étudiants
    print(e1)
    print(e4)
    print(e6)

    # Affichage des groupes
    print(G1)
    print(G2)
    print(G3)

    """
    Le choix entre le mode texte et le mode binaire pour le stockage de données dépend des exigences spécifiques de l'application. 
    Les fichiers texte offrent une facilité de lecture et d'édition, ainsi qu'une interchangeabilité et une structure standardisée, 
    mais peuvent occuper plus d'espace sur le disque et nécessiter des opérations de conversion lors du traitement des données. 
    En revanche, les fichiers binaires offrent une efficacité de stockage et de traitement supérieure, ainsi qu'une meilleure portabilité des données, 
    mais sont illisibles pour les humains et peuvent être moins compatibles avec d'autres applications ou systèmes. 
    Le choix entre les deux dépendra des compromis entre lisibilité, efficacité, portabilité et compatibilité requis par l'application.
    """






