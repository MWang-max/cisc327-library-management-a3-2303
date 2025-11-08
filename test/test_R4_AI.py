import pytest
from services.library_service import return_book_by_patron

# (1st valid)
def test_return_book_success_no_late_fee():
    patron_id = "000001"
    book_id = "1001000000000"
    
    # Precondition: patron_001 has book_id 1001 borrowed, and no late fee
    success, message = return_book_by_patron(patron_id, book_id)
    assert success is True
    assert message == "Book successfully returned."

# (2nd valid)

def test_return_book_success_with_late_fee():
    patron_id = "000002"
    book_id = "1002000000000"
    
    # Precondition: patron_002 has book_id 1002 borrowed, with a late fee > 0
    success, message = return_book_by_patron(patron_id, book_id)
    assert success is True
    assert isinstance(message, tuple) or isinstance(message, str)
    assert "Book successfully returned." in message

# (1st invalid)

def test_return_book_failure_not_borrowed():
    patron_id = "000003"
    book_id = "9999999999999"  # assume this book was never borrowed by this patron
    
    success, message = return_book_by_patron(patron_id, book_id)
    assert success is False
    assert message == "Book not borrowed."




# (2nd invalid)

def test_return_book_failure_already_returned():
    patron_id = "000004"
    book_id = "1004000000000"

    # First return (assumed successful)
    return_book_by_patron(patron_id, book_id)

    # Second return should fail because book is already returned
    success, message = return_book_by_patron(patron_id, book_id)
    assert success is False
    assert message == "Book not borrowed."
