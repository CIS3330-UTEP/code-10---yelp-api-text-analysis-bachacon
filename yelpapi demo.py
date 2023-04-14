from yelpapi import YelpAPI
import pandas as pd

api_key = "hy8_mc7NcYkgqLW2pfIeJMN3BO51gZCsNvBKbJfMfo3qWlVFet1y5L1C6eH1Gv4lOaYwsdPHiCx5hTShxqMBwKA4WT-XK4KbUcaZ3PhPTN84QNcwGXBURWLIwb82ZHYx"

yelp_api = YelpAPI(api_key)

# Search_query
search_term = "pizza"
search_location = "Chicago, IL"
search_sort_by = "rating" # Best_match, Rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_term, location=search_location, sort_by=search_sort_by, limit=search_limit)
'''
print(search_results)

for i in search_results['businesses']:
    print(i['name'])
    print(i['alias'])
    print("\n")
'''

results_df = pd.DataFrame.from_dict(search_results['businesses'])
print(results_df["alias"])

#results_df.to_csv("YelpAPI.csv")
id_for_reviews = "montis-chicago"

# Reviews Query
reviews_results = yelp_api.reviews_query(id=id_for_reviews)
print(reviews_results)
'''
for review in reviews_results["reviews"]:
    print(review)
    print("\n\n")
'''

reviews_df = pd.DataFrame.from_dict(reviews_results['reviews'])
print(reviews_df["text"])