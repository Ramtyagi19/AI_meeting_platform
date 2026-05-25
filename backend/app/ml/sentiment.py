from textblob import TextBlob

def get_sentiment(text: str):
    return TextBlob(text).sentiment.polarity