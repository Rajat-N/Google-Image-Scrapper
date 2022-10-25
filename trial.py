import os
import time
import requests
from selenium import webdriver

def init():
    return webdriver.Chrome(executable_path="chromedriver.exe")

url ="https://www.google.com/search?q=katrina+kaif&tbm=isch&sxsrf=ALiCzsZswXK6rwZzV-RtHQSVabpnNQcNuQ:1662981775509&source=lnms&sa=X&ved=2ahUKEwjb3vzvkY_6AhUEHKYKHXpiBhoQ_AUoAnoECAEQBA&biw=1280&bih=577&dpr=1.5"

def search(wd):
    wd.get(url)
    thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
    return thumbnail_results

if __name__ == '__main__':
    wd=init()
    search(wd)
