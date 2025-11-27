
class Book:
    def __init__(self, id:str, title:str, author:str, year:int, status:str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def describe(self):
        print("ID: ", self.id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Status:", self.status)

class Library:
    def __init__(self):
        self.books = []

    def add(self, book : Book):
        for b in self.books:
            if b.search_by_title == book.title:
                return False
        self.books.append(book)
        return True

    def remove(self, book: Book):
        self.books.remove(book)

    def search_by_title(self, title:str)->"Book":
        for book in self.books:
            if book.title == title:
                return book
        return None

    def search_by_author(self, author: str):
        list_of_books = []
        for book in self.books:
            if book.author == author:
                list_of_books.append(book)

        return list_of_books

    def borrow(self, book:Book):
        if book.status == "borrowed":
            print("Sach da duoc muon")
        else:
            book.status = "borrowed"
            print("Muon sach thanh cong")

    def give_back(self, book:Book):
        book.status = "borrowed"
        print('Tra sach thanh cong')

    def printAll(self):
        for b in self.books:
            b.describe()

class Manager:
    lib1 = Library()
    @classmethod

    def menu(cls):
        while True:
            print("1. Them sach")
            print("2. Xoa sach")
            print("3. Tim kiem theo tieu de")
            print("4. Tim kiem theo tac gia")
            print("5. Muon sach")
            print("6. Tra sach")
            print("0. Thoat")
            chon = int(input("Nhap chuc nang: "))
            if chon == 0:
                break
            elif chon == 1:
                id = input("Nhap id:")
                title = input("Nhap tieu de: ")
                author = input("Nhap tac gia: ")
                year = int(input("Nhap nam xb: "))
                status = input("Tinh trang (borrowed/unborrowed): ")
                book1 = Book(id, title, author, year, status)
                if cls.lib1.add(book1):
                    print("Them sach thanh cong")
                else:
                    print("Da ton tai sach co tieu de da nhap")

            elif chon == 2:
                title = input("Nhap ten sach muon xoa: ")
                book = cls.lib1.search_by_title(title)
                if (book == None):
                    print("Ten sach khong co trong thu vien")

                else:
                    cls.lib1.remove(book)
                    print("Xoa thanh cong")

            elif chon == 3:
                title = input("Nhap tieu de muon tim kiem: ")
                book = cls.lib1.search_by_title(title)
                if (book == None):
                    print("Khong tim thay")
                else:
                    book.describe()

            elif chon == 4:
                author = input("Nhap ten tac gia muon tim:")
                new_list = cls.lib1.search_by_author(author)
                for book in new_list:
                    book.describe()

            elif chon == 5:
                title = input("Nhap tieu de sach muon muon: ")
                book = cls.lib1.search_by_title(title)
                if book == None:
                    print("Khong tim thay")
                else:
                    cls.lib1.borrow(book)

            elif chon == 6:
                title = input("Nhap ten sach muon tra: ")
                book = cls.lib1.search_by_title(title)
                if book == None:
                    print("Khong tim thay")
                else:
                    cls.lib1.give_back(book)
            elif chon == 7:
                cls.lib1.printAll()

Manager.menu()





