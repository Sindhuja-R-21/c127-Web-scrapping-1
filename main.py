from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("C:/Users/HP/Downloads/PRO-C127-Reference-Code-main/chromedriver.exe")


browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    












    
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
