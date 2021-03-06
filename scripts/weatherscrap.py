#!/bin/python3

# Set up chrome driver https://sites.google.com/a/chromium.org/chromedriver/getting-started
# Install xorg-x11-server-Xvfb

import requests
import bs4
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display

def get_smn():
        
        smn = requests.get('http://www.smn.gov.ar/?mod=pron&id=1')
        soup = BeautifulSoup(smn.content, 'html.parser')
        return soup.find(id="divPronostico").b.string.split()[0]
        
def get_accu():

        accu = requests.get('http://www.accuweather.com/es/ar/buenos-aires/7894/weather-forecast/7894')
        soup = BeautifulSoup(accu.content, 'html.parser')
        u = soup.find("li", class_=re.compile('current first cl')).find(class_="large-temp").string
        return u.replace("°", "")
        
def get_wc():

        display = Display(visible=0, size=(800, 600))
        display.start()
        browser = webdriver.Chrome('/usr/bin/chromedriver')
        browser.get('https://weather.com/es-AR/tiempo/hoy/l/ARBA0009:1:AR')
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        browser.quit()
        display.stop()
        return soup.find(class_="today_nowcard-temp").find(class_="dir-ltr").string
#       s/term soup.find(class_="today_nowcard-feels").find(class_="dir-ltr").string

def main():

        smn = get_smn()
        with open('/tmp/smn', 'w') as f:
                f.write(smn)

        accu = get_accu()
        with open('/tmp/accu', 'w') as f:
                f.write(accu)

        wc = get_wc()
        with open('/tmp/wc', 'w') as f:
                f.write(wc)

#       print("SMN:     ", get_smn(), "ST: n/a")
#       print("ACCU:    ", get_accu(), "ST: n/a")
#       print("WC:      ", get_wc(), "°C ST: n/a")
        
if __name__ == "__main__":
    main()
