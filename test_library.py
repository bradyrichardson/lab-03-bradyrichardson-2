## Import libraries
import pandas as pd
from digital_library import Book, Library

## Read in data (this code reads data directly from GitHub)
url = 'https://github.com/esnt/Data/raw/main/CleanData/library_books.csv'
data = pd.read_csv(url)

lib = Library(data)

book_1 = Book('1232456789', 'Les Miserables', 'Victor Hugo', 'Historical Fiction', 1862, 1000)

# test methods of Book
print('BOOK')
print('is long')
print(book_1.is_long())

print('get age')
print(book_1.get_age())

print('summary')
print(book_1.summary())

# test methods of Library
print('LIBRARY')
print("before add: ", lib.get_size())
lib.add_book(book_1)
print("after add: ", lib.get_size())

print('get book summary')
print(lib.get_book_summary(book_1.book_id))

print("before removal: ", lib.get_size())
lib.remove_book(book_1.book_id)
print('after removal: ', lib.get_size())

print('get books by author:')
print(lib.get_books_by_author('Suzanne Collins'))

print('get genre count')
print(lib.get_genre_count())

print ('to string')
print(lib)