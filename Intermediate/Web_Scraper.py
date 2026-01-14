import requests
from bs4 import BeautifulSoup

try:
    # 1. Website URL (you can change to ShadowFox site if given)
    url = "https://example.com"

    # 2. Get website data
    response = requests.get(url)
    response.raise_for_status()

    # 3. Read HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. Extract data (website title)
    title = soup.title.text

    # 5. Save data to file
    with open("data.txt", "w") as file:
        file.write("Website Title:\n")
        file.write(title)

    print("Data scraped and saved successfully!")

except requests.exceptions.RequestException as e:
    print("Error occurred while scraping:", e)
