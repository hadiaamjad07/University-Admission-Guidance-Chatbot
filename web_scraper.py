import requests
from bs4 import BeautifulSoup

urls = [
    "https://en.wikipedia.org/wiki/University",
    "https://en.wikipedia.org/wiki/Scholarship",
    "https://en.wikipedia.org/wiki/Higher_education"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_text = ""

for url in urls:
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        page_text = " ".join(
            p.get_text(" ", strip=True)
            for p in paragraphs
        )

        all_text += page_text + "\n\n"

        print("Scraped:", url)

    except Exception as e:
        print("Failed:", url)
        print(e)

with open("training_data.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Dataset Created Successfully")