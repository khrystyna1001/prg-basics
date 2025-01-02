class EBook:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = 1
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def change_page(self, page):
        if self.is_open:
            if page < 1 or page > self.number_of_pages:
                print("There is no such page in this book.")
                return
            self.current_page = page
        else:
            print("The book is closed.")
    def display_info(self):
        print(f"The name of this book is {self.title}.")
        print(f"Written by {self.author}.")
        print(f"This book has {self.number_of_pages} pages.")
        if self.is_open:
            print(f"I am just reading the book, page {self.current_page}.")
        else:
            print("I am going to read the book later.")