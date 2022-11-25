### Chiffrement de Vigenère

# Importation des modules
import sys
import string

### Fonctions
def decodevigenere(chaine, cle):
    """Chiffrement de Vigenère"""
    alphabet = string.ascii_uppercase
    chiffre = ""
    for i in range(len(chaine)):
        if chaine[i] in alphabet:
            chiffre += alphabet[(alphabet.index(chaine[i]) - alphabet.index(cle[i % len(cle)])) % len(alphabet)]
        else:
            chiffre += chaine[i]
    return chiffre

### Programme principal
if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(decodevigenere(sys.argv[1], sys.argv[2]))
    else:
        print("Usage: python decodevigenere.py chaine cle")
