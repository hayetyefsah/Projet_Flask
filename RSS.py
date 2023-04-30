import feedparser
from json import load
from flask import Flask, render_template, redirect, url_for


#Extraire les informations du fichier qui contient les flux RSS( liens.json).
with open('liens.json') as f:
    FEEDS=load(f)

#Fonction qui extrait les liens URL des flux RSS
def entry(lien):
    list=[]
    NewsFeed = feedparser.parse(lien)
    entry = NewsFeed.entries
    for i in range(len(entry)):
        list.append(entry[i].link)
    return(list)

app = Flask(__name__)




#Route pour chaque flux qui permet d'avoir accés aux liens du flux sélectionné
@app.route('/<FLUX>')

def RSS(FLUX):
    entries= entry(FEEDS[FLUX]) 
    return render_template("index1.html",entries=entries)

#Route qui permet d'avoir accés à l'accueil où il y a la liste des flux RSS( liens.json)
@app.route("/")

def liens():
    return render_template("index.html",FEEDS = FEEDS,RSS=RSS)

