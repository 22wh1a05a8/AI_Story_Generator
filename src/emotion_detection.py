import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download required NLP resources
nltk.download('punkt')

def detect_emotion(user_input):
    """Classifies text into Positive, Negative, or Neutral emotions."""
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(user_input)

    # Classify emotion based on sentiment score
    if sentiment_score['compound'] >= 0.5:
        return "Positive"
    elif sentiment_score['compound'] <= -0.5:
        return "Negative"
    else:
        return "Neutral"

# Example Usage
if __name__ == "__main__":
    user_text = "I'm feeling nostalgic and joyful"
    detected_emotion = detect_emotion(user_text)
    print(f"Detected Emotion: {detected_emotion}")
