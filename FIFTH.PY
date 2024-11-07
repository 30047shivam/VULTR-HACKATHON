@app.route('/dashboard', methods=['GET'])
def dashboard():
    sentiments = get_sentiments()
    data = [{'text': s.text, 'sentiment': s.sentiment} for s in sentiments]
    return jsonify(data)
