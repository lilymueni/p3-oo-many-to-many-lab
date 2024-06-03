class Book:
    all = []

    def __init__(self, title):
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Author:
    all = []

    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book")
        self._book = value

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
