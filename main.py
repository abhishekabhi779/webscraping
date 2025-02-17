import streamlit as st
from Scrape import Scrape_webSite

# Title for the Streamlit application
st.title('Web Scraper')

# Input field for the user to provide a URL
url = st.text_input('Enter the URL:')

# Button to initiate scraping
if st.button('Scrape'):
    st.write(f"Scraping the website: {url}...")
    
    try:
        # Call the scraping function and get the HTML content
        result = Scrape_webSite(url)
        st.success("Scraping completed successfully!")
        
        # Display the HTML content in an expandable section
        with st.expander("Scraped HTML"):
            st.code(result, language='html')
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
