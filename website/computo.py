import requests
from bs4 import BeautifulSoup
from flask import Blueprint

p = Blueprint('p', __name__)

@p.route('/')
def hola(start=True):
    dinero = 0
    req = requests.get('https://www.teleton.cl/')
    soup = BeautifulSoup(req.content, 'lxml')
    get = soup.find(class_='counter3')
    get2 = get.contents[0]
    dinero = get2.strip()
    print(dinero)
    return str(dinero)