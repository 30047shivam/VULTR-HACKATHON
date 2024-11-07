def save_sentiment(text, sentiment):
    new_sentiment = Sentiment(text=text, sentiment=sentiment)
    session.add(new_sentiment)
    session.commit()

def get_sentiments():
    return session.query(Sentiment).all()
