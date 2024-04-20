import math
import copy

with open(r"C:\Users\Abdul\Desktop\UTC\TC04\INF2\poème.txt", "r", encoding='utf-8') as f:
    contenu = f.read()
ponct = (".", " !", ",", " ?")
contenu2 = copy.deepcopy(contenu)
contenu2 = contenu2.replace("'", " ")
for p in ponct:
    contenu2 = contenu2.replace(p, "")
contenu3 = contenu2.split()
list_digits = []
for mot in contenu3:
    list_digits.append(str(len(mot)))
dico_digits = {}
for mot in contenu3:
    dico_digits[mot] = (len(mot))
list_digits.insert(1, ".")
digits = float("".join(list_digits))
print(digits)
print(digits/math.pi)
print(math.pi)

with open(r"C:\Users\Abdul\Desktop\UTC\TC04\INF2\resultat.txt", "w", encoding='utf-8') as f:
    f.write(f"Texte original:\n\n{contenu}"
            f"\n\n{"-"*50}\n\n"
            f"Nouveau texte après suppression des ponctuations et apostrophes:\n\n{contenu2}"
            f"\n\n{"-"*50}\n\n"
            f"Dictionaire avec la longueur de chaque mot:\n{dico_digits}"
            f"\n\n{"-"*50}\n\n"
            f"Listes des digits: {list_digits}"
            f"\n\n{"-"*50}\n\n"
            f"Pi déduit: {digits}"
            f"\n\n{"-"*50}\n\n"
            f"Rapport Pi déduit / Math.Pi: {digits/math.pi}")

with open(r"C:\Users\Abdul\Desktop\UTC\TC04\INF2\poeme2.txt", "w") as f:
    f.write(contenu2)



