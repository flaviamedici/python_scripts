# Install dependency
# pip install slack_sdk


import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random

# --- Configuration ---
SLACK_BOT_TOKEN = "YOUR_SLACK_BOT_TOKEN"  # Starts with xoxb-
SLACK_CHANNEL = "#your-channel-name"       # e.g., #friends-motivation or a user ID like @username

# --- Function to get a random quote ---
def get_random_quote():
    try:
        # Using a free quote API
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status() # Raise an exception for HTTP errors
        quote_data = response.json()
        
        quote = quote_data['content']
        author = quote_data['author']
        return f"*{quote}*\n- {author}"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        # Fallback quote if API fails
        return "The only way to do great work is to love what you do. - Steve Jobs"

# --- Function to send message to Slack ---
def send_slack_message(message):
    client = WebClient(token=SLACK_BOT_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=message
        )
        print(f"Message sent to Slack: {response['ts']}")
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")

# --- Main automation logic ---
if __name__ == "__main__":
    motivational_quote = get_random_quote()
    
    # Customize the message
    full_message = f"Good morning, team! Here's some motivation for your day:\n\n{motivational_quote}"
    
    send_slack_message(full_message)