from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    print(settings)

    # driver = webdriver.Chrome()




if __name__ == '__main__':
    main()









