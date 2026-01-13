import re
import csv
from collections import Counter

def extraire_paquets(fichier_entree):
    """
    Cette fonction lit le fichier DumpFile.txt ligne par ligne
    et extrait les informations de chaque paquet réseau.
    
    Retourne une liste de dictionnaires, chaque dict = 1 paquet
    """
    paquets = []
    
    # Ouvrir le fichier en lecture
    with open(fichier_entree, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
    
    # Parcourir chaque ligne
    for ligne in lignes:
        # Ignorer les lignes hexadécimales (qui commencent par \t0x)
        if ligne.strip().startswith('0x'):
            continue
        
        # Pattern pour extraire : IP source > IP destination
        # Exemple : "190-0-175-100.gba.solunet.com.ar.3121 > 184.107.43.74.http"
        match = re.search(r'IP\s+([\w\.\-]+)\.(\d+)\s+>\s+([\w\.\-]+)\.(\w+):', ligne)
        
        if match:
            ip_source = match.group(1)
            port_source = match.group(2)
            ip_dest = match.group(3)
            port_dest = match.group(4)
            
            # Extraire l'heure (format : HH:MM:SS.microsec)
            match_time = re.search(r'(\d{2}:\d{2}:\d{2}\.\d+)', ligne)
            timestamp = match_time.group(1) if match_time else "N/A"
            
            # Extraire les flags TCP (ex: [S], [.], [F])
            match_flags = re.search(r'Flags\s+\[([^\]]+)\]', ligne)
            flags = match_flags.group(1) if match_flags else "N/A"
            
            # Extraire la longueur du paquet
            match_length = re.search(r'length\s+(\d+)', ligne)
            length = match_length.group(1) if match_length else "0"
            
            # Ajouter à la liste
            paquets.append({
                'timestamp': timestamp,
                'ip_source': ip_source,
                'port_source': port_source,
                'ip_dest': ip_dest,
                'port_dest': port_dest,
                'flags': flags,
                'length': length
            })
    
    return paquets

def generer_csv(paquets, fichier_sortie):
    """
    Prend la liste de paquets et génère un fichier CSV
    """
    # Définir les colonnes
    colonnes = ['timestamp', 'ip_source', 'port_source', 'ip_dest', 'port_dest', 'flags', 'length']
    
    # Écrire dans le CSV
    with open(fichier_sortie, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(paquets)
    
    print(f" Fichier CSV généré : {fichier_sortie}")
    print(f" Nombre de paquets analysés : {len(paquets)}")

# Exécution principale
if __name__ == "__main__":
    fichier_entree = "DumpFile.txt"
    fichier_sortie = "resultats_analyse.csv"
    
    print(" Analyse du fichier réseau en cours...")
    paquets = extraire_paquets(fichier_entree)
    generer_csv(paquets, fichier_sortie)
