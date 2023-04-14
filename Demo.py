import nltk

reviews = open("tacos_reviews.txt")

for line in reviews:
    tokens = nltk.word_tokenize(line)
    pos_tags = nltk.pos_tag(tokens)
    #print(pos_tags)
    for tag in pos_tags:
        if tag[1] == "JJ" or tag[1] == "JJS":
            print(tag[0])

   