class NameError(Exception):
    def __init__(self):
        self._msg = 'Null error'

    def __str__(self):
        return self._msg

class Book:
    def __init__(self, name):
        if name is None:
            raise NameError

        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @staticmethod
    def info():
        print("Book class")

class Library:
    def __init__(self, name, books):
        if name is None:
            raise NameError

        self._name = name
        self._books = books

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, value):
        self._books = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def displayBooks(self):
        for tempBook in self._books:
            print(tempBook._name)


if __name__ == '__main__':
    Book.info()

    books = [Book("book1"), Book("book2")]
    library = Library("lib", books)

    print(library.name)
    library.displayBooks()