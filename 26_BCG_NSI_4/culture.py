#############################################################################
# Jeux de données fournis                                                   #
#############################################################################
from plantes import Plante, plantes
from mesures import mesures

#############################################################################
# Écrire le code de la fonction croissance_moyenne de la question 1         #
#############################################################################


def croissance_moyenne(plantes):
    moy = []
    for i in range(len(plantes)):
        moy.append(plantes[i].croissance)
    return sum(moy) / len(moy)


#############################################################################
# Écrire le code de la fonction dictionnaire_mesure de la question 2      #
#############################################################################

def dictionnaire_mesure(plantes, mesures):
    dico_mesure = {}
    for i in range(len(plantes)):
        dico_mesure[plantes[i].nom] = []
        for y in range(len(mesures)):
            if plantes[i].nom == mesures[y]['plante']:
                dico_mesure[plantes[i].nom].append(mesures[y])
    return dico_mesure

#############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4     #
#############################################################################

def purger_mesures_extremes(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    for mesure in liste_mesures:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            liste_mesures.remove(mesure)
    """cette fonction suprime des données d'une liste quelle parcours ce qui crée l'erreur"""

def purger_mesures_extremes_corrigé(liste_mesures):
    liste_mesures_copy = liste_mesures.copy()
    for mesure in liste_mesures_copy:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            liste_mesures.remove(mesure)
    return liste_mesures

def test_purger():
    mesures_test = [
        {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
        {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
        {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
        {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
        {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]

    purger_mesures_extremes(mesures_test)

    print("Résultat après la purge :")
    for m in mesures_test:
        print(f"Jour {m['jour']} : {m['temperature']}°C")