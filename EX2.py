import csv
import copy


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
            raise TypeError("nom doit etre un str")
        self._nom = n

    @property
    def annee_naissance(self):
        return self._annee_naissance

    @annee_naissance.setter
    def annee_naissance(self, a):
        if a < 2000 or a > 2006:
            raise ValueError("année impossible")
        if not isinstance(a, int):
            raise TypeError("l'année de naissance doit etre un int")
        self._annee_naissance = a

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, a):
        if a < 0 or a > 5:
            raise ValueError("gpa doit etre entre 0 et 5")
        if not isinstance(a, float):
            raise TypeError("le gpa doit etre un float")
        self._gpa = a

    @property
    def connais_python(self):
        return self._connais_python

    @connais_python.setter
    def connais_python(self, a):
        if not isinstance(a, bool):
            raise TypeError("doit etre un bool")
        self._connais_python = a

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(cls, donnees):
        return cls(**donnees)

    @staticmethod
    def charger_csv(chemin):
        etudiants = []
        with open(chemin, "r", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convertir chaque ligne du CSV en un dictionnaire d'étudiant
                etudiant_dict = {key.strip(): value for key, value in row.items()}
                etudiants.append(Etudiant.from_dict(etudiant_dict))
        return Groupe(etudiants)

class Groupe:
    def __init__(self, etudiants: list[Etudiant]):
        self.etudiants = etudiants

    @property
    def etudiants(self):
        return self._etudiants

    @etudiants.setter
    def etudiants(self, l):
        if not isinstance(l, list):
            raise TypeError("Il faut une liste d'étudiants")
        self._etudiants = l

    def sauvegarder_csv(self, chemin):
        with open(chemin, "w", newline='', encoding='utf-8') as f:
            if self.etudiants:
                # Obtenir les noms de champs et supprimer les underscores
                fieldnames = [field[1:] for field in self.etudiants[0].to_dict().keys()]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for student in self.etudiants:
                    # Modifier les clés du dictionnaire pour supprimer le underscore
                    modified_dict = {key[1:]: value for key, value in student.to_dict().items()}
                    writer.writerow(modified_dict)


e1 = Etudiant('abdul', 2004, 3.0, True)
e2 = Etudiant('juliette', 2001, 3.9, True)
e3 = Etudiant('matthieu', 2006, 4.5, False)
e4 = Etudiant('sandra', 2001, 4.0, True)
donnees_e5 = {'nom': 'sarah', 'annee_naissance': 2004, 'gpa': 3.7, 'connais_python': False}
e5 = Etudiant.from_dict(donnees_e5)
G1 = Groupe([e1, e2, e3, e4, e5])
path = r"C:\Users\Abdul\Desktop\UTC\TC04\INF2" #Copiez chemin du dossier où vous souhaitez entregistrer les fichiers
G1.sauvegarder_csv(path+r"\etudiants.csv")







    


