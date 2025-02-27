﻿# webscraping
# Web Scraper Project

A Streamlit-based web application that allows users to scrape car listing titles from websites using Selenium.

## Overview

This project provides a simple web interface built with Streamlit that enables users to enter a URL and scrape car titles from the page. The application uses Selenium WebDriver to navigate to the website, extract title information, and save the results to an Excel file.

## Features

- **User-friendly Interface**: Clean Streamlit UI for entering URLs and viewing results
- **Headless Browsing**: Uses Chrome in headless mode for efficient scraping
- **Data Export**: Automatically saves scraped data to an Excel file
- **Error Handling**: Provides clear error messages when scraping fails

## Requirements

- Python 3.6+
- Chrome browser
- ChromeDriver (matching your Chrome version)

## Dependencies

- Selenium
- Streamlit
- Pandas
- Time (standard library)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/web-scraper.git
   cd web-scraper
   ```

2. Install the required packages:
   ```
   pip install selenium streamlit pandas
   ```

3. Download the appropriate [ChromeDriver](https://sites.google.com/chromium.org/driver/) for your Chrome version and place it in the project root directory.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Enter the URL of the website you want to scrape in the input field

4. Click the "Scrape" button to start the scraping process

5. View the results in the expandable section and check the "car_titles.xlsx" file for the saved data

## Project Structure

- `main.py`: The Streamlit application that provides the user interface
- `Scrape.py`: Contains the scraping logic using Selenium
- `chromedriver.exe`: Chrome WebDriver executable (not included, must be downloaded separately)
- `car_titles.xlsx`: Output file where scraped data is saved

## How It Works

1. The user enters a URL in the Streamlit interface
2. When the "Scrape" button is clicked, the application calls the `Scrape_webSite` function
3. Selenium opens a headless Chrome browser and navigates to the provided URL
4. The script searches for car titles using the specified CSS selector
5. The titles are extracted, processed, and saved to an Excel file
6. The results are displayed in the Streamlit interface

## Limitations

- The current implementation is specifically designed to scrape car titles using a specific CSS selector
- The script includes a fixed 5-second wait time, which may need adjustment for slower-loading websites
- The scraper runs in headless mode, so you won't see the browser interface during operation

## Future Improvements

- Add support for different types of content beyond car titles
- Implement customizable CSS selectors through the UI
- Add pagination support for multi-page scraping
- Include more advanced filtering options
- Add proxy support for avoiding IP restrictions

## Legal Considerations

Web scraping may be subject to legal restrictions. Always:
- Check the website's robots.txt file and terms of service before scraping
- Respect rate limits and don't overload servers
- Be aware that some websites explicitly prohibit scraping
- Use the scraped data responsibly and in accordance with applicable laws

## License

This project is licensed under the MIT License - see the LICENSE file for details.
