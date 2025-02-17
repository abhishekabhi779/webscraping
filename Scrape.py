import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

def Scrape_webSite(Website):
    print("Scraping website: ", Website)

    # Path to your ChromeDriver executable
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU usage
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(Website)
        print("Scraping in progress...")
        time.sleep(5)  # Wait for the page to load fully

        # Locate car titles (adjust the XPath or CSS selector as needed)
        titles = driver.find_elements(By.CSS_SELECTOR, "div[role='article'] span[dir='auto']")

        # Extract text from the elements
        car_titles = [title.text for title in titles if title.text.strip()]
        print(f"Found {len(car_titles)} titles")

        # Save to Excel
        df = pd.DataFrame({"Car Titles": car_titles})
        excel_file = "car_titles.xlsx"
        df.to_excel(excel_file, index=False)
        print(f"Data saved to {excel_file}")

        return car_titles

    finally:
        driver.quit()
        print("Scraping completed.")
