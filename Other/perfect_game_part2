from time import sleep
from selenium import webdriver
import csv

base_url = "http://www.perfectgame.org/Players/"

file_txt = open("links2.txt", "r")
urls = file_txt.readlines()
file_txt.close()
print(len(urls))

file_csv = open("contact_data.csv", "w", newline='', encoding='utf-8')
csv_writer = csv.writer(file_csv, dialect=csv.excel)
csv_writer.writerow(["Name and Surname","Address","Phone","Email"])


driver = webdriver.Chrome(r"C:\Users\HomePC\Desktop\chromedriver.exe")
driver.set_window_size(1500,1080)
driver.get("http://www.perfectgame.org/")
driver.find_element_by_id("signdiv").click()
driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbUsername").send_keys("hockeyscoutingca@hotmail.com")
driver.find_element_by_name("ctl00$Header1$HeaderTop1$tbPassword").send_keys("bballstats10")
driver.find_element_by_name("ctl00$Header1$HeaderTop1$Button1").click()

for url in urls:
    try:
        driver.get(base_url + url.replace("\n", ""))
        name = driver.find_element_by_id("ContentPlaceHolder1_Bio1_lblName").text
        driver.execute_script("window.scrollTo(0, 1100);")
        driver.find_element_by_id("ContentPlaceHolder1_lbDisplayContact").click()
        try:
            sleep(1)
            address = driver.find_element_by_id("ContentPlaceHolder1_lblAddress").text
            phone = driver.find_element_by_id("ContentPlaceHolder1_lblPhone").text
            email = driver.find_element_by_id("ContentPlaceHolder1_lblEmail").text
            csv_writer.writerow([name,address,phone,email])
            file_csv.flush()
        except:
            sleep(2)
            address = driver.find_element_by_id("ContentPlaceHolder1_lblAddress").text
            phone = driver.find_element_by_id("ContentPlaceHolder1_lblPhone").text
            email = driver.find_element_by_id("ContentPlaceHolder1_lblEmail").text
            csv_writer.writerow([name, address, phone, email])
            file_csv.flush()
    except:
        address = "NaN"
        phone = "NaN"
        email = "NaN"
        csv_writer.writerow([name, address, phone, email])
        file_csv.flush()

file_csv.close()
