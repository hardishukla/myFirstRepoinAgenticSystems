import requests

# API endpoint
url = "https://api.github.com/search/repositories"

# Query parameters
params = {
    "q": "python",        # search keyword
    "sort": "stars",     # sort by stars
    "order": "desc",     # descending order
    "per_page": 5        # limit to 5 results
}

# Send GET request
response = requests.get(url, params=params)

# Convert response to JSON
data = response.json()

# Extract and print required details
print("Top 5 Python Repositories:\n")

for repo in data["items"]:
    name = repo["name"]
    stars = repo["stargazers_count"]
    
    print(f"Repository Name: {name}")
    print(f"Stars: {stars}")
    print("-" * 30)