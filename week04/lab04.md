
# Lab 04: Data structures

**Due:** Sunday at 11:59 PM  
**Points:** 10

Use lists, dictionaries, sets, and iteration to select an appropriate representation for each problem. Ask an AI assistant to explain its recommended data structure before you implement the function, but your submitted deliverable is the tested Python file.

## Deliverable

Create `week04/lab04.py`. Do not create or modify test files.

## Functions

```python
def find_common_elements(list1, list2):
    """Return a list of values present in both input lists."""


def find_user_by_name(users, name):
    """Return the matching user dictionary, or None when no user matches."""


def get_list_of_even_numbers(numbers):
    """Return the even integers in their original order."""
```

Requirements:

- The order returned by `find_common_elements` does not matter.
- `find_user_by_name` receives a list of dictionaries containing a `name` key.
- Empty inputs must return an empty list or `None`, as appropriate.
- Zero and negative even numbers must be retained.

## Test locally

```bash
uv run --directory week04 python -m pytest tests/ -v
```

## Submit

```bash
git add week04/lab04.py
git commit -m "Complete Lab 04"
git push origin main
```

A green Week 04 badge earns 10 points.
