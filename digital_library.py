## Import necessary libraries
import pandas as pd
import datetime

## Book Class
class Book:
    def __init__(self, book_id, title, author, genre, published_year, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.published_year = published_year
        self.pages = pages
        self.book_id = book_id
    
    def is_long(self):
        return self.pages > 300

    def get_age(self):
        return datetime.datetime.now().year - self.published_year

    def summary(self):
        return f'Book ID {self.book_id}: {self.title} by author has {self.pages} pages. It was first published in {self.published_year} and belongs to the genre {self.genre}.'
    
class Library:
    def __init__(self, data):
        self.data = data.set_index('book_id')
        self.size = len(data)
        self.authors = data['author'].nunique()

    def get_size(self):
        return self.size
    
    def add_book(self, book: Book):
        # Takes an instance of Book and adds it to the DataFrame. All Library attributes should be updated accordingly.
        # If the book already exists in library the method should return the string "Error: book_id book_id is already in the library."
        if book.book_id not in self.data.index:
            self.data.loc[book.book_id] = {'title': book.title, 'author': book.author, 'genre': book.genre, 'published_year': book.published_year, 'pages': book.pages, 'book_id': book.book_id}
            self.size = len(self.data)
        else:
            return f"Error: {book_id} is already in the library."
        
    def remove_book(self, book_id: str): 
        # Takes a book_id and removes the corresponding book from the DataFrame. All Library attributes should be updated accordingly.
        # If the book_id is not in the library, the method should return the string: "Error: book_id is not in the library."
        if book_id in self.data.index:
            self.data.drop(index=book_id, inplace=True)
            self.size = len(self.data)
        else:
            return "Error: book_id is not in the library."
    
    def get_books_by_author(self, author: str):
        # Takes an author's name and returns a DataFrame containing all books by that author.
        # If author is not in the library, the method should return the string: "No books by author in library"
        return self.data[self.data['author'] == author]

    def get_genre_count(self):
        # Should return a series with the count of books in each genre.
        return self.data['genre'].value_counts()

    def get_book_summary(self, book_id: str):
        # Takes a book_id and returns a string with the format:
        # "Book ID book_id: title by author has pages pages. It was first published in published_year and belongs to the genre genre."
        # If the book_id is not in the library, it should return "No matching book in the library."
        if book_id in self.data.index:
            book = Book(book_id, **self.data.loc[book_id])
            return book.summary()
        else:
            return "No matching book in the library."

    def __str__(self):
        # Should return a string representing the library.
        # When a Library object is printed, the string "There are size books in the library by authors unique authors.
        # The oldest book in the library is title by author published in published_year." should be output.
        book_id = self.data['published_year'].idxmin()
        print(book_id)
        book = self.data.loc[book_id]
        return f"There are {self.size} books in the library by {self.authors} unique authors. The oldest book in the library is {book.title} by {book.author} published in {book.published_year}."

        

