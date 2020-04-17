# for plain old html, python 2.7
import urllib
url = 'https://mapattack.wordpress.com'
html = urllib.urlopen(url).read()

# note that it might be better to use chromedriver to retrieve html as some info might be truncated
import urllib.request # python 3*
html = urllib.request.urlopen(url).read()


#----------------
# download images
urllib.request.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")


# force all encoding to be utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#----------------
# chromedriver for using webforms, dropdown and other browser manipulations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import platform


if platform.system() == 'Windows':
    chromedriver = r'C:\xxx\MyPythonScripts\chromedriver235.exe'
else: # linux, mac
    chromedriver = r'/Users/xxx/MyPythonScripts/chromedriver_mac235'


# option commands are required for headless GUI Chrome
# otherwise remove all these options for normal GUI Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver=webdriver.Chrome(chromedriver, chrome_options=options)


url= 'https://mapattack.wordpress.com'
driver.get(url)

# input value into form
driver.get(r'https://npgsweb.ars-grin.gov/gringlobal/taxon/taxonomysimple.aspx')
elem = driver.find_element_by_name('ctl00$cphBody$txtSearch')  #find search box
elem.send_keys(species)  #input species, note that input must be string
elem.send_keys(Keys.RETURN) #start search
time.sleep(5)   #delay for search to process

# get data from searched page
html = driver.page_source  #grab entire html
link = driver.current_url  #grab hyperlink


# select dropdown
select = Select(driver.find_element_by_id('fruits01'))
# using this as sample <option value="7">Jul</option>
    # select by visible text
select.select_by_visible_text('Jul')
    # select by value 
select.select_by_value('7')
# press button
driver.find_element_by_css_selector('.button.c_button.s_button').click()
driver.find_element_by_link_text("Send InMail").click()
driver.find_element_by_xpath('//a[img/@src="/static/img/download.png"]').click() # click image
# close chrome so there will not be so many appearing if there is iteration
driver.close()


#----------------
# handling/removing pop-ups
driver=webdriver.Chrome(chromedriver)
driver.get(url)
time.sleep(2)
driver.refresh()
time.sleep(2)
html = driver.page_source

#----------------
# parsing html that are in iframes
from selenium import webdriver

driver.get(url)
# add these two lines
iframeElement = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframeElement)
html = driver.page_source.encode('utf-8') #without encode, sometimes value does not appear


#----------------
# if iframe does not load element values, use this
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chromedriver = r'C:\xxx\MyPythonScripts\chromedriver.exe'
url= 'https://mapattack.wordpress.com'

driver=webdriver.Chrome(chromedriver)
driver.get(url)

# optional, wait 10 sec for iframe to load
    # by xpath
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//div[starts-with(@id, "mainns_")]/iframe')))
    # by id
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'ddlDay')))
    # by tag
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))
html = driver.page_source.encode('utf-8')


#----------------
# use beautiful soup to search for html tags
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find element td, attribute data-name, with value of totalRevenue; using xpath
revenue=soup.select('td[data-name="totalRevenue"]')
# use getText() to get all text within the tag
r1 = revenue[0].getText()
# OR use contents to get all contents within tag, but as a list w every linebreak
r1 = revenue[0].contents 
    # e.g., ['1 Tampines Walk, Our Tampines Hub', <br/>, '#04-31', <br/>, 'Singapore 528523']
# print pretty
revenue[0].prettify()


#----------------
# download html as file and prettify
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
with open('test.html', 'w') as f:
    f.write(soup.prettify())


#----------------
# other bs4 selection
soup.select("title") # get title tag
soup.select("body a") # all a tag inside body
soup.select("html head title") # html->head->title
soup.select("head > title") # head->title
soup.select("p > a") # all a tag that inside p
soup.select("body > a") # all a tag inside body
soup.select(".sister") # select by class
soup.select("#link1") # select by id
soup.select('span[data-bind]') # select elements named <span> that have an attribute called data-bind

# get attribute content; eg links in href
for tag in soup.select('a'):
    a = tag.get('href')
    print(a)


#----------------
# single result to dump into soup and retrieve list
# e.g. get all rows in a table, then put each row into a list
url = 'https://www.xeno-canto.org/explore?query=asian%20koel'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
result = soup.select('table[class="results"] tr')

for i in result[1:]:
    soup = BeautifulSoup(str(i), 'html.parser')
    result = soup.select('td')
    print(result)


#----------------
# ANONOMYOUS SCRAPING USING TOR
# https://deshmukhsuraj.wordpress.com/2015/03/08/anonymous-web-scraping-using-python-and-tor/

# install tor in Ubuntu
sudo apt-get install tor
# start tor
tor &
# check for port and ip used by tor
netstat -tupln

import socks
import socket
import requests

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
socket.socket = socks.socksocket

# check your IP in the web
print requests.get("http://icanhazip.com").text
