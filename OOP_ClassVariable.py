class StoryBook:

    # Class Variable
    no_of_books = 0

    discount = 0.5

    def __init__(self, name, price, author_name, author_born, no_of_pages):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishingL_year = 2022
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    # Regular Method 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, pages: {self.no_of_pages}')

    # Regular Method 2
    def get_author_info(self):
        print(f'The author name: {self.author_name}, born: {self.author_born}')

    # applying discount to an instance
    def apply_discount(self):
        self.price = int(self.price - self.price * self.discount)

book_1 = StoryBook('Hamlet', 350, 'Shakespeare', 1564, 500)
book_2 = StoryBook('The Kite Runner', 200, 'Khaled Hossain', 1965, 200)


# print(book_1.no_of_books)
# print(book_2.no_of_books)
# print(StoryBook.no_of_books)

print(book_2.price)
book_2.apply_discount()
print(book_2.price)

