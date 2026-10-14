class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """Add a book title to the library collection."""
        self.books.append(book)

    def remove_book(self, book_title):
        """Remove a book title if it exists in the collection."""
        if book_title in self.books:
            self.books.remove(book_title)

    def search_book(self, keyword):
        """Return titles containing the keyword, ignoring letter case."""
        keyword = keyword.lower()
        return [book for book in self.books if keyword in book.lower()]

    def display_books(self):
        """Display every book title in the collection."""
        if not self.books:
            print("The library has no books.")
            return

        for book in self.books:
            print(book)


if __name__ == "__main__":
    library = Library("City Library")
    library.add_book("Python Programming")
    library.add_book("Database Systems")
    library.add_book("Advanced Backend Development")

    print(f"Books in {library.name}:")
    library.display_books()
    print("Books matching 'python':", library.search_book("python"))

    library.remove_book("Database Systems")
    print("After removing Database Systems:")
    library.display_books()