from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import csv
import time

# Set up the Chrome WebDriver
chromedriver_path = r'C:\WebDrivers\chromedriver-win64\chromedriver.exe'
service = Service(chromedriver_path)

# driver = webdriver.Chrome(service=service, options=chrome_options)


options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
url = "https://www.getyourguide.com/puerto-rico-l169159/"
driver.get(url)

def click_button():
    # Set a counter for 'show more' clicks
    show_more_clicks = 0
    last_height = driver.execute_script("return document.body.scrollHeight")

    # Loop until 'show more' is clicked 10 times or no new elements are loaded
    while show_more_clicks < 10:
        # Scroll down until no new elements are loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Add a slight pause after scrolling (adjust as needed)

        # Look for the 'show more' button and click it (adjust selector if needed)
        try:
            show_more_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='c-button c-button--medium c-button--outlined-standard']")))
            show_more_button.click()
            show_more_clicks += 1
            print(f"'Show More' button clicked {show_more_clicks} times")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error clicking 'Show More' button or button not found: {e}")
            # Handle cases where button might not exist or takes longer to load

    # ... rest of your code to scrape tour information ...

    return

click_button()


# Function to scrape tour information
def scrape_tours():
    tours = []
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_attempts = 0
    max_scroll_attempts = 10

    while scroll_attempts < max_scroll_attempts:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for 2 seconds after each scroll
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'activity-card-block activity-card-block--grid')]")))
        except TimeoutException:
            print(f"Timeout waiting for new elements. Attempt {scroll_attempts + 1}/{max_scroll_attempts}")
            scroll_attempts += 1
            continue

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scroll_attempts = 0  # Reset scroll attempts if successful

    # Wait for a longer time after scrolling is complete
    time.sleep(5)

    tour_elements = driver.find_elements(By.XPATH, ".//div[contains(@class, 'activity-card-block activity-card-block--grid')]")
    print(f"Found {len(tour_elements)} tour elements")

    if len(tour_elements) == 0:
        print("No tour elements found. Printing page source:")
        print(driver.page_source)

    for index, tour in enumerate(tour_elements):
        try:
            activity = WebDriverWait(tour, 5).until(
                EC.presence_of_element_located((By.XPATH, ".//h3[contains(@class, 'text-atom text-atom--title-4 vertical-activity-card__title')]"))
            ).text.strip()

            price = WebDriverWait(tour, 5).until(
                EC.presence_of_element_located((By.XPATH, ".//span[contains(@class, 'c-text-atom c-text-atom--body-compact-strong activity-price__text-price')]"))
            ).text.strip()

            rating = WebDriverWait(tour, 5).until(
                EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'c-activity-rating__rating')]"))
            ).text.strip()

            reviews = WebDriverWait(tour, 5).until(
                EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'c-activity-rating__label')]"))
            ).text.strip().strip('()')

            # Find the link within the div tag
            link = WebDriverWait(tour, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, ".//div[@class='vertical-activity-card__content-wrapper']//a"))
            ).get_attribute('href')

            print(f"Tour {index + 1}:")
            print(f"Activity: {activity}")
            print(f"Link: {link}")
            print(f"Price: {price}")
            print(f"Rating: {rating}")
            print(f"Reviews: {reviews}")

            print("---")

            tours.append({"activity": activity, "price": price, "link": link, "rating": rating, "reviews": reviews})
            # tours.append({"title": title, "price": price})
        except Exception as e:
            print(f"Error processing tour {index + 1}: {str(e)}")

    return tours

# Scrape the tours
tours = scrape_tours()

# Close the browser
driver.quit()

# Write the data to a CSV file
csv_file_path = r"C:[Add your path here for .csv output]"

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['activity', 'price', 'link', 'rating', 'reviews']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(tours)