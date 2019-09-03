from selenium import webdriver
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException

import os

os.chdir(r"D:\Users\Laurent\Documents\GitHub\pyEtude")
class COBA():
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.auth()
        self.getTravaux()

    def auth(self):
        try:
            options = webdriver.FirefoxOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--headless')


            self.driver = webdriver.Firefox(executable_path="./path/geckodriver.exe", options=options)  # Open the Firefox Selenium driver
        except:
            raise ImportError

        self.driver.get("https://brebeuf.coba.ca/pednet/login.asp?NoRegr=1")  # Go to COBA's web page

        self.driver.find_element_by_id("txtCodeUsager").send_keys(self.username)  # Enter the username
        self.driver.find_element_by_id("txtMotDePasse").send_keys(self.password)  # Enter the password
        self.driver.find_element_by_id("btnConnecter").click()

        try:  # Check if the login info was correct
            self.driver.find_element_by_class_name("BlueXButton")
            print("Login was successful")
        except NoSuchElementException:
            raise ConnectionRefusedError
    
    def getTravaux(self):
        self.driver.find_element_by_id("Menu02Center").click()
        self.page_source = driver.page_source 

if __name__ == "__main__":
    c = COBA(input("Username: "), getpass())


"""
table = driver.find_elements_by_class_name("BlueTableau")
data = table[0].find_elements_by_class_name("Even")

"""