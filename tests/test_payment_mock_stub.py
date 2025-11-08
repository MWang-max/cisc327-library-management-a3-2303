import pytest
from services.payment_service import PaymentGateway
import unittest.mock
import services.library_service as library_service
import pytest

# pay_late_fees() tests

# successful payment 

def test_successful_payment():
    mock = unittest.mock.Mock(spec=PaymentGateway)
    mock.return_value = (True, "Payment successful!" ,"txn_111111")
    success, book_id, transaction_id = library_service.pay_late_fees("111111", "1234567890", mock)
    mock.assert_not_called()
    assert (success, book_id, transaction_id) == mock.return_value

# payment declined by gateway

def test_declined_payment():
    mock = unittest.mock.Mock(spec=PaymentGateway)
    mock.return_value = (False, "Unable to calculate late fees." , None)
    success, _, transaction_id = library_service.pay_late_fees("111111", "1234567890", mock)
    mock.assert_not_called()
    assert (success, "Unable to calculate late fees.", transaction_id) == mock.return_value

# invalid patron ID - mock not called

def test_invalid_id():
    mock = unittest.mock.Mock(spec=PaymentGateway)
    mock.return_value = (False, "Invalid patron ID. Must be exactly 6 digits.", None)
    success, message, return_val = library_service.pay_late_fees("abc123", "1234567890123", mock)
    mock.assert_not_called()
    assert (success, message, return_val) == mock.return_value

    
# 0 late fees - mock not called

def test_no_late_fees():
    mock = unittest.mock.Mock(spec=PaymentGateway)
    stub = unittest.mock.patch('services.library_service.calculate_late_fee_for_book')
    stub.return_value = (True, {'late_fee': 0, 'days_overdue': 0, 'status': 'Not late'})
    mock.return_value = (False, "No late fees to pay for this book.", None)
    success, _, _ = library_service.pay_late_fees("123456", "1234567890", mock)
    mock.assert_not_called()
    assert success == False

# network error exception handling 

def test_network_error_exception():
    success, _, _ = library_service.pay_late_fees(patron_id = "123456", book_id = "", payment_gateway=" ")
    assert success == False
    
# refund_late_fee_payment() tests

# successful refund

def test_successful_refund():
    success, _ = library_service.refund_late_fee_payment("txn_123456", 1.00, None)
    assert success == True

# invalid transaction ID rejected 

def test_invalid_transaction_id():
    _, message = library_service.refund_late_fee_payment(None, 1.00, None)
    assert message == "Invalid transaction ID."

# negative refund (invalid)

def test_negative_refund():
    _, message = library_service.refund_late_fee_payment("txn_123456", -0.05, None)
    assert message == "Refund amount must be greater than 0."

# zero refund (invalid)

def test_no_refund():
    _, message = library_service.refund_late_fee_payment("txn_123456", 0, None)
    assert message == "Refund amount must be greater than 0."

# refund over $15 (invalid)

def test_excess_refund():
    _, message = library_service.refund_late_fee_payment("txn_123456", 16, None)
    assert message == "Refund amount exceeds maximum late fee."

# get fee info

def test_fee_info():
    overdue, _, _ = library_service.pay_late_fees(patron_id = '123456', book_id = '1234567890123', payment_gateway = None)
    assert overdue == False
     
def test_pay_late_fees_fail():
    success, _, _ = library_service.pay_late_fees('1234', 1234567890123, payment_gateway=None)
    assert success == False

def test_search_fail():
    found = library_service.search_books_in_catalog("1849182798", "author")
    assert found == False

def test_add_book_no_title():
    title, _ = library_service.add_book_to_catalog("", "author", "3333333333333", total_copies=1)
    assert title == False

# check author - stub

def test_author_check():
    stub = unittest.mock.patch('services.library_service.add_book_to_catalog')
    library_service.add_book_to_catalog("Anne of Green Gables", "Lucy Maud Montgomery", "7777777777777", total_copies=2)
    stub.return_value = (True, "Anne of Green Gables")
    success, _ = library_service.search_books_in_catalog("Lucy Maud Montgomery", "author")
    assert success == stub.return_value[0]

# names too long

def test_long_author_name():
    _, message = library_service.add_book_to_catalog("Book by an author with a super long name", author = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm", isbn = "0000000001011", total_copies=1)
    assert message == "Author must be less than 100 characters."

def test_long_title():
    _, message = library_service.add_book_to_catalog("qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm", author = "qwertyuiop", isbn = "0000000001012", total_copies=1)
    assert message == "Title must be less than 200 characters." 

# refund gateway failure
def test_invalid_refund(): 
    success, _ = library_service.refund_late_fee_payment("txn_123456", 0.50, "Fail")
    assert success == False

