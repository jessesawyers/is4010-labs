import argparse
import os
from pathlib import Path
import sys

# Imports differ when running a file directly versus importing it as a package.
if __package__:
    from .favorites import FavoritesManager
    from .weather_api import WeatherAPI, format_current_weather, format_forecast
else:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast


# Keep the saved favorites beside this script, regardless of where it is run.
FAVORITES_FILE = Path(__file__).parent / "favorites.json"


def load_api_key():
    # An environment variable takes priority over a local configuration file.
    api_key = os.environ.get("WEATHER_API_KEY")
    if api_key:
        return api_key

    try:
        if __package__:
            from .config import WEATHER_API_KEY
        else:
            from config import WEATHER_API_KEY
    except ImportError:
        return None

    # The example placeholder is not a real API key.
    if not WEATHER_API_KEY or WEATHER_API_KEY == "YOUR_API_KEY_HERE":
        return None
    return WEATHER_API_KEY


def build_parser():
    parser = argparse.ArgumentParser(description="Look up weather and save favorites.")
    # Subparsers let each command have its own arguments.
    commands = parser.add_subparsers(dest="command", required=True)

    current = commands.add_parser("current", help="Show current weather")
    current.add_argument("location")

    forecast = commands.add_parser("forecast", help="Show a weather forecast")
    forecast.add_argument("location")
    forecast.add_argument("--days", type=int, choices=[1, 2, 3], default=3)

    favorites = commands.add_parser("favorites", help="Manage saved locations")
    favorite_commands = favorites.add_subparsers(
        dest="favorites_command", required=True
    )
    add = favorite_commands.add_parser("add", help="Save a location")
    add.add_argument("name")
    add.add_argument("location")
    favorite_commands.add_parser("list", help="List saved locations")
    remove = favorite_commands.add_parser("remove", help="Remove a location")
    remove.add_argument("name")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    favorites = FavoritesManager(FAVORITES_FILE)

    # Favorite commands only use the local file, so they need no API key.
    if args.command == "favorites":
        if args.favorites_command == "add":
            if not favorites.add(args.name, args.location):
                print("That favorite already exists.", file=sys.stderr)
                return 1
            print(f"Added favorite: {args.name}")
        elif args.favorites_command == "remove":
            if not favorites.remove(args.name):
                print("That favorite does not exist.", file=sys.stderr)
                return 1
            print(f"Removed favorite: {args.name}")
        else:
            for name, location in favorites.list_all().items():
                print(f"{name}: {location}")
        return 0

    api_key = load_api_key()
    if not api_key:
        print("Missing API key. Set WEATHER_API_KEY or use config.py.", file=sys.stderr)
        return 1

    # Use the saved location if the argument matches a favorite name.
    location = favorites.get_location(args.location)
    if location is None:
        location = args.location

    api = WeatherAPI(api_key)
    if args.command == "current":
        data = api.get_current_weather(location)
    else:
        data = api.get_forecast(location, days=args.days)

    if data is None:
        print("Could not retrieve weather. Please try again.", file=sys.stderr)
        return 1

    if args.command == "current":
        print(format_current_weather(data))
    else:
        print(format_forecast(data))
    return 0


if __name__ == "__main__":
    # Pass main's result to the terminal: 0 means success, 1 means failure.
    sys.exit(main())
