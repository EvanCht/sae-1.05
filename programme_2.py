import csv
from collections import Counter

def analyser_csv(fichier_csv):
    """
    Lit le CSV et calcule des statistiques
    """
    paquets = []
    
    with open(fichier_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        paquets = list(reader)
    
    # Statistiques
    total_paquets = len(paquets)
    
    # Top 10 IP sources les plus actives
    ip_sources = [p['ip_source'] for p in paquets]
    top_sources = Counter(ip_sources).most_common(10)
    
    # Top 10 IP destinations
    ip_dest = [p['ip_dest'] for p in paquets]
    top_dest = Counter(ip_dest).most_common(10)
    
    # Répartition des flags TCP
    flags = [p['flags'] for p in paquets]
    repartition_flags = Counter(flags).most_common()
    
    # Ports destination les plus ciblés
    ports = [p['port_dest'] for p in paquets]
    top_ports = Counter(ports).most_common(10)
    
    return {
        'total': total_paquets,
        'top_sources': top_sources,
        'top_dest': top_dest,
        'flags': repartition_flags,
        'ports': top_ports
    }

def generer_markdown(stats, fichier_sortie):
    """
    Génère un fichier Markdown avec les résultats
    """
    md_content = f"""#  Rapport d'Analyse Réseau - SAÉ1.05

##  Vue d'ensemble

**Nombre total de paquets analysés** : {stats['total']}

---

##   - Adresses IP Sources les plus actives

| Rang | Adresse IP | Nombre de paquets |
|------|-----------|-------------------|
"""
    
    for i, (ip, count) in enumerate(stats['top_sources'], 1):
        md_content += f"| {i} | `{ip}` | {count} |\n"
    
    md_content += f"""
---

##   - Adresses IP Destinations

| Rang | Adresse IP | Nombre de paquets |
|------|-----------|-------------------|
"""
    
    for i, (ip, count) in enumerate(stats['top_dest'], 1):
        md_content += f"| {i} | `{ip}` | {count} |\n"
    
    md_content += f"""
---

##  Répartition des Flags TCP

| Flag | Description | Nombre |
|------|-------------|--------|
"""
    
    flag_desc = {
        'S': 'SYN - Demande de connexion',
        'F': 'FIN - Fermeture de connexion',
        '.': 'ACK - Accusé de réception',
        'P': 'PUSH - Envoi immédiat',
        'R': 'RESET - Réinitialisation'
    }
    
    for flag, count in stats['flags']:
        desc = flag_desc.get(flag, 'Autre')
        md_content += f"| `{flag}` | {desc} | {count} |\n"
    
    md_content += f"""
---

##   - Ports Destination ciblés

| Rang | Port | Service | Nombre |
|------|------|---------|--------|
"""
    
    port_services = {
        'http': 'HTTP (80)',
        'https': 'HTTPS (443)',
        'ssh': 'SSH (22)',
        'ftp': 'FTP (21)'
    }
    
    for i, (port, count) in enumerate(stats['ports'], 1):
        service = port_services.get(port, port)
        md_content += f"| {i} | `{port}` | {service} | {count} |\n"
    
    md_content += """
---

##  Conclusion

### Activités suspectes Potentiel :

1. **Scan de ports potentiel** : Si une IP source génère beaucoup de paquets SYN vers différents ports
2. **Attaque DDoS/DoS** : Si une IP destination reçoit un nombre anormal de requêtes

**Recommandation** : Analyser les IP présentant un trafic anormalement élevé.
"""
    
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f" Rapport Markdown généré : {fichier_sortie}")

# Exécution
if __name__ == "__main__":
    fichier_csv = "resultats_analyse.csv"
    fichier_markdown = "rapport_analyse.md"
    
    print(" Calcul des statistiques...")
    stats = analyser_csv(fichier_csv)
    
    print(" Génération du rapport Markdown...")
    generer_markdown(stats, fichier_markdown)
    
    print("\n Analyse terminée !")
