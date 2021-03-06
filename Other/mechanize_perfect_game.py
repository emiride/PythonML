from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
base_url = "http://www.perfectgame.org/Players/"
id = 346509
url = "http://www.perfectgame.org/Players/Playerprofile.aspx?ID="

driver = webdriver.Chrome(r"C:\Users\emirh\Desktop\chromedriver.exe")
driver.get(base_url)
driver.find_element_by_id("signdiv").click()
driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbUsername").send_keys("hockeyscoutingca@hotmail.com")
driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbPassword").send_keys("bballstats10")
driver.find_element_by_name("ctl00$Header1$HeaderTop1$Button1").click()

driver.get(url+str(id))

name_and_surname = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblName").text
hs_grad = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblGradYear").text
age = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblAgeNow").text
age_on_2017_draft = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblAgeAtDraft").text
position_primary = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblPrimaryPosition").text
position_other = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblOtherPositions").text
height = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblHeight").text
weight = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblWeight").text
bt = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblBatsThrows").text
school = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblHS").text
hometown = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblHomeTown").text
summer_team = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblSummerTeam").text
fall_team = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblFallTeam").text
national_overall = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblNationalRank").text
national_position_c = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblNationalPosRank").text
state_overall = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblStateRank").text
state_position_c = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblStatePosRank").text
gpa = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblGPA").text
sat = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblSAT").text
act = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblACT").text

fb = driver.find_element_by_id("ContentPlaceHolder1_lblFB").text
_60 = driver.find_element_by_id("ContentPlaceHolder1_lbl60").text
_10_spl = driver.find_element_by_id("ContentPlaceHolder1_lbl10").text
of = driver.find_element_by_id("ContentPlaceHolder1_lblOF").text
_if = driver.find_element_by_id("ContentPlaceHolder1_lblIF").text
bat_speed_at_impact = driver.find_element_by_id("ContentPlaceHolder1_lblZeppBat").text
hand_speed = driver.find_element_by_id("ContentPlaceHolder1_lblZeppHand").text
time_to_impact = driver.find_element_by_id("ContentPlaceHolder1_lblZeppTime").text
exit_velo = driver.find_element_by_id("ContentPlaceHolder1_lblPRExitVelo").text

driver.get(driver.find_element_by_xpath("""//*[@id="ContentPlaceHolder1_Bio1_hlContactInfo"]""").get_attribute("href"))

display_contact = driver.find_element_by_id("ContentPlaceHolder1_lbDisplayContact")
ActionChains(driver).click(display_contact).perform()
ActionChains(driver).click(display_contact).perform()
time.sleep(0.5)
display_coach = driver.find_element_by_id("ContentPlaceHolder1_lbCoach")
ActionChains(driver).click(display_coach).perform()
ActionChains(driver).click(display_coach).perform()
time.sleep(0.5)
display_details = driver.find_element_by_id("ContentPlaceHolder1_lbDetails")
ActionChains(driver).click(display_details).perform()
ActionChains(driver).click(display_details).perform()

address = driver.find_element_by_id("ContentPlaceHolder1_lblAddress").text
phone = driver.find_element_by_id("ContentPlaceHolder1_lblPhone").text
email = driver.find_element_by_id("ContentPlaceHolder1_lblEmail").text

hs_coach = driver.find_element_by_id("ContentPlaceHolder1_lblCoachName").text
coach_phone = driver.find_element_by_id("ContentPlaceHolder1_lblCoachPhone").text
coach_email = driver.find_element_by_id("ContentPlaceHolder1_lblCoachEmail").text

player_dob = driver.find_element_by_id("ContentPlaceHolder1_lblDOB").text
player_other_sports = driver.find_element_by_id("ContentPlaceHolder1_lblothersports").text
player_glasses = driver.find_element_by_id("ContentPlaceHolder1_lblglasses").text
father = driver.find_element_by_id("ContentPlaceHolder1_lblFather").text
father_athletic_history = driver.find_element_by_id("ContentPlaceHolder1_lblFatherAthletic").text
father_college = driver.find_element_by_id("ContentPlaceHolder1_lblFatherCollege").text
mother = driver.find_element_by_id("ContentPlaceHolder1_lblMother").text
mother_athletic_history = driver.find_element_by_id("ContentPlaceHolder1_lblMotherAthletic").text
mother_college = driver.find_element_by_id("ContentPlaceHolder1_lblMotherCollege").text

print(name_and_surname, hs_grad, age, age_on_2017_draft, position_primary, position_other, height, weight, bt, school, hometown, summer_team, fall_team)
print(national_overall, national_position_c, state_overall, state_position_c, gpa, sat, act)
print(fb, _60, _10_spl, of, _if, bat_speed_at_impact, hand_speed, time_to_impact, exit_velo)
print(address, phone, email)
print(hs_coach, coach_phone, coach_email, player_dob, player_other_sports, player_glasses, father, father_athletic_history, father_college, mother, mother_athletic_history, mother_college)