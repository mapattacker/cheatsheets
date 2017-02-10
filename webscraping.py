# for plain old html
import urllib
url = 'https://mapattack.wordpress.com'
html = urllib.urlopen(url).read()


#----------------
# chromedriver for using webforms, dropdown and other browser manipulations
from selenium import webdriver

chromedriver = r'C:\xxx\MyPythonScripts\chromedriver.exe'
url= 'https://mapattack.wordpress.com'

driver=webdriver.Chrome(chromedriver) #use PhantomJS to parse js
driver.get(url)

html = driver.page_source  #grab entire html
link = driver.current_url  #grab hyperlink


#----------------
# phantomjs for parsing javascripts, no browser popups
from selenium import webdriver

chromedriver = r'C:\xxx\MyPythonScripts\chromedriver.exe'
url= 'https://mapattack.wordpress.com'

driver=webdriver.PhantomJS(PJ) #use PhantomJS to parse js
driver.get(url)

# optional, wait 10 sec for iframe to load
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//div[starts-with(@id, "mainns_")]/iframe')))
html = driver.page_source.encode('utf-8')


#----------------
# use beautiful soup to search for html tags
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find element td, attribute data-name, with value of totalRevenue
revenue=soup.select('td[data-name="totalRevenue"]')
# use getText() to get all text within the tag
r1 = revenue[0].getText()
