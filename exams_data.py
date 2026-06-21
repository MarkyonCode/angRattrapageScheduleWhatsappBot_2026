# -*- coding: utf-8 -*-
"""
Programme des examens de rachat - Anglais 2
Semestre 3 (impairs) : Lundi 22 -> Mercredi 24 juin 2026
Semestre 4 (pairs)   : Jeudi 25 -> Samedi 27 juin 2026

Chaque examen est un dict avec :
- jour       : nom du jour en français
- date       : date ISO (YYYY-MM-DD) pour calculs
- heure_debut, heure_fin : heures (format 24h, entiers)
- code       : code EC (ex: "ANG 1361")
- matiere    : nom complet de la matière
- semestre   : 3 ou 4
- surveillants : liste des noms (info secondaire, optionnelle)
"""

EXAMS = [
    # ---------- SEMESTRE 3 ----------
    {
        "jour": "Lundi", "date": "2026-06-22", "heure_debut": 14, "heure_fin": 16,
        "code": "ANG 1361", "matiere": "Phonétique & Grammaire", "semestre": 3,
        "surveillants": ["Koukpossi", "Dovonou", "Toboula", "Ezin", "Egounleti", "Kottin"],
    },
    {
        "jour": "Lundi", "date": "2026-06-22", "heure_debut": 16, "heure_fin": 18,
        "code": "ANG 1362", "matiere": "Études de Romans", "semestre": 3,
        "surveillants": ["Seguedeme", "Abadame", "Aguessy", "Ahouangansi", "Houndjo", "Gbaguidi"],
    },
    {
        "jour": "Mardi", "date": "2026-06-23", "heure_debut": 10, "heure_fin": 12,
        "code": "ANG 1363", "matiere": "Langue appliquée et anglais de spécialité", "semestre": 3,
        "surveillants": ["Hindeme", "Kottin", "Dovonou", "Bodjrenou"],
    },
    {
        "jour": "Mardi", "date": "2026-06-23", "heure_debut": 12, "heure_fin": 14,
        "code": "ANG 1364", "matiere": "Traduction des Textes Spécialisés", "semestre": 3,
        "surveillants": ["Iwikotan", "Kottin", "Akpaca", "Toboula"],
    },
    {
        "jour": "Mardi", "date": "2026-06-23", "heure_debut": 14, "heure_fin": 16,
        "code": "ANG 1365", "matiere": "Recherche Scientifique", "semestre": 3,
        "surveillants": ["Iwikotan", "Sakpoliba", "Dovonou"],
    },
    {
        "jour": "Mercredi", "date": "2026-06-24", "heure_debut": 12, "heure_fin": 14,
        "code": "ANG 1366", "matiere": "Français et langue vivante étrangère", "semestre": 3,
        "surveillants": ["Ayena", "Sohoue", "Medenou"],
    },
    {
        "jour": "Mercredi", "date": "2026-06-24", "heure_debut": 14, "heure_fin": 16,
        "code": "ANG 1367", "matiere": "Initiation à la gestion de projet", "semestre": 3,
        "surveillants": ["Hounmenou", "Toboula"],
    },

    # ---------- SEMESTRE 4 ----------
    {
        "jour": "Jeudi", "date": "2026-06-25", "heure_debut": 14, "heure_fin": 16,
        "code": "ANG 1461", "matiere": "Phonologie et Communication", "semestre": 4,
        "surveillants": ["Koutchade", "Koukpossi", "Dovonou", "Hounyetin", "Dossou"],
    },
    {
        "jour": "Jeudi", "date": "2026-06-25", "heure_debut": 16, "heure_fin": 18,
        "code": "ANG 1462", "matiere": "Histoire Économique", "semestre": 4,
        "surveillants": ["Abodohoui", "Houndjo", "Ahouangansi", "Seguedeme", "Bodjrenou", "Hounmenou"],
    },
    {
        "jour": "Vendredi", "date": "2026-06-26", "heure_debut": 8, "heure_fin": 10,
        "code": "ANG 1463", "matiere": "Linguistique et Anglais de Spécialité", "semestre": 4,
        "surveillants": ["Datondji", "Koukpossi", "Kpavode"],
    },
    {
        "jour": "Vendredi", "date": "2026-06-26", "heure_debut": 10, "heure_fin": 12,
        "code": "ANG 1464", "matiere": "Techniques d'Enseignement", "semestre": 4,
        "surveillants": ["Egounleti", "Hindeme", "Kottin"],
    },
    {
        "jour": "Vendredi", "date": "2026-06-26", "heure_debut": 12, "heure_fin": 14,
        "code": "ANG 1465", "matiere": "Méthodologie de la Recherche", "semestre": 4,
        "surveillants": ["Iwikotan", "Dovonou", "Kottin", "Toboula"],
    },
    {
        "jour": "Samedi", "date": "2026-06-27", "heure_debut": 12, "heure_fin": 14,
        "code": "ANG 1466", "matiere": "Bibliographie, Droit d'Auteur et Styles de Référence", "semestre": 4,
        "surveillants": ["Abadame", "Sakpoliba", "Amoussou"],
    },
    {
        "jour": "Samedi", "date": "2026-06-27", "heure_debut": 14, "heure_fin": 16,
        "code": "ANG 1467", "matiere": "Initiation à la Rédaction de Projet", "semestre": 4,
        "surveillants": ["Abadame", "Kpavode"],
    },
]
