import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def play_youtube_video(search_query):
    # Configure Chrome options for headless mode and allow autoplay
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")

    try:
        # Set up Chrome WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open YouTube and perform a search
        driver.get("https://www.youtube.com/")
        search_box = driver.find_element(By.CSS_SELECTOR, "input[id='search']")
        search_box.send_keys(search_query)
        search_box.submit()

        # Wait for search results to load
        time.sleep(5)

        # Click on the first video in the search results
        first_video = driver.find_element(By.CSS_SELECTOR, "a[id='video-title']")
        first_video.click()

        # Wait for the video player to load
        time.sleep(5)

        # Find the video player element
        video_player = driver.find_element(By.CSS_SELECTOR, "video")

        # Get the video URL
        video_url = video_player.get_attribute("src")

        # Print the video URL
        print("Playing video:", video_url)

        # Keep the script running to simulate background playback
        while True:
            time.sleep(10)  # Keep checking every 10 seconds

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the WebDriver session
        try:
            driver.quit()
        except NameError:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <search_query>")
        sys.exit(1)

    search_query = sys.argv[1]
    play_youtube_video(search_query)
