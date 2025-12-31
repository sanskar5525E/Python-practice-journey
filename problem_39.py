with open("reviews.txt", "r") as file:
    reviews = file.readlines()

positive_words = ["good", "great", "useful", "quality", "love"]
negative_words = ["bad", "poor", "hate", "worst", "waste of time ", "delay"]

positive = 0
negative = 0
neutral = 0

for review in reviews:
    review_lower = review.lower()
    pos_count = 0
    neg_count = 0

    for word in positive_words:
        if word in review_lower:
            pos_count += 1

    for word in negative_words:
        if word in review_lower:
            neg_count += 1

    if pos_count > neg_count:
        positive += 1
    elif neg_count > pos_count:
        negative += 1
    else:
        neutral += 1


with open("report.txt", "w") as file:
    file.write(f"Total reviews: {len(reviews)}\n")
    file.write(f"positive reviews: {positive}\n")
    file.write(f"negative reviews: {negative}\n")
    file.write(f"neutral reviews: {neutral}\n")

print("Analysis complete.check report.txt")
