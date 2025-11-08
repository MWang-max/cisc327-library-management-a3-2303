import pytest
from services.library_service import return_book_by_patron, borrow_book_by_patron, add_book_to_catalog

# valid test case - both library card number and ISBN valid

def test_1():
    add_book_to_catalog("123456", "John Doe", "1234567890123", 1)
    borrow_book_by_patron("123456", "1234567890123")
    returned, _ = return_book_by_patron("123456", "1234567890123")
    assert returned == True
    

# invalid test case 2 - library card number not valid

def test_2():
    returned, _ = return_book_by_patron("12345", "1234567890123")
    assert returned == False

# invalid test case 3 - ISBN not valid

def test_3():
    returned, _ = return_book_by_patron("123456", "123456789012")
    assert returned == False


# invalid test case 4 - neither valid

def test_4():
    returned, _ = return_book_by_patron("12345", "123456789012")
    assert returned == False 