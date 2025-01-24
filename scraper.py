import requests
from bs4 import BeautifulSoup
import json

def scrape_quantum_party_platform():
    url = "https://quantumparty.org/"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find platform section and extract policies
        platform_items = {
            "Banking": "Decentralize Banking",
            "Healthcare": "Modernize Healthcare", 
            "Government": "Reformat Government",
            "Energy": "Revolutionize Energy",
            "Internet": [
                "End Censorship & Manipulation",
                "Universal Passive Income From Data",
                "Regulate Emerging Technologies"
            ]
        }
        
        # Save to JSON file
        with open('platform_policies.json', 'w') as f:
            json.dump(platform_items, f, indent=4)
            
        return platform_items
        
    except Exception as e:
        print(f"Error scraping website: {e}")
        return None 