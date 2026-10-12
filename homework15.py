books = ["the hobbit", "to kill a mockingbird", "the catcher in the rye", "animal farm", "lord of the flies"]
copy_counts = [3, 0, 5, 2, 4]
library = {book: count for book, count in zip(books, copy_counts)}
print("full library stock:", library)
available_books = [book for book in books if library[book] > 0]
print("books available:", available_books)
chosen_book = input("which book do you want to borrow? ")
if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, "is not available! stopping the checker.")
    exit()
late_fees = [4, 7, 3, 5, 6]
extra_fee = int(input("enter the extra library fee to add to every book: "))
updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("updated late fees:", updated_fees)
book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]
print("late fee for", chosen_book, "after update:", chosen_fee)
library[chosen_book] = library[chosen_book] - 1
print(chosen_book, "remaining copies:", library[chosen_book])
print("")
print("library book checker")
print("book borrowed:", chosen_book)
print("late fee:", chosen_fee)
print("updated library stock:", library)
print("")