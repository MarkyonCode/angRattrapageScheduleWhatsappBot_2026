# -*- coding: utf-8 -*-
"""
Logique du bot : comprend un message texte en français et renvoie une réponse
basée sur le programme des examens (exams_data.py).
"""
import re
import unicodedata
from datetime import datetime
from zoneinfo import ZoneInfo

from exams_data import EXAMS

# Fuseau horaire utilisé pour "maintenant" (Bénin / Afrique de l'Ouest = UTC+1, pas de DST)
TZ = ZoneInfo("Africa/Porto-Novo")

JOURS_VALIDES = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


def _normaliser(texte: str) -> str:
    """Minuscule + suppression des accents, pour comparer du texte libre."""
    texte = texte.lower().strip()
    texte = unicodedata.normalize("NFKD", texte)
    texte = "".join(c for c in texte if not unicodedata.combining(c))
    return texte


def _formater_examen(exam: dict, avec_date: bool = True) -> str:
    date_str = ""
    if avec_date:
        d = datetime.strptime(exam["date"], "%Y-%m-%d")
        date_str = f" ({d.day:02d}/{d.month:02d})"
    return (
        f"📘 *{exam['code']}* — {exam['matiere']}\n"
        f"🗓️ {exam['jour']}{date_str}, {exam['heure_debut']}h-{exam['heure_fin']}H "
        f"(Semestre {exam['semestre']})"
    )


def _trouver_code_ec(texte_normalise: str):
    """Cherche un code EC du type 'ANG 1361' ou 'ang1361' dans le texte."""
    match = re.search(r"ang\s*-?\s*(\d{4})", texte_normalise)
    if match:
        code_cherche = f"ANG {match.group(1)}"
        for exam in EXAMS:
            if exam["code"].lower().replace(" ", "") == code_cherche.lower().replace(" ", ""):
                return exam
    return None


def _trouver_jour(texte_normalise: str):
    for jour in JOURS_VALIDES:
        if jour in texte_normalise:
            return jour.capitalize()
    return None


def _trouver_matiere_par_nom(texte_normalise: str):
    """Cherche si un nom de matière (ou un mot significatif de celui-ci) est mentionné."""
    meilleurs = []
    for exam in EXAMS:
        nom_normalise = _normaliser(exam["matiere"])
        mots = [m for m in re.split(r"[^a-z]+", nom_normalise) if len(m) > 3]
        if any(mot in texte_normalise for mot in mots):
            meilleurs.append(exam)
    return meilleurs


def _maintenant():
    return datetime.now(TZ)


def _exam_datetime_fin(exam: dict) -> datetime:
    d = datetime.strptime(exam["date"], "%Y-%m-%d")
    return d.replace(hour=exam["heure_fin"], tzinfo=TZ)


def repondre(message: str) -> str:
    texte = _normaliser(message)

    # --- Salutations / aide ---
    if texte in ("", "salut", "bonjour", "hello", "hi", "aide", "help", "menu"):
        return (
            "👋 Salut ! Je connais ton programme d'examens (Anglais 2, S3 & S4).\n\n"
            "Tu peux me demander :\n"
            "• *Lundi* → les examens de ce jour\n"
            "• *ANG 1361* → la matière correspondant à un code EC\n"
            "• *Phonétique* → infos sur une matière par son nom\n"
            "• *Il me reste quoi ?* → les examens pas encore passés\n"
            "• *Programme* → tout le calendrier\n"
            "• *Quand je compose Phonétique* → le jour de cet examen"
        )

    # --- Programme complet ---
    if "programme" in texte or "calendrier" in texte or "tout" in texte:
        lignes = ["🗂️ *Programme complet des examens :*"]
        for exam in EXAMS:
            lignes.append(_formater_examen(exam))
        return "\n\n".join(lignes)

    # --- Ce qu'il reste à composer ---
    if "reste" in texte or "restant" in texte or "prochain" in texte:
        maintenant = _maintenant()
        a_venir = [e for e in EXAMS if _exam_datetime_fin(e) > maintenant]
        if not a_venir:
            return "🎉 Il ne te reste plus aucun examen à composer. Bon courage pour la suite !"
        a_venir.sort(key=lambda e: (e["date"], e["heure_debut"]))
        lignes = ["📝 *Voici ce qu'il te reste à composer :*"]
        for exam in a_venir:
            lignes.append(_formater_examen(exam))
        return "\n\n".join(lignes)

    # --- Code EC -> matière ---
    exam_par_code = _trouver_code_ec(texte)
    if exam_par_code:
        return _formater_examen(exam_par_code)

    # --- Jour -> liste des examens de ce jour ---
    jour_trouve = _trouver_jour(texte)
    if jour_trouve:
        exams_du_jour = [e for e in EXAMS if e["jour"] == jour_trouve]
        if not exams_du_jour:
            return f"Aucun examen programmé le {jour_trouve}."
        exams_du_jour.sort(key=lambda e: e["heure_debut"])
        lignes = [f"📅 *Examens du {jour_trouve} :*"]
        for exam in exams_du_jour:
            lignes.append(_formater_examen(exam, avec_date=False))
        return "\n\n".join(lignes)

    # --- Nom de matière -> jour / code / horaire ---
    correspondances = _trouver_matiere_par_nom(texte)
    if len(correspondances) == 1:
        exam = correspondances[0]
        return (
            f"La matière *{exam['matiere']}* ({exam['code']}) "
            f"se compose le *{exam['jour']}* de {exam['heure_debut']}H à {exam['heure_fin']}H."
        )
    elif len(correspondances) > 1:
        lignes = ["J'ai trouvé plusieurs matières possibles :\n"]
        for exam in correspondances:
            lignes.append(_formater_examen(exam))
        return "\n\n".join(lignes)

    # --- Rien compris ---
    return (
        "🤔 Je n'ai pas compris ta demande.\n"
        "Essaie par exemple : *Lundi*, *ANG 1361*, *Phonétique*, "
        "*il me reste quoi*, ou *programme*."
    )
