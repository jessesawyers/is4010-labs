# The json module converts between Python data and JSON text.
import json


def save_contacts_to_json(contacts, filename):
    """Write the contacts list to filename as indented JSON."""
    # "w" opens the file for writing, creating it or replacing its old contents.
    # "with" automatically closes the file when this block finishes.
    # UTF-8 lets the file store names that contain accented letters.
    with open(filename, "w", encoding="utf-8") as contact_file:
        # dump writes the Python list to the file as JSON.
        # indent=4 adds spaces and line breaks to make the JSON easy to read.
        json.dump(contacts, contact_file, indent=4)


def load_contacts_from_json(filename):
    """Return contacts from filename, or an empty list if it does not exist."""
    # try lets us handle the missing-file error if opening the file fails.
    try:
        # "r" opens the file for reading. "with" closes it automatically.
        with open(filename, "r", encoding="utf-8") as contact_file:
            # load reads JSON from the file and converts it back to Python data.
            contacts = json.load(contact_file)
            return contacts
    except FileNotFoundError:
        # If no contact file exists yet, start with an empty list.
        return []
