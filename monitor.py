import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

settings = {}


def load_settings():
    """
    load user provided settings from the settings.txt file to populate the settings dictionary above
    """
    with open('settings.txt') as f:
        for line in f:
            if '=' in line:
                key, value = line.lower().strip().split('=', 1)
                settings[key.strip()] = value.strip()
    
    global headless, use_proxy, delay # global required for use in later functions
    # default is not headless and no proxy with a 10 second delay
    headless = settings.get('headless', 'false').lower().startswith('t')
    use_proxy = settings.get('proxy', 'false').lower().startswith('t')
    delay = int(settings.get('delay', '10000')) # in ms



def main():
    
    load_settings()
    url = settings.get("url")
    if not url:
        print("ERROR: settings.txt needs url designated")
        sys.exit(1)


    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
    

    driver = webdriver.Chrome(options=chrome_options)


    driver.get(url)
    with open("output.html","w",encoding="utf-8") as out:
        out.write(driver.page_source)
    driver.save_screenshot("screenshot.png")

    time.sleep(10)





if __name__ == '__main__':
    main()

