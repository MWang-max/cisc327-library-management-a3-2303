import pytest
from services.library_service import get_patron_status_report, borrow_book_by_patron, add_book_to_catalog

# valid test case - valid patron ID

def test_1():
    add_book_to_catalog("123456", "John Doe", "1234567890123", 1)
    borrow_book_by_patron("123456", "1234567890123")
    patron_status, _ = get_patron_status_report("123456")
    assert patron_status == True

# invalid test case 2 - blank patron ID

def test_2():
    patron_status, _ = get_patron_status_report("")
    assert patron_status == False

# invalid test case 3 - invalid patron ID (too many digits)

def test_3():
    patron_status, _ = get_patron_status_report("1234567")
    assert patron_status == False

# invalid test case 4 - invalid patron ID (too few digits)

def test_4():
    patron_status, _ = get_patron_status_report("123")
    assert patron_status == False