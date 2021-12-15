from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
CHARTINK_URL = "https://chartink.com/screener/mean-reversion-51"
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_stocks(driver):
  STOCK_XPATH = "//table[@id='DataTables_Table_0']/tbody/tr"
  driver.get(CHARTINK_URL)
  stocks = driver.find_elements(By.XPATH, STOCK_XPATH)
  return stocks

def parse_stocks(driver, size):
  res = {'stock name':[],
          'price':[]}
  for i in range(1, size+1):
    NAME_XPATH = f"//table[@id='DataTables_Table_0']/tbody/tr[{i}]/td[3]/a[@class='text-teal-700']"
    PRICE_XPATH = f"//table[@id='DataTables_Table_0']/tbody/tr[{i}]/td[6]"
    name = driver.find_element(By.XPATH, NAME_XPATH).text
    price = driver.find_element(By.XPATH, PRICE_XPATH).text
    res['stock name'].append(name)
    res['price'].append(price)
  
  return res
    



if __name__ == "__main__":
  print("Creating Driver")
  driver = get_driver()

  print("Fetching the page")
  stocks = get_stocks(driver)
  size = len(stocks)
  print(f'Found {size} stocks')
  stocks_data = parse_stocks(driver, size)
  df = pd.DataFrame(stocks_data)
  df.to_csv('stocks_data.csv')