import os


class Library:
    status = True

    def __init__(self):
        self.books = self.loadBooksFromFile()

    def addBookToTxt(self, book):
        with open("books.txt", "a+", encoding="utf-8") as file:
            book_info = f"{book[0]},{book[1]},{book[2]},{book[3]}\n"
            file.write(book_info)

    def saveChanges(self):
        with open("books.txt", "w", encoding="utf-8") as file:
            for book in self.books:
                book_info = f"{book[0]},{book[1]},{book[2]},{book[3]}\n"
                file.write(book_info)

    def loadBooksFromFile(self):
        books = []
        if os.path.exists("books.txt"):
            with open("books.txt", "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
                for line in lines:
                    book = line.split(",")
                    book[3] = book[3][:-2]
                    books.append(book)

        return books

    def listBook(self):
        if self.books != []:
            for i in range(len(self.books)):
                print(f"\n{i + 1}.Kitap: {self.books[i][0]},{self.books[i][1]},{self.books[i][2]},{self.books[i][3]}")
        else:
            print("Kütüphanede kitap yok!")

        self.showAndChooseMenu()

    def addBook(self):
        bookName = input("\nKitabın Adı: ")
        bookAuthor = input("Kitabın Yazarı: ")
        bookReleaseDate = input("Kitabın Yayımlanma Tarihi: ")
        bookNumberOfPages = input("Kitabın Sayfa Sayısı: ")

        book = [bookName, bookAuthor, bookReleaseDate, bookNumberOfPages]
        self.books.append(book)

        print("Kitap Eklenme Tamamlandı")
        self.addBookToTxt(book)
        self.showAndChooseMenu()

    def removeBook(self):
        if self.books:
            for i in range(len(self.books)):
                print(f"{i + 1}. Kitap Adı: {self.books[i][0]}")

            silinen = input("Silinecek Olan Kitabın Adı: ")

            bulundu = False
            for book in self.books:
                if book[0] == silinen:
                    self.books.remove(book)
                    bulundu = True
                    break

            if bulundu:
                print("Seçtiğiniz Kitap Silindi.")
                self.saveChanges()
            else:
                print("Seçtiğiniz kitap bulunamadı.")


        else:
            print("Kütüphanede kitap yok! Lütfen önce kitap ekleyin.")

        self.showAndChooseMenu()

    def __del__(self):
        print("Kütüphane kapanıyor")

    def showAndChooseMenu(self):
        print("\n----MENU------")
        print("1)Kitapları Listele\n2)Kitap Ekle\n3)Kitap Sil\n4)Çıkış\n")

        user_input = int(input("(1-4) Seçim Yapınız: "))

        if user_input == 1:
            self.listBook()
        elif user_input == 2:
            self.addBook()
        elif user_input == 3:
            self.removeBook()
        elif user_input == 4:
            self.status = False
        else:
            print("Lütfen Menüden Uygun Değerleri Seçiniz!")
            self.showAndChooseMenu()


lib = Library()

while lib.status:
    lib.showAndChooseMenu()

del lib
