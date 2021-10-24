from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import os
import sys
import urllib
import time
import tkinter as tk
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from patch import download_latest_chromedriver, webdriver_folder_name

def delay(waiting_time=5):
    driver.implicitly_wait(waiting_time)

if __name__ == "__main__":
    # download latest chromedriver, please ensure that your chrome is up to date
    while True:
        try:
            # create chrome driver
            path_to_chromedriver = os.path.normpath(
                os.path.join(os.getcwd(), webdriver_folder_name, "chromedriver.exe")
            )
            driver = webdriver.Chrome(path_to_chromedriver)
            delay()
            break
        except Exception:
            # patch chromedriver if not available or outdated
            try:
                driver
            except NameError:
                is_patched = download_latest_chromedriver()
            else:
                is_patched = download_latest_chromedriver(
                    driver.capabilities["version"]
                )
            if not is_patched:
                sys.exit(
                    "[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:"
                    "https://chromedriver.chromium.org/downloads"
                )
