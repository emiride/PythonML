import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

base_url = "http://www.perfectgame.org/Players/"
url = "http://www.perfectgame.org/Players/Playerprofile.aspx?ID="
url_id = 346511
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
list = []
_1Name_and_Surname="";_2HS_Grad="";_3Age="";_4Age_on_2017_draft="";_5Position_primary="";_6Position_other="";_7Height="";_8Weight="";_9BT="";_10School="";_11Hometown="";_12Summer_team="";_13Fall_team="";_14national_rank="";_15position_ss="";_16gpa="";_17sat="";_18act="";_19fb="";_2060="";_2110_spl="";_22of="";_23_if="";_24bat_speed_imapact="";_25hand_speed="";_26time_to_impact="";_27exit_velo=""
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

file = open('links.txt', 'w')

file_csv = open("data.csv", "w", newline='', encoding='utf-8')
csv_writer = csv.writer(file_csv, dialect=csv.excel)
csv_writer.writerow(['Name and Surname','HS Grad',"Age","Age on 2017 draft","Position primary","Position other","Height","Weight","BT","School","Hometown","Summer team","Fall team","national rank","position ss","gpa","sat","act",'fb','60','10 spl','of',"if",'bat speed imapact',"hand speed","time to impact","exit velo"])
#-----------------------------------------------------------------------------------------
while(url_id > 40000):
    r = s.get(url + str(url_id))
    page_content = r.content.decode()
    soup = BeautifulSoup(page_content, "html.parser")
    try:
        _1Name_and_Surname = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblName]").text
        try:
            _2HS_Grad = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblGradYear]").text
        except:
            _2HS_Grad = "NaN"
        try:
            _3Age = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblAgeNow]").text
        except:
            _3Age = "NaN"
        try:
            _4Age_on_2017_draft = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblAgeAtDraft]").text
        except:
            _4Age_on_2017_draft = "NaN"
        try:
            _5Position_primary = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblPrimaryPosition]").text
        except:
            _5Position_primary = "NaN"
        try:
            _6Position_other = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblOtherPositions]").text
        except:
            _6Position_other = "NaN"
        try:
            _7Height = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblHeight]").text
        except:
            _7Height = "NaN"
        try:
            _8Weight = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblWeight]").text
        except:
            _8Weight = "NaN"
        try:
            _9BT = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblBatsThrows]").text
        except:
            _9BT = "NaN"
        try:
            _10School = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblHS]").text
        except:
            _10School = "NaN"
        try:
            _11Hometown = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblHomeTown]").text
        except:
            _11Hometown = "NaN"
        try:
            _12Summer_team = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblSummerTeam]").text
        except:
            _12Summer_team = "NaN"
        try:
            _13Fall_team = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblFallTeam]").text
        except:
            _13Fall_team = "NaN"
        try:
            _14national_rank = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblNationalRank]").text
        except:
            _14national_rank = "NaN"
        try:
            _15position_ss = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblNationalPosRank]").text
        except:
            _15position_ss = "NaN"
        try:
            _16gpa = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblGPA]").text
        except:
            _16gpa = "NaN"
        try:
            if soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblSAT]").text != "--":
                _17sat = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblSAT]").text
        except:
            _17sat = "NaN"
            pass
        try:
            if soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblACT]").text != "--":
                _18act = soup.select_one("span[id=ContentPlaceHolder1_Bio1_lblACT]").text
        except:
            _18act = "NaN"
            pass
        try:
            _19fb = soup.select_one("span[id=ContentPlaceHolder1_lblFB]").text
        except:
            _19fb = "NaN"
        try:
            _2060 = soup.select_one("span[id=ContentPlaceHolder1_lbl60]").text
        except:
            _2060 = "NaN"
        try:
            _2110_spl = soup.select_one("span[id=ContentPlaceHolder1_lbl10]").text
        except:
            _2110_spl = "NaN"
        try:
            _22of = soup.select_one("span[id=ContentPlaceHolder1_lblOF]").text
        except:
            _22of = "NaN"
        try:
            _23_if = soup.select_one("span[id=ContentPlaceHolder1_lblIF]").text
        except:
            _23_if = "NaN"
        try:
            _24bat_speed_imapact = soup.select_one("span[id=ContentPlaceHolder1_lblZeppBat]").text
        except:
            _24bat_speed_imapact = "NaN"
        try:
            _25hand_speed = soup.select_one("span[id=ContentPlaceHolder1_lblZeppHand]").text
        except:
            _25hand_speed = "NaN"
        try:
            _26time_to_impact = soup.select_one("span[id=ContentPlaceHolder1_lblZeppTime]").text
        except:
            _26time_to_impact = "NaN"
        try:
            _27exit_velo = soup.select_one("span[id=ContentPlaceHolder1_lblPRExitVelo]").text
        except:
            _27exit_velo = "NaN"
        try:
            file.write("%s\n" % soup.find('li', id='ContentPlaceHolder1_Bio1_liContactInfo').a["href"])
        except:
            pass
        csv_writer.writerow(
            [_1Name_and_Surname, _2HS_Grad, _3Age, _4Age_on_2017_draft, _5Position_primary, _6Position_other, _7Height,
             _8Weight, _9BT, _10School, _11Hometown, _12Summer_team, _13Fall_team, _14national_rank, _15position_ss,
             _16gpa, _17sat, _18act, _19fb, _2060, _2110_spl, _22of, _23_if, _24bat_speed_imapact, _25hand_speed,
             _26time_to_impact, _27exit_velo])
        file_csv.flush()
        file.flush()
        print(url_id)
        url_id = url_id - 1
    except:
        print("passed: " + str(url_id))
        url_id = url_id - 1


file_csv.close()
file.close()





