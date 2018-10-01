# Python code for TomeRater Capstone Project
# Christopher Arnold

# The following defines the User class and its methods.
class User(object):
    def __init__(self, name, email):
        self.name = name.title()
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email 

    def change_email(self, address):
        if self.email != address:
            self.email = address
            print("{} is the new email address for {}.".format(self.email, self.name))
        else:
            print("{} is already the email address for {}.".format(address, self.name))

    def __repr__(self):
        return "user: {}, email: {}, books read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            other_user = self

    def read_book(self, book, rating = None):
        if rating in range(0,5):
            self.books[book] = rating
        elif rating == None:
            self.books[book] = None
        else:
            print("Invalid Rating. Ratings are from 0 to 4. Please try again.")

    def get_average_rating(self):
        total_rating = 0
        no_rating_count = 0
        for book in self.books:
            if self.books.get(book) == None:
                no_rating_count +=1
            else:
                total_rating += self.books.get(book)
        average_rating = total_rating/(len(self.books) - no_rating_count)
        return average_rating

# The following defines the Book class and its subclasses (Fiction and NonFiction), and their methods.
class Book(object):
    def __init__(self, title, isbn):
        self.title = str(title).title()
        self.ratings = []
        try:
            self.isbn = int(isbn)
        except ValueError:
            print("Invalid Entry. ISBN must be an integer. Please try again.")
        
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        if self.isbn != new_isbn:
            self.isbn = new_isbn
            print("{} is the new ISBN for {}.".format(self.isbn, self.title))
        else:
            print("{} is already the ISBN for {}.".format(new_isbn, self.title))

    def add_rating(self, rating):
        if rating in range(0,5):
            self.ratings += [rating]
        elif rating == None:
            pass  
        else:
            print("Invalid Rating. Ratings are from 0 to 4. Please try again.")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            other_book = self

    def get_average_rating(self):
        total_rating = 0
        for rating in self.ratings:
            total_rating += rating
        average_rating = total_rating/len(self.ratings)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author.title()

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = str(subject)
        self.level = str(level).lower()

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a(n) {} manual on {}".format(self.title, self.level, self.subject)

# The following defines the TomeRater class and its methods, which call the methods above.
class TomeRater:
    def __init__(self):
        self.users = {} 
        self.books = {} 

    def create_book(self, title, isbn):
        self = Book(title, isbn)
        return self

    def create_novel(self, title, author, isbn):
        self = Fiction(title, author, isbn)
        return self

    def create_non_fiction(self, title, subject, level, isbn):
        self = Non_Fiction(title, subject, level, isbn)
        return self

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users.get(email).read_book(book, rating)
            if book in self.books.keys():
                book.add_rating(rating)
                self.books[book] += 1
            else:
                self.books[book] = 1
                book.add_rating(rating)
        else:
            print("No user with email: {}".format(email))

    def add_user(self, name, email, user_books = None):
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

	# Below begins the TomeRater analysis methods.

    def print_catalog(self):
        print("Book Catalog:")
        for book in self.books.keys():
            print("\"{}\" has been read {} times and has an average rating of {}".format(book.title, self.books.get(book), book.get_average_rating()))
        print("\n")

    def print_users(self):
        print("Book Connoisseurs:")
        for user in self.users.values():
            print(user.name)
        print("\n")

    def most_read_book(self):
        most_read_count = 0
        most_read = ""
        for book in self.books:
            if self.books.get(book) > most_read_count:
                most_read = book.title
                most_read_count = self.books.get(book)
            elif self.books.get(book) == most_read_count:
                most_read += " & " + book.title
        return most_read

    def highest_rated_book(self):
        highest_rating = 0
        best_book = ""
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                best_book = book.title
                highest_rating = book.get_average_rating()
            elif book.get_average_rating() == highest_rating:
                best_book += " & " + book.title
        return best_book

    def most_positive_user(self):
        highest_rating = 0
        most_positive = ""
        for user in self.users.values():
            if user.get_average_rating() > highest_rating:
                most_positive = user.name
                highest_rating = user.get_average_rating()
            elif user.get_average_rating() == highest_rating:
                most_positive += " & " + user.name
        return most_positive

    


	