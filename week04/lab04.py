def find_common_elements(list1, list2):
    """Return a list of values present in both input lists."""
    if not list1 or not list2:
        return []

    common_elements = [] ## create an empty list to store common elements
    seen = set() ## create a set to keep track of seen elements (to avoid duplicates)

    for item in list1:
        if item in list2 and item not in seen: ## check if the item is in both lists and not already added to the common_elements
            common_elements.append(item)
            seen.add(item)

    return common_elements


def find_user_by_name(users, name):
    """Return the matching user dictionary, or None when no user matches."""
    if not users:
        return None

    ## check if the user is a dictionary and if the name matches.'isinstance' checks if the user is a dictionary, and 'get' retrieves the value for the key "name" safely.
    for user in users:
        if isinstance(user, dict) and user.get("name") == name: 
            return user

    return None


def get_list_of_even_numbers(numbers):
    """Return the even integers in their original order."""
    ## check if the input list is empty. If it is, return an empty list.
    if not numbers:
        return []

    even_numbers = []

    for number in numbers: 
        if number % 2 == 0: ## checks if the number is divisable by 2 and checks the remainder. If the remainder is 0, it means the number is even.
            even_numbers.append(number)

    return even_numbers