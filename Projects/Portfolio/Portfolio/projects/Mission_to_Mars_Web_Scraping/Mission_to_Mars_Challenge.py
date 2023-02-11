# downloaded from Jupyter notebook and cleaned
# Module Code-------------------------------------------------------------------------
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)

## 10.3.3 Scrape Mars Data: The News--------------------------------------------------
# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
#url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# set up HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
# add the find element, find(where to look, key word = give it a name)
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

## 10.3.4 Scrape Mars Data: Featured Image-----------------------------------------------
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/'
browser.visit(url)
# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()
# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

## 10.3.5 Scrape Mars Data: Mars Facts--------------------------------------------------
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df
df.to_html()
browser.quit()

# Challenge Code-------------------------------------------------------------------------
# # Path to chromedriver (for MacOS users, mine is PC)
# !which chromedriver

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)

### Visit the NASA Mars News Site--------------------------------------------------------
# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

### JPL Space Images Featured Image------------------------------------------------------
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

### Mars Facts-----------------------------------------------------------------------
df = pd.read_html('http://space-facts.com/mars/')[0]
df.head()
df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df
df.to_html()

### Mars Weather----------------------------------------------------------------------
# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')

# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())
browser.quit()

# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles----------------------
# ### Hemispheres
# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)

# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Parse the html with beautifulsoup
html = browser.html
hemi_soup = soup(html, 'html.parser')

# Get the links for each of the 4 hemispheres
hemi_links = hemi_soup.find_all('h3')
# hemi_links

# loop through each hemisphere link
for hemi in hemi_links:
    # Navigate and click the link of the hemisphere
    img_page = browser.find_by_text(hemi.text)
    img_page.click()
    html= browser.html
    img_soup = soup(html, 'html.parser')
    # Scrape the image link
    img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])
    # Scrape the title
    title = img_soup.find('h2', class_='title').text
    # Define and append to the dictionary
    hemi_dict = {'img_url': img_url,'title': title}
    hemisphere_image_urls.append(hemi_dict)
    browser.back()
# print(hemisphere_image_urls)

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()
