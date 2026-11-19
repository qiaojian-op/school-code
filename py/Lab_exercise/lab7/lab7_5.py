class Book:
    def __init__(self,title,author,year):
        self.__title=title
        self.__author=author
        self.__year=year
    def setTitle(self,title):
        self.__title=title
    def setAuthor(self,author):
        self.__author=author
    def setYear(self,year):
        self.__year=year
    def getTitle(self):
        print(self.__title)
    def getAuthor(self):
        print(self.__author)
    def getYear(self):
        print(self.__year)
    def displayBook(self):
        self.getTitle()
        self.getAuthor()
        self.getYear()
def main():
    book1=Book("The Great Gatsby","F. Scott Fitzgerald",1925)
    book2=Book("To Kill a Mockingbird","Harper Lee",1960)
    print("Book1 befor update: ")
    book1.displayBook()
    book1.setTitle("The Old Man And The Sea")
    book1.setAuthor("Erneast Hemingway")
    book1.setYear(1951)
    print("Book1 after update: ")
    book1.displayBook()
    print("Book2: ")
    book2.displayBook()
main()

      