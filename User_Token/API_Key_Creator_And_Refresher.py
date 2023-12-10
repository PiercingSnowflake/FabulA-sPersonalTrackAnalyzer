import requests
import json
from base64 import b64encode
from datetime import datetime, timedelta


def save_token_info(token_info, filename='token_info.json'):
    with open(filename, 'w') as file:
        json.dump(token_info, file)

def load_token_info(filename='token_info.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def get_spotify_access_token(client_id, client_secret):
    # Spotify API endpoint for obtaining access token
    token_url = 'https://accounts.spotify.com/api/token'

    # Base64 encode the client ID and client secret
    credentials = b64encode(f'{client_id}:{client_secret}'.encode()).decode('utf-8')

    # Request headers
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Request body
    data = {
        'grant_type': 'client_credentials',
    }

    # Make the request to obtain the access token
    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
        # Successful response
        token_info = response.json()
        access_token = token_info.get('access_token')
        expires_in = token_info.get('expires_in', 3600)  # Default expiration time is 1 hour
        expiration_time = datetime.now() + timedelta(seconds=expires_in)
        print(f"Access Token: {access_token}")
        print(f"Expiration Time: {expiration_time}")

        # Save token info to a JSON file
        save_token_info({'access_token': access_token, 'expiration_time': expiration_time.isoformat()})

        return access_token, expiration_time
    else:
        # Error handling
        print(f"Error: {response.status_code}, {response.text}")
        return None, None


# Example usage
with open("Client_Data.json", "r", encoding = "utf-8") as file:
    data = json.load(file)
    client_id = data["Client ID"]
    client_secret = data["Client secret"]

token_info = load_token_info()

# Check if the loaded token is still valid
if token_info and 'access_token' in token_info and 'expiration_time' in token_info:
    expiration_time = datetime.fromisoformat(token_info['expiration_time'])
    if datetime.now() < expiration_time:
        # Token is still valid, use the existing token
        access_token = token_info['access_token']
        print(f"Using existing access token: {access_token}")
    else:
        # Token has expired, refresh the token
        access_token, expiration_time = get_spotify_access_token(client_id, client_secret)
else:
    # No existing token or the token has expired, obtain a new one
    access_token, expiration_time = get_spotify_access_token(client_id, client_secret)