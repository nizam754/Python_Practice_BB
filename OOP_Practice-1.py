class StoryBook:
    def __init__(self, name, price, author_name, author_born):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishingL_year = 2022

book_1 = StoryBook('Hamlet', 350, 'Shakespeare', 1564)
book_2 = StoryBook('The Kite Runner', 200, 'Khaled Hossain', 1965)

print(book_1.author_name)
print(book_2.publishingL_year)
