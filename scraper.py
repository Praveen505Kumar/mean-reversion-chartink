from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHARTINK_URL = "https://chartink.com/screener/mean-reversion-51"
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  
  return driver

if __name__ == "__main__":
  print("Creating Driver")
  driver = get_driver()

  print("Fetching the page")
  driver.get(CHARTINK_URL)

  print("page title: ", driver.title)

  stocks = driver.find_element_by_class_name('text-teal-700')
  print(len(stocks))
  driver.close()