import ebook

# Open a book
# Display a book status (title, author, page numbers, current page no)
# Read a few pages
# Display a book status
# Close a book
# Read a few pages (it should not be possible to perform this operation - display the message 
# that the book is closed).

def main():
    ebook1 = ebook.EBook('Harry Potter and the Philosopher\'s Stone', 'J. K. Rowling', 223)
    ebook1.open()
    ebook1.display_info()
    ebook1.change_page(15)
    ebook1.display_info()
    ebook1.close()
    ebook1.display_info()
    ebook1.change_page(19)


if __name__ == "__main__":
    main()