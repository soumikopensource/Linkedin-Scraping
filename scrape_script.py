from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
option = Options()

# linkedin login and going to the target
driver_path = "./chromedriver.exe"
s = Service(driver_path)
driver = webdriver.Chrome(service=s)
email = "rishuranjan039@gmail.com"
password = "Rishuab@1995"
driver.get('https://www.linkedin.com/login')
driver.maximize_window()
#wait = WebDriverWait(driver, 30)
time.sleep(5)
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
driver.get("https://www.linkedin.com/groups/44979/members/")

time.sleep(2)

profile_links = []
profile_image_links = []
members = []
emails =[]
# scrolling and loading from top to bottom
scroll_pause_time = 3 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1
count = 0

while True:
    # scroll one screen height each time
    #see_more = driver.find_element(By.CLASS_NAME,'artdeco-button') 
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;") 
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
        
    
    profiles = soup.find_all(class_='artdeco-list__item', limit=5)

    # button = driver.find_elements(By.CLASS_NAME, 'artdeco-button--1')
    # driver.execute_script("arguments[0].click();", button)
    
    for profile in profiles:
        profile_links.append(profile.find("a",{"class":"ui-entity-action-row__link"})['href'])
        profile_image_links.append(profile.find('img')['src'])
        members.append(profile.find(class_='artdeco-entity-lockup__title').text)
        link = "https://www.linkedin.com"+str(profile.find("a",{"class":"ui-entity-action-row__link"})['href'])
        driver.get(link)
        contact_link = link + str("overlay/contact-info/")
        driver.get(contact_link)
        contact_info = soup.find(class_='ci-email')
        emails.append(contact_info.find('a').text)



    
    
    if screen_height > scroll_height:
        break
    



    # count = len(profile_links)
    
    # if count > 5000:
    #     break
  

    
    



#print(len(profile_image_links))
#print(emails)
    
       












    







  



