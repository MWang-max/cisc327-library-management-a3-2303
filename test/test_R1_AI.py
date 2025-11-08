import pytest
from services.library_service import add_book_to_catalog, get_book_by_isbn

# (1st valid test)

def test_add_book_success():
    title = "The Great Gatsby"
    author = "F. Scott Fitzgerald"
    isbn = "1000000000001"  # Ensure a unique ISBN
    total_copies = 5

    # Ensure test is isolated by choosing a unique ISBN
    if not get_book_by_isbn(isbn):
        success, message = add_book_to_catalog(title, author, isbn, total_copies)
        assert success is True
        assert "successfully added" in message
    else:
        assert success is False


# (2nd valid test)

def test_add_book_success_with_whitespace():
    title = " 1984 "
    author = " George Orwell "
    isbn = "1000000000002"  # Unique ISBN
    total_copies = 3

    if not get_book_by_isbn(isbn):
        success, message = add_book_to_catalog(title, author, isbn, total_copies)
        assert success is True
        assert '1984' in message
    else:
        assert success is False

# (1st invalid test)

def test_add_book_duplicate_isbn():
    title = "Brave New World"
    author = "Aldous Huxley"
    isbn = "1000000000003"
    total_copies = 4

    # First attempt should succeed if not already inserted
    if not get_book_by_isbn(isbn):
        add_book_to_catalog(title, author, isbn, total_copies)

    # Second attempt must fail due to duplicate ISBN
    success, message = add_book_to_catalog("Some Other Title", "Another Author", isbn, 2)
    assert success is False
    assert message == "A book with this ISBN already exists."

# (2nd invalid test)

def test_add_book_invalid_isbn_length():
    title = "Short ISBN Book"
    author = "Test Author"
    isbn = "12345"  # Too short
    total_copies = 2

    success, message = add_book_to_catalog(title, author, isbn, total_copies)

    assert success is False
    assert message == "ISBN must be exactly 13 digits."



