import pytest
from services.library_service import add_book_to_catalog

# positive test case 1

def test_valid_1():
    added, message = add_book_to_catalog("My autobiography", "John Doe", "1234567890123", 1)
    assert added == True
    assert "successfully added to the catalog" in message

# positive test case 2

def test_valid_2():
    added, message = add_book_to_catalog("My personal autobiography", "Jane Doe", "1234567890124", 2)
    assert added == True
    assert "successfully added to the catalog" in message

# negative test case 1 - no author

def test_invalid_1():
    added, message = add_book_to_catalog("An anonymous autobiography", None, "1234567890125", 1)
    assert added == False
    assert message == "Author is required."

# negative test case 2 - invalid number of copies

def test_invalid_2():
    added, message = add_book_to_catalog("The book I decided not to name", "John Smith", "1234567890126", -2.3)
    assert added == False
    assert "must be a positive integer" in message

