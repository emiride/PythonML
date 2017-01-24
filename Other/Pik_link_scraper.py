import requests
from bs4 import BeautifulSoup
import csv

file_txt = open("links.txt", "r")
urls = file_txt.readlines()
file_txt.close()

browser_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
headers = ["Cijena", "Stanje", "Lokacija", "Proizvodjac", "Model", "Godiste", "Kilometraza"]
lista = [headers]
for url in urls:
    r = requests.get(url.replace("\n",""), headers = browser_headers)
    page_content = r.content.decode()

    soup = BeautifulSoup(page_content, "html.parser")
    try:
        cijena = soup.find(class_="op pop mobile-cijena ").find("p").find_next("p").get_text().replace("KM","").replace(".","").strip()
        stanje = soup.find(class_="op mobile-stanje").find("p").find_next("p").get_text().strip()
        lokacija = soup.find(class_="op pop mobile-lokacija").find("p").find_next("p").get_text().strip()
        proizvodjac = soup.find(class_="op pop ispod").find("p").find_next("p").get_text().strip()
        model = soup.find(class_="op ispod").find("p").find_next("p").get_text().strip()
        godiste = soup.find(class_="op ispod").find_next(class_="op ispod").find("p").find_next("p").get_text().strip()
        kilometraza = soup.find(class_="op ispod").find_next(class_="op ispod").find_next(class_="op ispod").find("p").find_next("p").get_text().replace(".","").strip()
        lista.append([cijena,stanje,lokacija,proizvodjac,model,godiste,kilometraza])
    except:
        pass
    print(lista)

