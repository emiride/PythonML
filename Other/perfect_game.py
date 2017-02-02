import requests
from selenium import webdriver
from bs4 import BeautifulSoup
base_url = "http://www.perfectgame.org"
url = "http://www.perfectgame.org/Players/PlayerProfile_ContactInfo.aspx?ID=J34665D097ED"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
list = []

driver = webdriver.Chrome(r"C:\Users\HomePC\Desktop\chromedriver.exe")
driver.get(base_url)
driver.find_element_by_id("signdiv").click()
driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbUsername").send_keys("hockeyscoutingca@hotmail.com")
driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbPassword").send_keys("bballstats10")
driver.find_element_by_name("ctl00$Header1$HeaderTop1$Button1").click()

s = requests.Session()
s.headers.update(headers)

for cookie in driver.get_cookies():
    c = {cookie['name']: cookie['value']}
    s.cookies.update(c)
#s.cookies.update( {c['name']:c['value'] for c in driver.get_cookies()} ) one liner :)
driver.close()

r = s.get(url)
page_content = r.content.decode()
soup = BeautifulSoup(page_content, "html.parser")

HS_Grad = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblGradYear]").text
Age = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblAgeNow]").text
Age_on_2017_draft = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblAgeAtDraft]").text
Position_primary = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblPrimaryPosition]").text
Position_other = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblOtherPositions]").text
Height = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblHeight]").text
Weight = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblWeight]").text
BT = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblBatsThrows]").text
School = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblHS]").text
Hometown = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblHomeTown]").text
Summer_team = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblSummerTeam]").text
Fall_team = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblFallTeam]").text
list.append([HS_Grad, Age, Age_on_2017_draft, Position_primary, Position_other, Height, Weight, BT, School, Hometown, Summer_team, Fall_team])
print(list, len(list[0]))


