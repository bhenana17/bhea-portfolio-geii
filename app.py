from flask import Flask, render_template, abort
import os
import markdown

app = Flask(__name__)

competences = [
    {
        "id": 1,
        "titre": "Vérifier",
        "ac": [
            {
                "id_ac": "AC3201",
                "titre": "Evaluer la cause racine d'un dysfonctionnement",
                "texte": "AC32.01"
            },
            {
                "id_ac": "AC3203",
                "titre": "Produire une procédure d'essaie pour valider la comformité d'un système",
                "texte": "AC32.03"
            }
        ]
    },
    {
        "id": 2,
        "titre": "Intégrer",
        "ac": [
            {
                "id_ac": "AC3401",
                "titre": "Planifier l'installation et la mise en service d'un nouvel équipement",
                "texte": "AC34.01"
            },
            {
                "id_ac": "AC3402",
                "titre": "Produire une procédure d'installation et de mise en service d'un nouvel équipement",
                "texte": "AC34.02"
            }
        ]
    }
]


@app.route("/")
def accueil():
    return render_template("accueil.html")


@app.route("/competences")
def competences_page():
    return render_template("competences.html", competences=competences)


@app.route("/ac/<string:id_ac>")
def ac_detail(id_ac):

    ac_trouve = None
    competence_parent = None

    for comp in competences:
        for ac in comp["ac"]:
            if ac["id_ac"] == id_ac:
                ac_trouve = ac
                competence_parent = comp

    if ac_trouve is None:
        return "AC introuvable", 404

    contenu = ""

    file_path = f"static/markdown/{id_ac}.md"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            contenu = markdown.markdown(f.read()#,
               # extensions=["tables", "fenced_code"]
            )

    return render_template(
        "ac_detail.html",
        ac=ac_trouve,
        competence=competence_parent,
        contenu=contenu
    )


#@app.route("/contact")
#def contact():
 #   return render_template("contact.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
