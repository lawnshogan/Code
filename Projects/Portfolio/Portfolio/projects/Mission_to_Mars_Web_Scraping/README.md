# Mission-to-Mars
Mission to Mars - Web Scraping with HTML/CSS

## Main Objectives
1. Gain familiarity with and use HTML elements, as well as class and id attributes, to identify content for web scraping.
2. Use BeautifulSoup and Splinter to automate a web browser and perform a web scrape.
3. Create a MongoDB database to store data from the web scrape.
4. Create a web application with Flask to display the data from the web scrape.
5. Create an HTML/CSS portfolio to showcase projects.
6. Use Bootstrap components to polish and customize the portfolio.

## Data Environment
1.  BeautifulSoup4 4.9.3
2.  Bootstrap 3.3.7
3.  DateTime 4.3
4.  Flask 1.1.2
5.  Flask-PyMongo 2.3.0
6.  html5lib 1.1
7.  Jupyter Notebook 6.1.4
8.  MongoDB 4.4.2
9.  Numpy 1.19.3***
10. Pandas 1.1.4
11. PyMongo 3.11.2
12. Splinter 0.14.0
13. webdriver-manager 3.2.2
* ***A higher version prevented Flask from running.

# Web Scraping Mars data from NASA using Jupyter Notebook
BeautifulSoup and Splinter were used to automate a web browser and perform a web scrape.

## Mars Hemisphere data dictionary
![Pic 1](https://github.com/Baylex/Mission-to-Mars/blob/main/Resources/hemi_dict.PNG)

# Using MongoDB and Flask to display the data as HTML/CSS
MongoDB database was used to store data from the web scrape, and then a web application was created with Flask to display the data from the web scrape.

The Python code from the scraping file may differ slightly from the Jupyter Notebook Mission to Mars Challenge file.  Some variables needed to be changed to match other files. 

## Final code in the scraping file:
![Pic 2](https://github.com/Baylex/Mission-to-Mars/blob/main/Resources/code_top.PNG)
![Pic 3](https://github.com/Baylex/Mission-to-Mars/blob/main/Resources/code_bottom.PNG)

## Scraping Success:
![Pic 4](https://github.com/Baylex/Mission-to-Mars/blob/main/Resources/Successful_scrape.PNG)

## Website after scraping:
![Pic 5](https://github.com/Baylex/Mission-to-Mars/blob/main/Resources/website_top.PNG)
![Pic 6](https://github.com/Baylex/Mission-to-Mars/blob/main/Resources/website_bottom.PNG)

# Using Bootstrap 3 to modify the html file
## The webpage is mobile-responsive
Changed everything to col-xs, which is the smallest option.  Everything will scale up from the mobile phones size to the larger desktop sizes. 

## Two additional Bootstrap 3 components are used to style the webpage
1. Changed the button color to warning, which is orange to match the header color.
2. Added a tooltip that says Click Me!, when the user hoovers over the Scrape button.
3. Bonus: Changed the colors of various areas, adjusted some heights, and added a striped table pattern.
