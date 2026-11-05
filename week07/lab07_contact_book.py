# The json module converts between Python data and JSON text.
import json


def save_contacts_to_json(contacts, filename):
    """Write the contacts list to filename as indented JSON."""

    with open(filename, "w", encoding="utf-8") as contact_file:     # "w" opens the file for writing. "with" closes it automatically. UTF-8 lets the file store names that contain accented letters.        
        json.dump(contacts, contact_file, indent=4)                 # dump writes the Python list to the file as JSON.


def load_contacts_from_json(filename):
    """Return contacts from filename, or an empty list if it does not exist."""

    # try lets us handle the missing-file error if opening the file fails.
    try:        
        with open(filename, "r", encoding="utf-8") as contact_file:     # "r" opens the file for reading. "with" closes it automatically.
            contacts = json.load(contact_file)                          # load reads JSON from the file and converts it back to Python data.
            return contacts
    except FileNotFoundError:
        return []      # If no contact file exists yet, start with an empty list.
