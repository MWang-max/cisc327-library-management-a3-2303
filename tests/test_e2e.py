from playwright.sync_api import Page, expect

def test_add_book(page: Page):
    page.goto("http://localhost:5000/catalog")
    page.get_by_role('button', name = 'Add New Book').click()
    expect(page.get_by_text('Add New Book')).to_be_visible()
    expect(page.get_by_title('Library Management System')).to_be_visible()
    page.get_by_role('textbox', name = 'Title').click()
    page.get_by_role('textbox', name = 'Title').fill('zxcvbnm')
    page.get_by_role('textbox', name = 'Title').press('Enter')
    page.get_by_role('textbox', name = 'Author').click()
    page.get_by_role('textbox', name = 'Author').fill('zxcvbnm')
    page.get_by_role('textbox', name = 'Author').press('Enter')
    page.get_by_role('textbox', name = 'ISBN').click()
    page.get_by_role('textbox', name = 'ISBN').fill('9780743273565')
    page.get_by_role('textbox', name = 'ISBN').press('Enter')
    page.get_by_role('textbox', name = 'Total Copies').click()
    page.get_by_role('textbox', name = 'Total Copies').fill('2')
    page.get_by_role('button', name = 'Add Book to Catalog').click()
    expect(page.get_by_text('zxcvbnm')).to_be_visible()

def test_borrow_book(page: Page):
    page.goto("http://localhost:5000/catalog")
    page.get_by_role('textbox', name = 'Patron ID (6 digits)').click()
    page.get_by_role('textbox', name = 'Patron ID (6 digits)').fill('333333')
    page.get_by_role('button', name = 'Borrow').click()
    expect(page.get_by_text('Successfully borrowed')).to_be_visible()