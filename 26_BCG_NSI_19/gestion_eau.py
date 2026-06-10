# ------------------------------------
# gestion_eau.py
# Programme de contrôle des réservoirs
# ------------------------------------
from donnees import reservoirs

# Question 1 : écrire la fonction est_en_penurie


def est_en_penurie(reservoirs, nom_reservoir):
    for i in range(len(reservoirs)):
        if reservoirs[i]['nom'] == nom_reservoir:
            limite = (reservoirs[i]['volume']*100)/reservoirs[i]['capacite']
            if limite < 20:
                return True
            else:
                return False

# Question 2 : écrire la fonction volume_par_district


def volume_par_district(reservoirs):
    dico = {}
    for i in range(len(reservoirs)):
        dico[reservoirs[i]['district']] = []
    for i in range(len(reservoirs)):
        for keys in dico:
            if keys == reservoirs[i]['district']:
                dico[keys].append(reservoirs[i])
    return dico

# Question 3


def volume_moyen(reservoirs):
    """
    Renvoie le volume moyen d'eau disponible dans les réservoirs.
    """
    somme_totale = 0
    for r in reservoirs:
        somme_totale += r["volume"]
        """le problème vient de la ligne du bas"""
    moyenne = somme_totale / (len(reservoirs)-1)
    return moyenne

def volume_moyen_correction(reservoirs):
    moy_vol = []
    for i in range(len(reservoirs)):
        moy_vol.append(reservoirs[i]['volume'])
    return sum(moy_vol) / len(moy_vol)

# Question 4


def liste_districts(reservoirs):
    """
    Renvoie la liste des districts présents dans les données.
    """
    liste = []
    for r in reservoirs:
        if (r["district"] not in liste):
            liste.append(r["district"])
    return liste


def reservoirs_par_district(reservoirs):
    """
    Renvoie un dictionnaire associant chaque district à la liste
    des réservoirs qui s’y trouvent.
    """
    liste_rpd = {}
    for r in reservoirs:
        district = r["district"]
        if district not in liste_rpd:
            liste_rpd[district] = []
        liste_rpd[district].append(r)
    return liste_rpd


def districts_vulnerables(reservoirs):
    """il suffit juste de réinvoquer les anciennes fonctions"""