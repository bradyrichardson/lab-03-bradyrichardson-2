## Import libraries
import pandas as pd
from digital_library import Book, Library

## Read in data (this code reads data directly from GitHub)
url = 'https://github.com/esnt/Data/raw/main/CleanData/library_books.csv'
data = pd.read_csv(url)

