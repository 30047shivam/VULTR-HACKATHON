from transformers import pipeline

# Load a sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Test the model
text = "This is a wonderful platform for content!"
result = sentiment_pipeline(text)
print(result)  # Outputs: [{'label': 'POSITIVE', 'score': 0.9995}]
