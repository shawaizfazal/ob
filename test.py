class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("you have borrowed '{self.title}' by {self.author}.")
        else:
            print("we arw sorry, '{self.title}' is not available at the moment")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("You have successfully returned '{self.title}'.")
        else:
            print("'{self.title}' was not borrowed.")
book1 = Book("matilda", "roald dahl")
book2 = Book("the hounds of the basker villas", "sir arthur conon doyle")
book3 = Book("the tempest", "shakespere")
print("vorrowing books")
book1.borrow()
book2.borrow()
book3.borrow()
print("\nreturningbooks")
book1.return_book()
book2.return_book()
book3.return_book()