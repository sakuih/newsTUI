#import json
#import pandas as pd
#from pandas.io.json import json_normalize
#import config
#from random import randint
import requests
from bs4 import BeautifulSoup


hsUrl = 'https://www.hs.fi'
alJazeeraUrl = 'https://www.aljazeera.com'
jerusalemUrl = 'https://www.jpost.com'
hindustanUrl = 'https://www.hindustantimes.com'
scmpUrl = 'https://www.scmp.com'



def getaljazeera():
    response = requests.get(aljazeeraUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    func(soup)

def geths():
    response = requests.get(hsUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.body.section.span
    func(results)

def getjerusalem():
    response = requests.get(jerusalemUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    func(soup)

def getHidustan():
    response = requests.get(hindustanUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    func(soup)

def getScmp():
    response = requests.get(scmpUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    func(soup)

def func (results):
    #headings = soup.find_all('span')
    for result in results:
        print(result.text.strip())

geths()
#getHidustan()
#getScmp()
#getaljazeera()
#getjerusalem()





