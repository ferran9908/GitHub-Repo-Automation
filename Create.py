from selenium import webdriver
import os
import sys

browser = webdriver.Chrome()
browser.get("https://www.github.com/login")

path = "Users/ferran/Documents/Projects/"

username = "GITHUB-USERNAME"
password = "GITHUB-PASSWORD"

RepoName = str(sys.argv[1])
os.mkdir(path + str(sys.argv[1]))


browser.find_element_by_xpath("//input[@id='login_field']").send_keys(username)
browser.find_element_by_xpath("//input[@id='password']").send_keys(password)
browser.find_element_by_xpath("//input[@name='commit']").click()

browser.get("https://www.github.com/new")
browser.find_elements_by_xpath("//input[@id='repository_name']")[0].send_keys(RepoName)

browser.find_element_by_css_selector("button.first-in-line").submit()

browser.quit()








