import os
import requests

def fetch_data():
    # Step 1: Get API key from environment variable
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API key not found in environment variables.")
        return

    # Step 2: Define API endpoint
    url = "https://api.example.com/data"

    # Step 3: Set headers with Bearer token
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        # Step 4: Send GET request
        response = requests.get(url, headers=headers)

        # Step 5: Handle status codes
        if response.status_code == 200:
            print("Success! Data received:")
            print(response.json())

        elif response.status_code == 429:
            print("Rate limit reached. Try again later.")

        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:")
        print(e)


# Run the function
if __name__ == "__main__":
    fetch_data()