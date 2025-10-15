"""Module d'encodage RLE (Run-Length Encoding) pour chaînes de caractères ASCII."""

#### Imports et définition des variables globales

# Obligatoire pour que la solution récursive fonctionne sur de grandes entrées
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # initialisations
    res = [ ]
    i = 0
    n = len(s)
    # parcours de la chaîne de caractères
    while i < n:
        c = s[i]
        nb = 1
        # comptage du nombre d'occurrences de c
        while i + 1 < n and s[i + 1] == c:
            nb += 1
            i += 1
        # ajout du tuple (c, nb) à la liste résultat
        res.append((c, nb))
        i += 1
    return res


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    c = s[0]
    nb = 1
    while nb < len(s) and s[nb] == c:
        nb += 1
    return [(c,nb)] + artcode_r(s[nb:])


#### Fonction principale


def main():
    """fonction principale de test"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
