# Chargement des librairies 
from flask import Flask, render_template

# Création de l'instance de l'application
app = Flask(__name__)

## Création de la page d'accueil #############
@app.route('/')
def accueil():

    # Ajout des icônes selon le thème (langages et logiciels)
    dict_icon = {
        "Langage de programmation" : [
            ["logo_SQL.png", "120", "180", "logo_SQL"],
            ["programmation-vba-360x360.jpg", "120", "120", "logo_VBA"],
            ["Python-logo-notext.svg.png", "120", "120", "logo_Python"],
            ["R_logo.svg.png", "120", "120", "logo_R"],
            ["SAS_logo_horiz.svg", "150", "150", "logo_SAS"]
        ],

        "Base de données" : [
            ["DBeaver_logo.svg.png", "90", "90", "logo_dbeaver"],
            ["sqlite.png", "120", "150", "logo_sqlite"],
            ["mysql.png", "90", "120", "logo_mysql"],
            ["Oracle_logo.svg.png", "20%", "60%", "logo_oracle"],
            ["mongodb.png", '60%', '60%', 'logo_mongodb'],
            ["Neo4j-logo_color.png", "90", "150", "logo_neo4j"],
            ["Redis_Logo.svg.png", "90", "150", "logo_redis"],

        ],

        "Développement WEB" : [
            ["HTML5_logo_and_wordmark.svg.png", "120", "120", "logo_html"],
            ["CSS3_logo_and_wordmark.svg.png", "90", "90", "logo_css"],
            ["js_logo.png", "120", "120", "logo_js"],
            ["PHP-logo.svg.png", "120", "120", "logo_php"],
            ["Flask_logo.svg.png", "120", "150", "logo_flask"],
            ["Bootstrap_logo.svg.png", "90", "120", "logo_bootstrap"]
        ],

        "Big Data / Machine Learning" : [
            ["logo_spark.png", "60%", "60%", "logo_spark"],
            ["Scikit_learn_logo_small.svg.png", "40%", "40%", "logo_scikit_learn"],
            ["768px-Keras_logo.svg.png", "80", "80", "logo_keras"],
            ["Amazon_Web_Services_Logo.svg.png", "25%", "25%", "logo_aws"]
            #["Tensorflow_logo.svg.png", "20%", "20%", "logo_tensorflow"],
        ],

        "Datavisualisation" : [
            ["Microsoft_Excel_2013-2019_logo.svg.png", "60%", "30%", "logo_Excel"],
            ["New_Power_BI_Logo.svg.png", "60%", "30%", "logo_powerbi"],
            ["Tableau-Logo.png", "70%", "50%", "logo_tableau"]
        ],

        "Gestion de projet" : [
            ["git.png", "60%", "60%", "logo_git"],
            ["git_hub_logo.png", "60%", "60%", "logo_github"],
        ],

        "Bureautique" : [
            ["LaTeX_logo.svg.png", "90", "120", "logo_latex"],
            ["marp_logo.png", "90", "140", "logo_marp"],
            ["logo_word.png", "90", "90", "logo_word"],
            ["powerpoint.png", "90", "90", "logo_powerpoint"],
        ]
    }

    items = ["Langage de programmation", "Base de données", 
             "Développement WEB", "Big Data / Machine Learning",
             "Datavisualisation", 
             "Gestion de projet", "Bureautique"]
    index = [0, 1, 2, 3, 4, 5, 6]

    return render_template("accueil.html",
                           items=items,
                           index=index,
                           dict_icon=dict_icon)

##############################################

## Aperçu du template portfolio ##############
@app.route("/template")
def obs():
    return render_template("index.html")
##############################################

## Pour les SAÉ/projets ##########################
@app.route("/SAE201")
def projet_201():
    return render_template("SAE_2_01.html")

@app.route("/SAE203")
def projet_203():
    return render_template("SAE_2_03.html")

@app.route("/SAE204")
def projet_204():
    return render_template("SAE_2_04.html")

@app.route("/SAE205")
def projet_205():
    return render_template("SAE_2_05.html")

@app.route("/SAE206")
def projet_206():
    return render_template("SAE_2_06.html")

@app.route("/SAE301")
def projet_301():
    return render_template("SAE_3_01.html")

@app.route("/SAE302")
def projet_302():
    return render_template("SAE_3_02.html")

@app.route("/SAE303")
def projet_303():
    return render_template("SAE_3_03.html")

@app.route("/SAE401")
def projet_401():
    return render_template("SAE_4_01.html")

@app.route("/SAE402")
def projet_402():
    return render_template("SAE_4_02.html")

@app.route("/SAE501")
def projet_501():
    return render_template("SAE_5_01.html")

@app.route("/SAE502")
def projet_502():
    return render_template("SAE_5_02.html")

@app.route("/SAE503")
def projet_503():
    return render_template("SAE_5_03.html")
##################################################

# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)
############################