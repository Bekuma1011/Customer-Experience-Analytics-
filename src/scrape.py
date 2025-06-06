from google_play_scraper import reviews_all, Sort
import pandas as pd
import os

class ReviewScraper:
    def __init__(self, apps):
        self.apps = apps
        self.reviews = []

    def fetch_reviews(self, lang="en", country="et", sort=Sort.NEWEST, count=400):
        for bank, app_id in self.apps.items():
            print(f"Fetching reviews for {bank}...")
            data = reviews_all(
                app_id,
                lang=lang,
                country=country,
                sort=sort,
            )
            for item in data[:count]:
                self.reviews.append({
                    "review": item.get("content"),
                    "rating": item.get("score"),
                    "date": item.get("at"),
                    "bank": bank,
                    "source": "Google Play"
                })

    def save_to_csv(self, filepath):
        df = pd.DataFrame(self.reviews)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Saved scraped data to {filepath}")
