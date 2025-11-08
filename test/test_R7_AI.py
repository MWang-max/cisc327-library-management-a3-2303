import pytest
from services.library_service import get_patron_status_report, borrow_book_by_patron, add_book_to_catalog

# (1st valid) 

def test_valid_patron_with_borrowed_books():
    patron_id = "123456"  # Assumed to be a test patron with borrowed books

    success, result = get_patron_status_report(patron_id)

    assert success is True
    assert isinstance(result, dict)
    assert "books_and_due_dates" in result
    assert "late_fees" in result
    assert "num_borrowed" in result
    assert result["num_borrowed"] > 0

# (2nd valid)

def test_borrow_history_equals_books_and_due_dates():
    patron_id = "123456"  # Same valid patron with borrowed books

    success, result = get_patron_status_report(patron_id)

    assert success is True
    assert result["books_and_due_dates"] == result["borrow_history"]

# (1st invalid) 

def test_patron_with_no_borrowed_books():
    patron_id = "654321"  # Assumed to be a test patron with zero borrowed books

    success, _ = get_patron_status_report(patron_id)

    assert success is False


# (2nd invalid)

def test_nonexistent_patron_id_returns_failure():
    patron_id = "999999"  # Assumed to be a 6-digit ID not in the test system

    success, _ = get_patron_status_report(patron_id)

    assert success is False
