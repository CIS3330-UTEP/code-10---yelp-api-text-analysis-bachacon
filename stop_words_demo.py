import nltk
from nltk.corpus import stopwords 

stop_words = set(stopwords.words('english'))

reviews = open('ice_cream_reviews.txt')

for review in reviews:
    # print(review)
    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    new_text = []
    for tag in pos_tags:
        if tag[0] not in stop_words:
            print(tag[0])
            new_text.append(tag[0])

    print("\nOriginal")
    print(review)
    print("\nNew")
    print(" ".join(new_text))

    





