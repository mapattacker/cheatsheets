# instagram api is in sandbox only, so have to use web scraping

from selenium import webdriver
from bs4 import BeautifulSoup
import time, traceback, urllib, sqlite3

######################ENTER VARIABLES########################
hashtag = 'punggoltree'
sqliteDB = 'allsocial.sqlite'
chromeDriver = r'C:\Users\xxx\MyPythonScripts\chromedriver.exe'
PJ = r'C:\Users\xxx\MyPythonScripts\phantomjs.exe'    #PhantomJS

# MacOS
# PJ = r'/Users/xxx/Scripts/MyPythonScripts/phantomjs.exe'
# chromeDriver = r'/Users/xxx/Scripts/MyPythonScripts/chromedriver.exe'
iterate = 15    #number of times to scroll down to load more pages

######################ENTER VARIABLES########################

conn = sqlite3.connect(sqliteDB)
cur = conn.cursor()

try:
    browser = webdriver.Chrome(chromeDriver)    #In windows, need to input path
    browser.get(r'https://www.instagram.com/explore/tags/{}/'.format(hashtag))

    #load all pages by clicking load more button and scrolling to bottom
    browser.find_element_by_link_text('LOAD MORE').click()
    for times in range(iterate):
        browser.execute_script("window.scrollTo(0, 100000)")
        time.sleep(1)

    #cooking the soup
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # get each post's urls, go into those urls and get the date
    tags = soup.select('a')
    for tag in tags:
        #get post urls
        link = tag.get('href')
        if link.find('tagged') > 1:
            link1 = link.find('?tagged')
            link2 = link[:link1]
            url = 'http://www.instagram.com{}'.format(link2)

            #cook soup for each post
            browser=webdriver.PhantomJS(PJ) #use Selenium and PhantomJS to parse js
            browser.get(url)
            html = browser.page_source.encode('utf-8')
            soup2 = BeautifulSoup(html, 'html.parser')

            #get photo caption
            things = soup2.select('ul li h1 span')
            if things is not None:
                caption = things[0].getText().replace('\n','').replace(',',' ').encode('utf')
            else:
                caption = None

            #get date
            locate = html.find('datetime')
            date = html[(locate+10):(locate+10+10)]
            print url, date

            cur.execute("INSERT OR IGNORE INTO main(posturl, caption, date, type) VALUES (?,?,?,'instagram')",(url, buffer(caption), date))
            conn.commit()

except:
    traceback.print_exc()
