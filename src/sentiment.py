from transformers import pipeline
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

#Download required resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

# Sentiment Analyzer class, Using DistilBERT (no neutral):
class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def analyze(self, texts):
        results = self.model(texts, truncation=True)
        return results

    @staticmethod
    def preprocess_text(text):
        tokens = word_tokenize(text.lower())
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
        return ' '.join(tokens)
    

# Sentiment Analyzer class, Using VADER (supports neutral):
class VADERSentimentAnalyzer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.sia = SentimentIntensityAnalyzer()

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        cleaned_tokens = [
            self.lemmatizer.lemmatize(token)
            for token in tokens
            if token.isalnum() and token not in self.stop_words
        ]
        return ' '.join(cleaned_tokens)

    def get_sentiment_and_score(self, text):
        scores = self.sia.polarity_scores(text)
        compound = scores['compound']
        if compound > 0.05:
            sentiment = 'positive'
        elif compound < -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        return sentiment, compound

    def analyze_dataframe(self, df, text_column='review'):
        df['processed_review'] = df[text_column].apply(self.preprocess_text)
        sentiment_results = df['processed_review'].apply(self.get_sentiment_and_score)
        df['sentiment_label'] = sentiment_results.apply(lambda x: x[0])
        df['sentiment_score'] = sentiment_results.apply(lambda x: x[1])
        return df
