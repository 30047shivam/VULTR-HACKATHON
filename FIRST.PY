from transformers import pipeline
from flask import Flask, request, jsonify

# Initialize the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

# Create a Flask web server
app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        # Get text data from the POST request
        data = request.get_json()
        text = data.get('text')

        # Analyze sentiment using the model
        result = sentiment_model(text)
        return jsonify({"sentiment": result[0]['label'], "confidence": result[0]['score']})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
