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

Name_and_Surname = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblName]").text
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

contact_link = soup.find('li', id='ContentPlaceHolder1_Bio1_liContactInfo').contents
contact_url = "http://www.perfectgame.org/Players/PlayerProfile_ContactInfo.aspx?ID=J34665D097ED"

r = s.get(url)
page_content = r.content.decode()
soup = BeautifulSoup(page_content, "html.parser")


list.append([Name_and_Surname, HS_Grad, Age, Age_on_2017_draft, Position_primary, Position_other, Height, Weight, BT, School, Hometown, Summer_team, Fall_team])
print(contact_link)
print(list, len(list[0]))
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
base_url = "http://www.perfectgame.org/Players/"
url = "http://www.perfectgame.org/Players/Playerprofile.aspx?ID=346509"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
list = []

driver = webdriver.Chrome(r"C:\Users\emirh\Desktop\chromedriver.exe")
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

Name_and_Surname = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblName]").text
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



contact_url = base_url + soup.find('li', id='ContentPlaceHolder1_Bio1_liContactInfo').a["href"]

r = s.get(contact_url)
page_content = r.content.decode()
soup = BeautifulSoup(page_content, "html.parser")

#display_contact_info = soup.find("a", id="ContentPlaceHolder1_lbDisplayContact")["href"]
ID = contact_url[-12]
VIEWSTATE = soup.find('input',{'id':'__VIEWSTATE'}).get('value')
EVENTVALIDATION = soup.find('input',{'id':'__EVENTVALIDATION'}).get('value')
headers = {'Cache-Control': 'no-cache',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
           'Referer': contact_url,
           'X-MicrosoftAjax': 'Delta=true'}
payload = {"ID":ID,
           "ctl00$ToolkitScriptManager2:":"ctl00$ContentPlaceHolder1$updCoach|ctl00$ContentPlaceHolder1$lbCoach",
           "ToolkitScriptManager2_HiddenField":"",
           "ctl00$Header1$Menu1$txtSearchBox": "",
           "ctl00$Header1$Menu1$txtSearchBox2": "",
           "__EVENTTARGET":"ctl00$ContentPlaceHolder1$lbDisplayContact",
           "__EVENTARGUMENT":"",
           "__VIEWSTATE":VIEWSTATE,
           "__SCROLLPOSITIONX":"0",
           "__SCROLLPOSITIONY":"0",
           "__EVENTVALIDATION":EVENTVALIDATION,
           "__ASYNCPOST": "true",
           }
r = s.post(contact_url,headers = headers, data=payload)
page_content = r.content.decode()
soup = BeautifulSoup(page_content, "html.parser")

Coach = soup.select_one("span[id=ContentPlaceHolder1_lblCoachName]").text
list.append([Name_and_Surname, HS_Grad, Age, Age_on_2017_draft, Position_primary, Position_other, Height, Weight, BT, School, Hometown, Summer_team, Fall_team, Coach])

print(list, len(list[0]))
