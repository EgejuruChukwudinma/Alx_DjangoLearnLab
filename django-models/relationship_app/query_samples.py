from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name: str):
    """Query all books by a specific author."""
    return Book.objects.filter(author__name=author_name)

def books_in_library(library_name: str):
    """List all books in a library."""
    lib = Library.objects.get(name=library_name)
    return lib.books.all()

def librarian_for_library(library_name: str):
    """Retrieve the librarian for a library."""
    lib = Library.objects.get(name=library_name)
    return lib.librarian

