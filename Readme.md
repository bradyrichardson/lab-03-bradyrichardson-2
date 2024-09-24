# Lab 3: Object-Oriented Programming and Pandas

### Instructions 
#### Objective: 
The goal of this assignment is to merge foundational concepts from object-oriented programming with the utility of the Pandas library. By the end, you should be able to create classes that can effectively interact with and manipulate Pandas data structures.

#### Problem Statement:  
You are a data analyst at a digital library. Your task is to design a system that can process, manipulate, and analyze data regarding different books available in the library.

#### Files and Functions
* For Tasks 1 and 2, write the code for the Classes in the provided `digital_library.py`.  
* For Task 3, use the file `test_library.py` to write code that shows that your classes work as expected. 
* **Do not** change the names of the files, functions, methods, or Classes.
* You are free to include other `.py` or `.ipynb` files with more of your work. However, ensure that `digital_library.py` contains the final code for each Class and `test_library.py` contains the code to test your classes. 

### Data
The data for this lab is `library_books.csv` found in the "CleanData" folder of my GitHub [Data Repository](https://github.com/esnt/Data/tree/main/CleanData).  This data is a simplified and cleaned subset from [Zenodo](https://zenodo.org/record/4265096).  It has the following columns:
1. `book_id`: Unique identifier for each book (should be a string)
2. `title`: Title of the book.
3. `author`: Author of the book.
4. `genre`: Genre of the book (e.g., Fiction, Non-Fiction, Mystery, Sci-Fi).
5. `pages`: Number of pages in the book.
6. `published_year`: The year the book was published.




---
### Task 1: Create a `Book` class
#### Attributes:
- `book_id` 
- `title`
- `author`
- `genre`
- `pages`
- `published_year`

#### Methods:
- `get_age()`: Should return the age of the book based on the current year.
- `is_long()`: Should return `True` if the book has more than 300 pages; otherwise, `False`.
- `summary()`: Should return a string with the format: "Book ID `book_id`: `title` by `author` has `pages` pages. It was first published in `published_year` and belongs to the `genre` genre."

#### Instantiating the Object:
- When an object of the `Book` class is instantiated, each of the attributes should be specified separately.  For example:
  ```
  book = Book('100', 'NewBook', 'NewAuthor', 'Mystery', 270, 2010)
  ```
- Make sure that the code for your classes, attributes, and functions assume this form for object instantiation

---
### Task 2: Create a `Library` class
#### Attributes:
- `data`: A pandas DataFrame loaded from the provided CSV file.
- `size`: Number of books in the library.
- `authors`: Number of unique authors in the library.

#### Methods:
- `add_book(book: Book)`: Takes an instance of `Book` and adds it to the DataFrame. All `Library` attributes should be updated accordingly.
   * If the book already exists in library the method should return the string "Error: book_id `book_id` is already in the library."
- `remove_book(book_id: str)`: Takes a `book_id` and removes the corresponding book from the DataFrame. All `Library` attributes should be updated accordingly.  
   * If the `book_id` is not in the library, the method should return the string: "Error: `book_id` is not in the library."
- `get_books_by_author(author: str)`: Takes an author's name and returns a DataFrame containing all books by that author.
   * If `author` is not in the library, the method should return the string: "No books by `author` in library"
- `get_genre_count()`: Should return a series with the count of books in each genre.
- `get_book_summary(book_id: str)`: Takes a `book_id` and returns a string with the format:  
   * "Book ID `book_id`: `title` by `author` has `pages` pages. It was first published in `published_year` and belongs to the `genre` genre."  
   * If the `book_id` is not in the library, it should return "No matching book in the library."
- `__str__()`: Should return a string representing the library. When a `Library` object is printed, the string "There are `size` books in the library by `authors` unique authors. The oldest book in the library is `title` by `author` published in `published_year`." should be output.

#### Instantiating the Object:
- An object of the `Library` class should be instantiated only with a *pandas* DataFrame.  For example:
  ```
  df = pd.read_csv('library_books.csv')
  library = Library(df)
  ```
- Make sure that the code for your classes, attributes, and functions assume this form for object instantiation

#### Additional Notes:
- Please ensure to update the `size` and `authors` attributes of the `Library` class appropriately whenever a book is added or removed.

---
### Task 3:  Test your Classes
In the `test_library.py` file write python code that:
* Creates instances of the `Book` class
* Initializes a `Library` using [`library_books.csv`](https://github.com/esnt/Data/tree/main/CleanData)
* Tests all methods of both classes to ensure they work as expected
* Ensure that your code is well-commented and that both files are free of syntax errors and run without issues