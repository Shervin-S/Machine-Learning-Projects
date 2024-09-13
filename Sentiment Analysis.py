# Import necessary libraries
import nltk
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Get sentiment polarity (-1 to 1)

    # Determine the sentiment category
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Main program to take user input and predict sentiment
if __name__ == "__main__":
    # Get input from the user
    user_input = input("Enter text to analyze its sentiment: ")

    # Analyze the sentiment of the input text
    sentiment = analyze_sentiment(user_input)

    # Output the result
    print(f"\nSentiment of the given text: {sentiment}")