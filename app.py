from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import requests
import webbrowser
import json
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from lxml import html

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    song=request.form['Singer']
    song=song.replace(" ","-")

    r=requests.get("http://www.repertuarim.com/ara/"+song)
    sayfa=r.content
    webpage = html.fromstring(sayfa)
    soup = BeautifulSoup(sayfa, "html.parser")
    Link=webpage.xpath('//a/@href')
    isimler = soup.find_all('div', attrs={'class':'title'})
    Adlar=[]
    for ın in isimler:
        ok = ın.text
        Adlar.append(ok)

    Linkler=Link[36:len(Link)-2]   
    adlar=Adlar[30:len(Adlar)-2]


    
    
       
    #webbrowser.open_new_tab(a)
    return render_template('pass.html', Linkler=Linkler, adlar=adlar)

if __name__ == '__main__':
    app.run(debug=True)


