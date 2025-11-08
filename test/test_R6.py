import pytest
from services.library_service import search_books_in_catalog, add_book_to_catalog

# valid test case - valid search term and search type

def test_1():
    add_book_to_catalog(title="My autobiography", author="John Doe", isbn="1234567890123", total_copies=1)
    search_result, _ = search_books_in_catalog("My autobiography", "title")
    assert search_result == True

# invalid test case 2 - invalid search term

def test_2():
    search_result, _ = search_books_in_catalog(None, "title")
    assert search_result == False

# invalid test case 3 - invalid search type

def test_3():
    search_result = search_books_in_catalog("My autobiography", "")
    assert search_result == False

# invalid test case 4 - both invalid

def test_4():
    search_result = search_books_in_catalog("", "qwertyuiop")
    assert search_result == False