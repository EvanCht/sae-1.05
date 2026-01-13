#  Rapport d'Analyse Réseau - SAÉ1.05

##  Vue d'ensemble

**Nombre total de paquets analysés** : 5026

---

##   - Adresses IP Sources les plus actives

| Rang | Adresse IP | Nombre de paquets |
|------|-----------|-------------------|
| 1 | `BP-Linux8` | 2991 |
| 2 | `190-0-175-100.gba.solunet.com.ar` | 1969 |
| 3 | `192.168.190.130` | 66 |

---

##   - Adresses IP Destinations

| Rang | Adresse IP | Nombre de paquets |
|------|-----------|-------------------|
| 1 | `184.107.43.74` | 1969 |
| 2 | `www.aggloroanne.fr` | 1022 |
| 3 | `mauves.univ-st-etienne.fr` | 751 |
| 4 | `par10s38-in-f3.1e100.net` | 255 |
| 5 | `par21s23-in-f3.1e100.net` | 200 |
| 6 | `par21s17-in-f1.1e100.net` | 176 |
| 7 | `par21s23-in-f10.1e100.net` | 85 |
| 8 | `ns1.lan.rt` | 83 |
| 9 | `par21s04-in-f4.1e100.net` | 79 |
| 10 | `BP-Linux8` | 66 |

---

##  Répartition des Flags TCP

| Flag | Description | Nombre |
|------|-------------|--------|
| `.` | ACK - Accusé de réception | 2325 |
| `S` | SYN - Demande de connexion | 2015 |
| `P.` | Autre | 583 |
| `N/A` | Autre | 83 |
| `F.` | Autre | 20 |

---

##   - Ports Destination ciblés

| Rang | Port | Service | Nombre |
|------|------|---------|--------|
| 1 | `https` | HTTPS (443) | 2853 |
| 2 | `http` | HTTP (80) | 2024 |
| 3 | `domain` | domain | 83 |
| 4 | `ssh` | SSH (22) | 66 |

---

##  Conclusion

### Activités suspectes Potentiel :

1. **Scan de ports potentiel** : Si une IP source génère beaucoup de paquets SYN vers différents ports
2. **Attaque DDoS/DoS** : Si une IP destination reçoit un nombre anormal de requêtes

**Recommandation** : Analyser les IP présentant un trafic anormalement élevé.
