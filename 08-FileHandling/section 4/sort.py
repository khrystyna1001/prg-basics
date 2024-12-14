# Genre --> Filename
# Fantasy --> books_fantasy.txt
# Historical --> books_historical.txt
# Romance --> books_romance.txt
# Classic --> books_classic.txt  
import csv

def read_books_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        books = [row for row in csv_reader]
    return books

def write_books_to_file(books, genre, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for book in books:
            if book['Genre'] == genre:
                f.write(f"{book['Title']}, {book['Author']}, {book['Year']}\n")

books = read_books_csv('books.csv')
write_books_to_file(books, 'Fantasy', 'books_fantasy.txt')
write_books_to_file(books, 'Historical', 'books_historical.txt')
write_books_to_file(books, 'Romance', 'books_romance.txt')
write_books_to_file(books, 'Classic', 'books_classic.txt')