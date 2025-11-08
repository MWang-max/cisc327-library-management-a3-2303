import pytest
from services.library_service import calculate_late_fee_for_book, borrow_book_by_patron, add_book_to_catalog

# valid test case - patron ID and ISBN valid

def test_1():
    add_book_to_catalog("123456", "John Doe", "1234567890123", 1)
    borrow_book_by_patron("123456", "1234567890123")
    status, _ = calculate_late_fee_for_book("123456", "1234567890123")
    assert status is False


# invalid test case 2 - invalid patron ID

def test_2():
    status,_ = calculate_late_fee_for_book("12345", "1234567890123")
    assert status is False

# invalid test case 3 - invalid ISBN

def test_3():
    status, _ = calculate_late_fee_for_book("123456", "123456789012345")
    assert status is False

# invalid test case 4 - neither valid

def test_4():
    status, _ = calculate_late_fee_for_book("12345", "1234567890")
    assert status is False