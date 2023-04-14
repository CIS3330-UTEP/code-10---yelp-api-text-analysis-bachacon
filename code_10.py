import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from yelpapi import YelpAPI
import pandas as pd

api_key = "hy8_mc7NcYkgqLW2pfIeJMN3BO51gZCsNvBKbJfMfo3qWlVFet1y5L1C6eH1Gv4lOaYwsdPHiCx5hTShxqMBwKA4WT-XK4KbUcaZ3PhPTN84QNcwGXBURWLIwb82ZHYx"
yelp_api = YelpAPI(api_key)


# Search Query
searh_term = "ramen"
search_location = "New York, NY"
search_by_rating = "rating"
search_limit = 20

search_results = yelp_api.search_query(term=searh_term, location=search_location, 
                                       sort_by=search_by_rating, limit=search_limit)

print(search_results)

## Create DataFrame ##

results_df = pd.DataFrame.from_dict(search_results['businesses'])
print(results_df)







## Getting reviews from 5 businesses ##
length = int(input("\nEnter the number of iterations: "))
review_lists = [[] for _ in range(length)]

## Adding vader sentiment and stopwords##
analyzer = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))


for i in range(length):
    id_for_review = input("\nEnter the business alias: ").strip()

    try:
        reviews_results = yelp_api.reviews_query(id=id_for_review)
        review_df = pd.DataFrame.from_dict(reviews_results['reviews'])

        review_texts = review_df["text"].tolist()
        for text in review_texts:
            tokens = nltk.word_tokenize(text)
            tokens_without_stopwords = [token for token in tokens if token.lower() not in stop_words]
            review_lists[i].extend(tokens_without_stopwords)

            sentiment = analyzer.polarity_scores(text)
            print(f"Review Text: {text}")
            print(f"Tokens: {tokens}")
            print(f"Tokens without Stop Words: {tokens_without_stopwords}")
            print(f"Sentiment - Positive: {sentiment['pos']}, Negative: {sentiment['neg']}, Neutral: {sentiment['neu']}, Compound: {sentiment['compound']}")
            print()

    except Exception as e:
        print("Error:", e)
        print("Skipping to next iteration")
        continue

for i, review_list in enumerate(review_lists, start=1):
    print(f"\nReview List {i}:", review_list)
    



