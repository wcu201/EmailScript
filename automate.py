import webbrowser
import os
import smtplib
import sys
import time
from selenium import webdriver

#form variables
url = "https://gmail.com"
user = sys.argv[1]
password = ''
subject = 'Automation Test'
email_body = 'This is a selenium automation test'

#open browser
browser = webdriver.Firefox()
browser.get(url)

#input username
emailElem = browser.find_element_by_id("identifierId")
emailElem.send_keys(user)
nextElem = browser.find_element_by_id("identifierNext")
nextElem.click()

#input password
psswrd = input()
psswrdElem = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
psswrdElem.send_keys(psswrd)
nextElem = browser.find_element_by_id("passwordNext")
nextElem.click()

time.sleep(2)

#start composing email
composeElem = browser.find_element_by_class_name('z0')
composeElem.click()

time.sleep(2)

#fill out email form
recieverElem = browser.find_element_by_class_name('vO')
recieverElem.send_keys(user)
subElem = browser.find_element_by_class_name('aoT')
subElem.send_keys(subject)
bodyElem = browser.find_element_by_xpath("//div[@aria-label='Message Body']")
bodyElem.send_keys(email_body)

#send email
sendElem = browser.find_element_by_xpath("//div[text()='Send']")
sendElem.click()



