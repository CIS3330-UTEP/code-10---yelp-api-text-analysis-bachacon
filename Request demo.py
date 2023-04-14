import requests
import urllib.parse
import json
import pandas as pd

search_term = "tacos"
search_term = urllib.parse.quote_plus(search_term)
location = "New York, NY"
location = urllib.parse.quote_plus(location)
sort_by = "rating"
limit = 20

url = f"https://api.yelp.com/v3/businesses/search?location={location}&term={search_term}&sort_by={sort_by}&limit={limit}"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer hy8_mc7NcYkgqLW2pfIeJMN3BO51gZCsNvBKbJfMfo3qWlVFet1y5L1C6eH1Gv4lOaYwsdPHiCx5hTShxqMBwKA4WT-XK4KbUcaZ3PhPTN84QNcwGXBURWLIwb82ZHYx"

}
response = requests.get(url, headers=headers)
response_json = json.loads(response.text)
print(response_json["businesses"])

results_df = pd.DataFrame.from_dict(response_json["businesses"])
print(results_df)
#results_df.to_csv("Requests_businesses_results.csv")


