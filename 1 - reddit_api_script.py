import requests
import json

# Reddit API credentials
CLIENT_ID = 'U9-eTs10P3l3DQ5ZICHw8w'
CLIENT_SECRET = 'CjhHMBIzvQ-wUtMmXVhqD8LRHMl5zA'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
USERNAME = 'goldfishnightmare'
PASSWORD = 'Bigdata@123'

# Get access token
def get_access_token():
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    headers = {'User-Agent': USER_AGENT}
    data = {'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD}

    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, headers=headers, data=data)

    # Log the response for debugging
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    response.raise_for_status()  # Raise an error on a bad request
    response_json = response.json()

    if 'access_token' in response_json:
        return response_json['access_token']
    else:
        raise Exception("Access token not found in the response")


# Search posts
def search_reddit(query):
    token = get_access_token()
    headers = {'Authorization': f'bearer {token}', 'User-Agent': USER_AGENT}
    params = {'q': query, 'limit': 100}
    response = requests.get('https://oauth.reddit.com/r/all/search', headers=headers, params=params)
    response.raise_for_status()  # Raise an error on a bad request
    return response.json()


# Main execution
if __name__ == '__main__':
    search_query = 'nio'
    try:
        result = search_reddit(search_query)
        print(json.dumps(result, indent=4))  # Pretty print the JSON response
    except Exception as e:
        print("Error:", str(e))
