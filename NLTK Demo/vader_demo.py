from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
reviews = open('ice_cream_reviews.txt')

for review in reviews:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')
