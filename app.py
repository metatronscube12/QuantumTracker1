from flask import Flask, render_template
import json
from newsapi import NewsApiClient
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Initialize News API client
newsapi = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

def check_policy_status(policy):
    """Check if policy has been achieved based on news articles"""
    try:
        # Get news from last 30 days
        to_date = datetime.now()
        from_date = to_date - timedelta(days=30)
        
        articles = newsapi.get_everything(
            q=policy,
            from_param=from_date.strftime('%Y-%m-%d'),
            to=to_date.strftime('%Y-%m-%d'),
            language='en',
            sort_by='relevancy'
        )
        
        # Simple heuristic: if there are articles with positive sentiment
        # mentioning policy implementation, mark as complete
        # This is a placeholder - you'd want more sophisticated analysis
        return len(articles['articles']) > 0
        
    except Exception as e:
        print(f"Error checking news for {policy}: {e}")
        return False

@app.route('/')
def index():
    # Load policies
    with open('platform_policies.json', 'r') as f:
        policies = json.load(f)
    
    # Check status of each policy
    policy_status = {}
    for category, items in policies.items():
        if isinstance(items, list):
            policy_status[category] = {
                item: check_policy_status(item) for item in items
            }
        else:
            policy_status[category] = {
                items: check_policy_status(items)
            }
    
    return render_template('index.html', policy_status=policy_status)

if __name__ == '__main__':
    app.run(debug=True) 