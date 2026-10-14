import json


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename
        self.favorites = {}

        # Open the saved file and turn its JSON text into Python data.
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                saved_data = json.load(file)

            # A favorites file should contain names and locations as strings.
            if isinstance(saved_data, dict):
                for name, location in saved_data.items():
                    if not isinstance(location, str):
                        self.favorites = {}
                        break
                    self.favorites[name.lower()] = location
        except (FileNotFoundError, ValueError):
            # A missing or corrupted file means we start with no favorites.
            self.favorites = {}

    def _save(self):
        # "w" replaces the old file with our updated dictionary.
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.favorites, file, indent=4)

    def add(self, name, location):
        name = name.lower()
        if name in self.favorites:
            return False

        self.favorites[name] = location
        self._save()
        return True

    def remove(self, name):
        name = name.lower()
        if name not in self.favorites:
            return False

        del self.favorites[name]
        self._save()
        return True

    def list_all(self):
        # Return a copy so callers cannot accidentally change our dictionary.
        return self.favorites.copy()

    def get_location(self, name):
        # get() returns None when the name is not in the dictionary.
        return self.favorites.get(name.lower())
