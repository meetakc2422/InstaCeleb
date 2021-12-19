from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from time import sleep
if os.path.isfile('E:\Desktop\InstaScrape\out.csv'):
        os.remove('out.csv')
chrome_options = Options()
u_name ='akash4pubg6'
pswrd = 'Novaka$2021'
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
# driver.maximize_window()


driver.get('http://instagram.com/')
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="-MzZI"][1]//input')))
user = driver.find_element_by_xpath('//div[@class="-MzZI"][1]//input')
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="-MzZI"][2]//input')))
password = driver.find_element_by_xpath('//div[@class="-MzZI"][2]//input')
user.send_keys(u_name)
password.send_keys(pswrd)
driver.find_element_by_xpath('//button[@type="submit"]').click()
driver.maximize_window()
##fetching input
celeb_list=[]
post_list =[]
followers_list =[]
following_list = []
with open('celebs.csv','r') as input_file:
        reader = csv.reader(input_file)
        for celeb in reader:
                WebDriverWait(driver,5).until(
                        EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search Input"]')))
                search = driver.find_element_by_xpath('//input[@aria-label="Search Input"]')
                search.send_keys(celeb)
                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@role="none"]')))
                driver.execute_script('document.getElementsByClassName("glyphsSpriteVerified_small u-__7")[0].click()')
                sleep(2)
                WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME,"k9GMp ")))
                Posts = driver.find_element_by_xpath('//span[@class="-nal3 "]/span').get_attribute('innerText')
                followers = driver.find_element_by_xpath('//ul[@class="k9GMp "]/li[2]/a/span').get_attribute('innerText')
                following = driver.find_element_by_xpath('//ul[@class="k9GMp "]/li[3]/a/span').get_attribute('innerText')
                celeb_list.append(celeb)
                post_list.append(Posts)
                followers_list.append(followers)
                following_list.append(following)
                print(following)

# driver.execute_script("document.getElementsByClassName('_2dbep qNELH')[0].click()")
sleep(1)
# signing out
# driver.execute_script('document.getElementsByClassName("-qQT3")[4].click()')
driver.quit()


with open('E:\Desktop\InstaScrape\out.csv','w') as out:
        writer = csv.writer(out,delimiter=",",lineterminator='\r')
        writer.writerow(['celeb','posts','followers','following'])
        for a,b,c,d in zip(celeb_list,post_list,followers_list,following_list):
                writer.writerow([a,b,c,d])
        out.close()