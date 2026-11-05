# requests provides the tools we need to send an HTTP request to an API.
import requests


def get_api_data(url):
    """Return parsed JSON from url, or None when the request or decoding fails."""

    # try runs these steps and lets the except blocks handle expected errors.
    try:
        response = requests.get(url, timeout=10) #Send a 'get' request to the URL. timeout=10 is how long to wait for a response before giving up.

        response.raise_for_status() # Gives an error for an unsuccessful HTTP status, such as 404 or 500.

        data = response.json()  # Convert the response's JSON text into Python data, such as a dictionary.
        return data
    
    except requests.exceptions.RequestException: # Handle request problems, including connection errors and HTTP errors.
        return None # None means we could not get usable data.
    
    except ValueError:
        return None # JSON decoding raises ValueError if the response is not valid JSON.
