import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get_current_weather(self, location):
        url = self.base_url + "/current.json"
        params = {"key": self.api_key, "q": location}

        try:
            # Send the key and location as parameters; wait at most 10 seconds.
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            # Network, HTTP, and invalid JSON errors all mean no usable result.
            return None

    def get_forecast(self, location, days=3):
        if days < 1 or days > 3:
            raise ValueError("Forecast days must be between 1 and 3.")

        url = self.base_url + "/forecast.json"
        params = {"key": self.api_key, "q": location, "days": days}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None


def format_current_weather(data):
    # Pull each value out of the nested dictionaries before building the text.
    city = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_f"]
    condition = data["current"]["condition"]["text"]
    return f"{city}, {country}: {temperature}°F, {condition}"


def format_forecast(data):
    lines = []
    # Build one line for each day, then join the lines with newline characters.
    for forecast_day in data["forecast"]["forecastday"]:
        date = forecast_day["date"]
        high = forecast_day["day"]["maxtemp_f"]
        low = forecast_day["day"]["mintemp_f"]
        condition = forecast_day["day"]["condition"]["text"]
        lines.append(f"{date}: high {high}°F, low {low}°F, {condition}")
    return "\n".join(lines)
