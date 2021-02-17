"""
Module Bonjour - (nom module)

(explication du module)
"""


def main():
    """
    année bissextile
    1 - si l'année est divisible par 4 et non par 100
    ou
    2 - si l'année est divisible par 400
    """
    annee = 1993
    if (annee % 4 == 0 and not annee % 100 == 0) or annee % 400 == 0:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()
