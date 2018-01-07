# for plain old html
import urllib
url = 'https://mapattack.wordpress.com'
html = urllib.urlopen(url).read()


#----------------
# force all encoding to be utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#----------------
# chromedriver for using webforms, dropdown and other browser manipulations
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = r'C:\xxx\MyPythonScripts\chromedriver.exe'
url= 'https://mapattack.wordpress.com'

driver=webdriver.Chrome(chromedriver) #use PhantomJS to parse js
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




#----------------
# phantomjs for parsing javascripts, no browser popups
from selenium import webdriver

chromedriver = r'C:\xxx\MyPythonScripts\chromedriver.exe'
url= 'https://mapattack.wordpress.com'

driver=webdriver.Chrome(chromeDriver) #use ChromeDriver.... OR
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
# OR use contents to get all contents within tag, but as a list w every linebreak
r1 = revenue[0].contents 
    # e.g., ['1 Tampines Walk, Our Tampines Hub', <br/>, '#04-31', <br/>, 'Singapore 528523']
# print pretty
revenue[0].prettify()


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

# get attribute content; eg links in href
for tag in soup.select('a'):
    a = tag.get('href')
    print(a)

#----------------
# extract URL for bs4, independent of selenium
html = urllib.urlopen(url).read()


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
