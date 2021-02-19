
# def html_from_browser(url)
#   browser = BrowserPool.instance.get_browser
#   browser.navigate.to url
#   return browser.page_source
# rescue Selenium::WebDriver::Error::TimeOutError => e
#   browser.action.send_keys(Selenium::WebDriver::Keys::KEYS[:escape])
#   return browser.page_source
# ensure
#   BrowserPool.instance.release!(browser)
# end
# handling button
# import mechanize
# brwsr = mechanize.Browser()
# brwsr.set_handle_robots(False)
# brwsr.open(url)
# brwsr.select_form(nr = 0)
# response = brwsr.submit()
# brwsr.submit()
# import mechanicalsoup
# browser = mechanicalsoup.Browser()
# login_page = browser.get(url, verify= False)
# login_html = login_page.soup

# form = login_html.select("form")[0]
# profiles_page = browser.submit(form, login_page.url)

#driver.manage().timeouts().implicitlyWait(5);
#driver.findElement(By.tagName("body")).sendKeys("Keys.ESCAPE");

# make HTTP GET request to the target URL
# print('HTTP GET: %s', url)
# response = requests.get(url, verify= False)

# # parse content
# content = BeautifulSoup(response.text, 'lxml')

# extract URLs referencing PDF documents
#all_urls = content.find_all('a')

test_url = "https://www.facebook.com/"
url__ = "https://online.pucit.edu.pk/index.php/welcome"


# packages
import requests
from bs4 import BeautifulSoup
from urllib.request import unquote
import urllib.request
from contextlib import redirect_stdout

# target URL
url = 'https://data.lhc.gov.pk/reported_judgments/judgments_approved_for_reporting'
url_ = 'https://data.lhc.gov.pk/reported_judgments/judgments_approved_for_reporting_by_former_judges'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Establish chrome driver and go to report site URL
driver = webdriver.Firefox()
driver.get(url)
driver.execute_script("window.stop()")

#Click submit button
driver.find_element_by_xpath("/html/body/div[3]/div/section/div/div/div[1]/form/table/tbody/tr[15]/td[2]/input[1]").click()
#driver.find_element_by_xpath("//*[@id="appjudgmentbtn"]").click()
time.sleep(5)


all_urls = driver.find_elements_by_xpath("//a[@href]")
s = requests.Session()

for url in all_urls:
    
    print(url.get_attribute("href"))
    pdf_url = url.get_attribute("href")
    
    if '.pdf' in pdf_url:
        #get pdf
        #pdf_response = urllib.request.urlopen(pdf_url, verify= False)
        #pdf_response= urllib.request.urlretrieve(url, pdf_url)
        
        pdf_response = s.get(pdf_url, verify= False)
        time.sleep(5)
        
        # extract  PDF file name
        filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')
        
        # write PDF to local file
        with open('D:/Thesis/Data-scrapper/by-sitting-judges/' + filename, 'wb') as f:
            # write PDF to local file
            f.write(pdf_response.content)






















