from selenium import webdriver
import os
import time

chrome_location = os.path.abspath("chromedriver")
driver = webdriver.Chrome(chrome_location)

# set the URL
driver.get('https://makaut1.ucanapply.com/smartexam/public/')

# get the weeks options of the select menu
weeks = []
for i in range(13):
    weeks.append(f'//*[@id="week"]/option[{i+2}]')

# get the web page elements

# for login
first_login = '/html/body/div[2]/div/div[2]/div[1]/div/div/div[1]/a/div/div[2]/span'
username = '//*[@id="username"]'
password = '//*[@id="password"]'
submit = '//*[@id="login"]/div[4]/div/a'

# to navigate to the report entry page
report = '//*[@id="dashApp"]/div/div[1]/div/ul/li[12]/a'

# report entry details
week = '//*[@id="week"]/option[8]'
sem = '//*[@id="SEMCODE"]/option[2]'
topic = '//*[@id="topic_covered"]'
platform = '//*[@id="platform_used"]'
faculty = '//*[@id="weekly-report-save"]/div/div[4]/div[1]/div/div/div/ul/li[14]'
link = '//*[@id="record_lecture_upload_link"]'
duration = '//*[@id="duration_in_min"]'
post_class = '//*[@id="post_class_interraction_note"]'
rec = '//*[@id="assignment_received"]'
sub = '//*[@id="assignment_submitted"]'
test = '//*[@id="test_attended_if_any"]'
study = '//*[@id="daily_self_acitvity"]'
rem = '//*[@id="remark"]'
date = '/html/body/div[8]/div[3]/table/tbody/tr[5]/td[5]'
hour = '/html/body/div[8]/div[2]/table/tbody/tr/td/fieldset[1]/span[11]'
minute = '/html/body/div[8]/div[1]/table/tbody/tr/td/fieldset/span[5]'

# report entry submit
add_details = '//*[@id="btnSubmit"]'

# back to dashboard
dashboard = '//*[@id="app"]/div[3]/div/div/div[1]/div/div[1]/ul/li[1]/a'

# read report data from the input file
myfile = open("input.txt", "r")
scrap = myfile.readline()
mytext = myfile.read().split("\n")
myinput = []
for i in mytext:
    myinput.append(i.split(", "))

# select login option
driver.find_element_by_xpath(first_login).click()

time.sleep(8)

# enter login details
driver.find_element_by_xpath(username).send_keys("my_username")
driver.find_element_by_xpath(password).send_keys("my_password")
driver.find_element_by_xpath(submit).click()

time.sleep(5)

# for every report
for i in myinput:

    driver.find_element_by_xpath(report).click()

    time.sleep(5)

    driver.find_element_by_xpath(weeks[int(i[10])-1]).click()
    driver.find_element_by_xpath(sem).click()

    driver.find_element_by_xpath(topic).send_keys(i[0])
    driver.find_element_by_xpath(platform).send_keys(i[1])
    # driver.find_element_by_xpath(faculty).click()
    driver.find_element_by_xpath(link).send_keys(i[2])
    driver.find_element_by_xpath(duration).send_keys(i[3])
    driver.find_element_by_xpath(post_class).send_keys(i[4])
    driver.find_element_by_xpath(rec).send_keys(i[5])
    driver.find_element_by_xpath(sub).send_keys(i[6])
    driver.find_element_by_xpath(test).send_keys(i[7])
    driver.find_element_by_xpath(study).send_keys(i[8])
    driver.find_element_by_xpath(rem).send_keys(i[9])
    # driver.find_element_by_xpath(date).click()
    # driver.find_element_by_xpath(hour).click()
    # driver.find_element_by_xpath(minute).click()

    time.sleep(40)

    driver.find_element_by_xpath(add_details).click()
    driver.find_element_by_xpath(dashboard).click()
