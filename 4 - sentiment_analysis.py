import pandas as pd
from textblob import TextBlob

# Load the CSV file
file_path = '/Users/store_kezhman/Desktop/UE/2nd semester /Big data analysis /sentiment_results.csv'
data = pd.read_csv(file_path)

# Display the column names to identify the correct column
print("Column names in the CSV file:", data.columns)

# Assuming the text data is in columns named 'keyword', 'datacreated', 'dataid', 'dataauthor'
# Combine the relevant columns into a single column for sentiment analysis
text_column_name = ['keyword', 'datacreated', 'dataid', 'dataauthor']
data['combined_text'] = data[text_column_name].astype(str).agg(' '.join, axis=1)

# Define the function for sentiment analysis
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Apply the sentiment analysis to the combined text column
data['sentiment'] = data['combined_text'].apply(get_sentiment)

# Save the results to a new CSV file
output_file_path = '/Users/store_kezhman/Desktop/sentiment_analysis_results.csv'
data.to_csv(output_file_path, index=False)

print("Sentiment analysis completed and saved to", output_file_path)
