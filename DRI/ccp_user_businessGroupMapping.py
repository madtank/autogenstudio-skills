import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHoops():
  def setup_method(self, url):
    self.driver = webdriver.Edge()
    self.vars = {}
    self.url = url
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_hoops(self):
    self.driver.get(self.url)        
    self.driver.set_window_size(1936, 1048)
    time.sleep(20)

    row_data = []
    while True:
        table_info = self.driver.find_element(By.CSS_SELECTOR, "div.ms-List-page")
        row_details = table_info.find_elements(By.CSS_SELECTOR,"div.ms-DetailsRow-fields")
        
        for row in row_details:
            column_details = row.find_elements(By.CSS_SELECTOR,'span[class^="css-"]')
            column_data = []
            for column in column_details:
                column_data.append(column.text.strip())
            row_data.append(column_data)

        next_button = self.driver.find_element(By.CSS_SELECTOR, 'button.ms-Button[title="Next"]')
        if next_button.get_attribute('disabled') is not None:
            break
        next_button.click()
        time.sleep(2)
    
    return row_data

url= "https://contactcenter.microsoft.com/userprovisioning/businessgroupsmapping"
test = TestHoops()
test.setup_method(url)
test.test_hoops()
test.teardown_method()
