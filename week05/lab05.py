def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when no valid ages are found."""
    total_age = 0  # Keep a running total of the valid ages.
    age_count = 0  # Count how many valid ages were added.

    for user in users:
        # Read the age only when the dictionary contains an age key.
        if "age" in user:
            age = user["age"]

            # Booleans are technically integers in Python, but are not ages.
            if isinstance(age, (int, float)):
                if not isinstance(age, bool):
                    total_age += age  # Add this valid age to the running total.
                    age_count += 1  # Include this age in the number being averaged.

    # Avoid dividing by zero when the list has no valid ages.
    if age_count == 0:
        return 0.0

    return total_age / age_count  # Divide the total by the number of valid ages.


def get_active_user_emails(users):
    """Return email addresses for users whose is_active value is truthy."""
    active_emails = []  # Store email addresses that meet both requirements.

    for user in users:
        # Include the email only if the user is active and has an email key.
        if user.get("is_active") and "email" in user:
            active_emails.append(user["email"])

    return active_emails  # This is an empty list when no emails were found.
