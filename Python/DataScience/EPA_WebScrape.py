from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Step 1: Install Selenium and necessary web driver (e.g. ChromeDriver)
# Step 2: Import Selenium and necessary libraries

# Step 3: Use Selenium to open a web browser and navigate to the website
driver = webdriver.Chrome()
driver.get("https://ghgdata.epa.gov/ghgp/main.do#/facility/?q=Find%20a%20Facility%20or%20Location&st=CO&bs=&et=PE&fid=&sf=11001100&lowE=-20000&highE=23000000&g1=1&g2=1&g3=1&g4=1&g5=1&g6=0&g7=1&g8=1&g9=1&g10=1&g11=1&g12=1&s1=1&s2=1&s3=1&s4=1&s5=1&s6=1&s7=1&s8=1&s9=1&s10=1&s201=1&s202=1&s203=1&s204=1&s301=1&s302=1&s303=1&s304=1&s305=1&s306=1&s307=1&s401=1&s402=1&s403=1&s404=1&s405=1&s601=1&s602=1&s701=1&s702=1&s703=1&s704=1&s705=1&s706=1&s707=1&s708=1&s709=1&s710=1&s711=1&s801=1&s802=1&s803=1&s804=1&s805=1&s806=1&s807=1&s808=1&s809=1&s810=1&s901=1&s902=1&s903=1&s904=1&s905=1&s906=1&s907=1&s908=1&s909=1&s910=1&s911=1&si=&ss=&so=0&ds=E&yr=2021&tr=current&cyr=2021&ol=0&sl=0&rs=ALL")

# Step 4: Use Selenium to interact with the website elements
select_year = Select(driver.find_element_by_id("reportingYear"))

# Step 5: Use a loop to select and download data for each year
for year in select_year.options:
    select_year.select_by_value(year.get_attribute("value"))
    # Step 5.1: Wait for page to load
    time.sleep(5)
    # Step 5.2: Use Selenium to click the download button
    driver.find_element_by_id("exportButton").click()
    # Step 5.3: Wait for download to complete
    time.sleep(5)
    # Step 5.4: Use a library such as pandas to read the downloaded file and combine it
    data = pd.read_excel(f"{year.get_attribute('value')}.xlsx")
    if 'all_data' not in locals():
        all_data = data
    else:
        all_data = pd.concat([all_data, data], ignore_index=True)

# Step 7: Save the combined data to a single excel file
all_data.to_excel("combined_data.xlsx", index=False)

# Step 8: Close the web browser
driver.quit()
