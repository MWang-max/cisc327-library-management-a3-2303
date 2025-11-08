import pytest
from database import insert_book
from services.library_service import borrow_book_by_patron, insert_borrow_record
from datetime import timedelta, datetime

# (1st valid)

def test_successful_borrow():
    # Arrange
    insert_book(title="1984",author="George Orwell",isbn="2222222222222",total_copies=3, available_copies=3)
    
    # Act
    success, message = borrow_book_by_patron("123456", 1)
    
    # Assert
    assert success is True
    assert "Successfully borrowed" in message
    assert "Due date:" in message

# (2nd valid)


def test_successful_borrow_with_5_books_limit_edge():
    # Arrange
    insert_book(title="Brave New World", author="Aldous Huxley", isbn="3333333333333", total_copies=2, available_copies=2)
    
    # Patron has borrowed 5 books (edge case: should still be allowed)
    for i in range(5):
        insert_book(100 + i, title=f"Book {i}", available_copies=1)
        insert_borrow_record("234567", 100 + i, datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=13))

    # Act
    success, message = borrow_book_by_patron("234567", 2)
    
    # Assert
    assert success is True
    assert "Successfully borrowed" in message

# (1st invalid)

def test_fail_invalid_patron_id():
    # Act
    success, message = borrow_book_by_patron("12AB", 1)
    
    # Assert
    assert success is False
    assert message == "Invalid patron ID. Must be exactly 6 digits."

# (2nd invalid)


def test_fail_book_not_available():
    # Arrange
    insert_book(title="The Catcher in the Rye", author="JD Salinger", isbn = "1111111111111", total_copies=1 , available_copies=0)
    
    # Act
    success, message = borrow_book_by_patron("345678", 3)
    
    # Assert
    assert success is False
    assert message == "This book is currently not available."

