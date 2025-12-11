chemin_fichier = "evenementSAE_15_2025.ics"

def ouvrir_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()

    lignes = contenu.splitlines()

    for ligne in lignes:
        print(ligne)

ouvrir_fichier(chemin_fichier)