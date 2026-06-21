# -*- coding: utf-8 -*-
"""
Serveur Flask qui sert de webhook pour Twilio WhatsApp.
Twilio appelle POST /whatsapp à chaque message reçu sur le numéro WhatsApp Sandbox.
"""
from flask import Flask, request, Response
from bot_logic import repondre

app = Flask(__name__)


@app.route("/", methods=["GET"])
def accueil():
    return "✅ Le bot d'examens est en ligne."


@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    message_entrant = request.form.get("Body", "")
    reponse_texte = repondre(message_entrant)

    # Réponse au format TwiML attendu par Twilio
    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{_escape_xml(reponse_texte)}</Message>
</Response>"""
    return Response(twiml, mimetype="text/xml")


def _escape_xml(texte: str) -> str:
    return (
        texte.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
