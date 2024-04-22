import csv

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
        return vars(self)

    @classmethod
    def from_dict(cls, donnees):
        return cls(**donnees)

    def __str__(self):
        if self.connais_python == True:
            c = "Oui"
        else:
            c = "Non"
        return f"Nom: {self.nom} - Année de naissance: {self.annee_naissance} - GPA: {self.gpa} - Connais python: {c}"


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
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for student in self.etudiants:
                    writer.writerow(student.to_dict())

    @classmethod
    def charger_csv(cls, chemin):
        etudiants = []
        with open(chemin, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                etudiant_data = {
                    'nom': row['_nom'],
                    'annee_naissance': int(row['_annee_naissance']),
                    'gpa': float(row['_gpa']),
                    'connais_python': row['_connais_python'].lower() == 'true'
                }
                etudiants.append(Etudiant.from_dict(etudiant_data))
        return cls(etudiants)

    def __str__(self):
        tous_etudiants = ""
        for etudiant in self.etudiants:
            tous_etudiants += "\n"+str(etudiant)
        return tous_etudiants



# Exemple d'utilisation
path = r"C:\Users\Abdul\Desktop\UTC\TC04\INF2\csvacharger.csv"
G2 = Groupe.charger_csv(path)
print(type(G2))


# Exemple d'utilisation
e1 = Etudiant('Abdul', 2004, 3.0, True)
e2 = Etudiant('Juliette', 2001, 3.9, True)
e3 = Etudiant('Matthieu', 2006, 4.5, False)
e4 = Etudiant('Sandra', 2001, 4.0, True)
donnees_e5 = {'nom': 'Sarah', 'annee_naissance': 2004, 'gpa': 3.7, 'connais_python': False}
e5 = Etudiant.from_dict(donnees_e5)
donnees_e6 = {'nom': 'Pierre', 'annee_naissance': 2003, 'gpa': 3.0, 'connais_python': True}
e6 = Etudiant.from_dict(donnees_e6)

G1 = Groupe([e1, e2, e3, e4, e5, e6])
print(G1)
print(G2)

# Spécifiez le chemin correct
path = r"C:\Users\Abdul\Desktop\UTC\TC04\INF2"
G1.sauvegarder_csv(path + r"\etudiants.csv")
