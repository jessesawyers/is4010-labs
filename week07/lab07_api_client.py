# requests provides the tools we need to send an HTTP request to an API.
import requests


def get_api_data(url):
    """Return parsed JSON from url, or None when the request or decoding fails."""
    # try runs these steps and lets the except blocks handle expected errors.
    try:
        # Send a GET request to the supplied URL to ask for data.
        # timeout=10 limits how long requests waits for a connection or data.
        response = requests.get(url, timeout=10)

        # Raise an error for an unsuccessful HTTP status, such as 404 or 500.
        response.raise_for_status()

        # Convert the response's JSON text into Python data, such as a dictionary.
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        # Handle request problems, including connection errors and HTTP errors.
        # None means we could not get usable data.
        return None
    except ValueError:
        # JSON decoding raises ValueError if the response is not valid JSON.
        return None
