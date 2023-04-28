 
import feedparser
from json import load
from flask import Flask, render_template, redirect, url_for

with open('liens.json') as f:
    FEEDS=load(f)

def entry(lien):
    list=[]
    NewsFeed = feedparser.parse(lien)
    entry = NewsFeed.entries
    for i in range(len(entry)):
        list.append(entry[i].link)
    return(list)

def title(lien):
    name=[]
    NewsFeed = feedparser.parse(lien)
    entry = NewsFeed.entries
    for i in range(len(entry)):
        name.append(entry[i].title)

    return(name)

app = Flask(__name__)

@app.route('/<FLUX>')
def RSS(FLUX):
    list_1=[]
    entries= entry(FEEDS[FLUX]) 
    titles=title(FEEDS[FLUX])
    
    for i in range (len(entries)):
        list_1.append("<ul><li><a href= {} > {}</a></li></ul> ".format(entries[i],titles[i]))
    return """  <!DOCTYPE html>
                <html>
                <head>
                <title>title</title>
                </head>
                <body>  
                <h1> Les liens du flux rss</h1>
                <p> {}</p>
                </body>

                </html>
                """.format('\n'.join(list_1))

@app.route("/")
def liens():
    return render_template("index.html",FEEDS = FEEDS,RSS=RSS)

