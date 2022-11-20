### Chiffrement de César

# Importation des modules
import sys
import string

### Fonctions
def cesar(chaine, decalage):
    """Chiffrement de César"""
    alphabet = string.ascii_lowercase
    alphabet += alphabet.upper()
    chiffre = ""
    for lettre in chaine:
        if lettre in alphabet:
            chiffre += alphabet[(alphabet.index(lettre) + decalage) % len(alphabet)]
        else:
            chiffre += lettre
    return chiffre


### Programme principal
if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(cesar(sys.argv[1], int(sys.argv[2])))
    else:
        print("Usage: python cesar.py chaine decalage")
