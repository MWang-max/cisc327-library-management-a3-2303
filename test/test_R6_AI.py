import pytest
from services.library_service import search_books_in_catalog, add_book_to_catalog

Dictionary = [
    {"book_id": 9781234567890, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"book_id": 9789876543210, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"book_id": 9781111111111, "title": "1984", "author": "George Orwell"},
]



# (1st valid) 

def test_search_books_by_isbn_success():
    result = search_books_in_catalog("9781234567890", "isbn")
    assert result[0] is True
    assert result[1]['title'] == "The Great Gatsby"

# (2nd valid)

def test_search_books_by_title_success():
    result = search_books_in_catalog("Mockingbird", "title")
    assert result[0] is True
    assert "Mockingbird" in result[1]['title']

# (1st invalid)

def test_search_books_by_isbn_failure_not_found():
    result = search_books_in_catalog("9780000000000", "isbn")
    assert result is False

# (2nd invalid)

def test_search_books_invalid_search_type():
    result = search_books_in_catalog("9781234567890", "publisher")
    assert result is False
