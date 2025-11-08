import pytest
from services.library_service import borrow_book_by_patron

# valid test case 1
def test_valid_1():
    borrowed, _ = borrow_book_by_patron("123456", "1234567890123")
    assert borrowed == True


# valid test case 2

def test_valid_2():
    borrowed, _ = borrow_book_by_patron("123457", "1234567890123")
    assert borrowed == True

# invalid test case 1 - patron ID too short

def test_invalid_1():
    borrowed, _ = borrow_book_by_patron("11111", "1234567890123")
    assert borrowed == False

# invalid test case 2 - ISBN too short

def test_invalid_2():

    borrowed, _ = borrow_book_by_patron("123458", "1234567890")
    assert borrowed == False