class StoryBook:
    def __init__(self, name, price, author_name, author_born, no_of_pages):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishingL_year = 2022
        self.no_of_pages = no_of_pages

    # Regular Method 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, pages: {self.no_of_pages}')

    # Regular Method 2
    def get_author_info(self):
        print(f'The author name: {self.author_name}, born: {self.author_born}')

book_1 = StoryBook('Hamlet', 350, 'Shakespeare', 1564, 500)
book_2 = StoryBook('The Kite Runner', 200, 'Khaled Hossain', 1965, 200)

book_1.get_book_info()
book_1.get_author_info()
StoryBook.get_book_info(book_2)

