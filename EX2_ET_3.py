import csv
import pickle
import os

# Les noms des fichiers et du répertoire de travail peuvent être modifiés ici, le reste du code suivra

# Récupère le répertoire de travail actuel
repertoire_travail = os.getcwd()

chemin_csv_charge = os.path.join(repertoire_travail, "csvetudiants.csv")
chemin_csv_a_charger = os.path.join(repertoire_travail, "csvacharger.csv")
chemin_pickle = os.path.join(repertoire_travail, "picklegroupe.pkl")

"""
- csvetudiants.csv sera utilisé pour sauvegarder les données des étudiants.
- csvacharger.csv sera utilisé pour charger et instancier des étudiants à partir d'un fichier CSV.
- picklegroupe.pkl sera utilisé pour sauvegarder et charger les données des groupes au format pickle.

Une fonction permet de les supprimer directement depuis ce script à la fin.
"""

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
        with open(chemin, "w", newline='', encoding='utf-8') as f:
            if self.etudiants:
                fieldnames = self.etudiants[0].to_dict().keys()
                # Objet DictWriter pour écrire l'en-tête du fichier CSV avec les noms de colonnes
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                # Écrit chaque étudiant dans le fichier CSV en utilisant la méthode to_dict() pour obtenir ses données sous forme de dictionnaire
                for student in self.etudiants:
                    writer.writerow(student.to_dict())

    @classmethod
    def charger_csv(cls, chemin):
        etudiants = []
        with open(chemin, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    etudiant_data = {
                        'nom': row['_nom'],
                        'annee_naissance': int(row['_annee_naissance']),
                        'gpa': float(row['_gpa']),
                        # Rend le test insensible à la casse peu importe si la valeur est écrite en majuscules, minuscules ou mixte
                        'connais_python': row['_connais_python'].lower() == 'true'
                    }
                    # Ajoute un nouvel objet Etudiant à la liste des étudiants en utilisant les données du dictionnaire créé
                    etudiants.append(Etudiant.from_dict(etudiant_data))
                except (ValueError, KeyError, TypeError) as e:
                    print(f"Erreur lors du chargement de l'étudiant: {e}")
        return cls(etudiants)

    def __str__(self):
        tous_etudiants = "\n".join(str(etudiant) for etudiant in self.etudiants)
        return f"\nEtudiants dans le groupe: \n{tous_etudiants}"

def sauvegarder_groupe_pickle(groupe, nom_fichier):
    with open(nom_fichier, "wb") as f:
        pickle.dump(groupe, f)


def charger_groupe_pickle(nom_fichier):
    with open(nom_fichier, "rb") as f:
        return pickle.load(f)

supp = False  #Suivre si supprimer_fichiers a été exécutée. Si oui, on exécute pas le reste.
def supprimer_fichiers(*chemins):
    global supp  # Déclaration de supp comme variable globale
    supp = False  # Réinitialisation de supp à False à chaque appel de la fonction
    for chemin in chemins:
        try:
            os.remove(chemin)
            print(f"Fichier {chemin} supprimé avec succès.")
        except FileNotFoundError:
            print(f"Le fichier {chemin} n'existe pas.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la suppression du fichier {chemin}: {e}")
    supp = True  # Modification de supp à True après la suppression des fichiers


# Exemples d'utilisation (mettre en commentaire la suppression des fichiers si pas besoin)
if __name__ == "__main__":

    supprimer_fichiers(chemin_pickle, chemin_csv_charge)

    if supp == False:
        e1 = Etudiant('Abdul', 2004, 3.0, True)
        e2 = Etudiant('Juliette', 2001, 3.9, True)
        e3 = Etudiant('Matthieu', 2006, 4.5, False)
        e4 = Etudiant('Sandra', 2001, 4.0, True)
        donnees_e5 = {'nom': 'Sarah', 'annee_naissance': 2004, 'gpa': 3.7, 'connais_python': False}
        e5 = Etudiant.from_dict(donnees_e5)
        donnees_e6 = {'nom': 'Pierre', 'annee_naissance': 2003, 'gpa': 3.0, 'connais_python': True}
        e6 = Etudiant.from_dict(donnees_e6)

        G1 = Groupe([e1, e2, e3, e4, e5, e6])

        # Charger depuis un fichier CSV
        G2 = Groupe.charger_csv(chemin_csv_a_charger)

        # Sauvegarder dans un fichier CSV
        G1.sauvegarder_csv(chemin_csv_charge)

        # Sauvegarder et charger depuis un fichier pickle, G3 sera identique à G1
        sauvegarder_groupe_pickle(G1, chemin_pickle)
        G3 = charger_groupe_pickle(chemin_pickle)

        print("\nAffichage des étudiants:\n")
        print(e1)
        print(e4)
        print(e6)
        print("-" * 50)

        print("\nAffichage des groupes:")
        print(G1)
        print(G2)
        print(G3)
        print("-" * 50)

    """
    Le choix entre le mode texte et le mode binaire pour le stockage de données dépend des exigences spécifiques de l'application. 
    Les fichiers texte offrent une facilité de lecture et d'édition, ainsi qu'une interchangeabilité et une structure standardisée, 
    mais peuvent occuper plus d'espace sur le disque et nécessiter des opérations de conversion lors du traitement des données. 
    En revanche, les fichiers binaires offrent une efficacité de stockage et de traitement supérieure, ainsi qu'une meilleure portabilité des données, 
    mais sont illisibles pour les humains et peuvent être moins compatibles avec d'autres applications ou systèmes. 
    Le choix entre les deux dépendra des compromis entre lisibilité, efficacité, portabilité et compatibilité requis par l'application.
    """






