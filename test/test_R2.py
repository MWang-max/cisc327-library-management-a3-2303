import pytest
import database

# test case 1 - book with ISBN that does not exist

def test_1():
    book = database.get_book_by_isbn("0000000000000")
    assert book == None

# test case 2 - patron with 0 books borrowed

def test_2():
    borrowed_count = database.get_patron_borrow_count("111111")
    assert borrowed_count == 0


# test case 3 - no title

def test_3():
    inserted = database.insert_book(None, "John Doe", "1231231231231", 1, 1)
    assert inserted == False

# test case 4 - patron with no books currently borrowed

def test_4(): 
    currently_borrowed = database.get_patron_borrowed_books("111111")
    assert currently_borrowed == []
