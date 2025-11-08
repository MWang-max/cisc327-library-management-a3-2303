import pytest
from services.library_service import calculate_late_fee_for_book, borrow_book_by_patron, add_book_to_catalog

# (1st valid)

def test_success_late_fee_within_7_days():
    # Assuming this patron has a book 5 days overdue
    patron_id = "123456"
    book_id = "1234567890123"  # 13 digits

    result = calculate_late_fee_for_book(patron_id, book_id)
    assert result[0] is True
    data = result[1].json
    assert data['days_overdue'] == 5
    assert data['late_fee'] == 5 * 0.5
    assert data['status'] == 'Late'


# (2nd valid)

def test_success_late_fee_over_7_days():
    patron_id = "111111"
    book_id = "1234567890123"  # 13 digits

    result = calculate_late_fee_for_book(patron_id, book_id)
    assert result[0] is True
    data = result[1].json
    # 7 days * 0.5 + 3 days * 1 = 3.5 + 3 = 6.5
    assert data['days_overdue'] == 10
    assert data['late_fee'] == 6.5
    assert data['status'] == 'Late'

# (1st invalid)

def test_failure_invalid_patron_id_length():
    # Patron ID length != 6 should fail
    patron_id = "ABCDE"  # length 5
    book_id = "1234567890123"

    result = calculate_late_fee_for_book(patron_id, book_id)
    assert result == "Invalid input"

# (2nd invalid)

def test_failure_book_not_borrowed():
    # Patron does not have this book borrowed
    patron_id = "222222"
    book_id = "9999999999999"  # some other book
    
    result = calculate_late_fee_for_book(patron_id, book_id)
    assert result[0] is False
    assert result[1] == 'Late fee calculation not implemented'
