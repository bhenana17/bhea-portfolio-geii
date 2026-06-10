from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask, render_template

app = Flask(__name__)

# --------------------
# Données du portfolio
# --------------------

projects = [
    {
        "title": "Système RFID ESP32",
        "desc": "Contrôle d'accès avec ESP32 et module RFID RC522.",
        "tech": ["ESP32", "MicroPython", "RFID"],
    },
    {
        "title": "Projet traitement du signal",
        "desc": "Filtrage et amplification de signal analogique.",
        "tech": ["Electronique", "Python", "DSP"],
    },
    {
        "title": "Balance automatisée",
        "desc": "Système de pesée automatisé avec microcontrôleur.",
        "tech": ["C", "Capteurs", "Automatisme"],
    },
]

skills = [
    "Python",
    "C",
    "MicroPython",
    "ESP32",
    "Electronique analogique",
    "Automatisme",
    "Réseaux (MPLS, SD-WAN)",
]


# --------------------
# Routes
# --------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def project_page():
    return render_template("projects.html", projects=projects)


@app.route("/skills")
def skills_page():
    return render_template("skills.html", skills=skills)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
