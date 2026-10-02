from datetime import date


class Book:
    def __init__(self, title, author, year):
        # Save each value on this book so the other methods can use it.
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Return readable text that includes all the book's information.
        return f"{self.title} by {self.author} ({self.year})"

    def get_age(self):
        """Return the number of years since publication."""
        current_year = date.today().year
        return current_year - self.year


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        # Reuse Book's constructor to set the title, author, and year.
        super().__init__(title, author, year)

        # An ebook has one extra value that a regular book does not have.
        self.file_size = file_size

    def __str__(self):
        # Add the file size to the readable information provided by Book.
        return f"{super().__str__()} - {self.file_size} MB"
