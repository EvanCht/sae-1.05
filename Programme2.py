chemin_fichier = "ADE_RT1_Septembre2025_Decembre2025.ics"

def ouvrir_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()

    lignes = contenu.splitlines()
    
    tmp = []
    for l in lignes:
        if "BEGIN:VEVENT" in ligne:
        