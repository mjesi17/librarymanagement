import os
class Book:
    def __init__(self, bname, bid, bkflag):
        self.bname = bname
        self.bid = bid
        self.bkflag = bkflag

class Student:
    def __init__(self, sname, spass, sid):
        self.sname = sname
        self.spass = spass
        self.sid = sid
        self.rbook = None

books = []
students = []
bcount = 0
bookid = 101
scount = 0
sid = 1001

def view_books():
    print("\n")
    for book in books:
        availability = "Available" if book.bkflag == 1 else "Not Available"
        print(f"Book name: {book.bname}\tBook Id: {book.bid}\t{availability}")
    print("\n")

def admin():
    global bcount, bookid
    username = input("Enter user name: ")
    password = input("Enter password: ")
    if username == "Library" and password == "Mylibrary":
        while True:
            print("\n----------> ADMIN <------------\n")
            print("1. Add Book")
            print("2. View Book")
            print("3. Report Book")
            print("4. Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                m = int(input("\nHow many Books to add: "))
                for _ in range(m):
                    bname = input("\nEnter Book name: ")
                    books.append(Book(bname, bookid, 1))
                    print(f"Your Book id is: {bookid}")
                    bookid += 1
                    bcount += 1
            elif choice == 2:
                view_books()
            elif choice == 3:
                report_books()
            elif choice == 4:
                break
            else:
                print("\nInvalid choice...\n")
    else:
        print("\nUser name or password is wrong...\n")

def stu():
    global scount, sid
    while True:
        print("\n-------------> STUDENT LOGIN <--------------\n")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            a = int(input("\nEnter user id: "))
            b = input("Enter password: ")
            student = next((s for s in students if s.sid == a and s.spass == b), None)
            if student:
                while True:
                    print("1. View Book")
                    print("2. Lend Book")
                    print("3. Return Book")
                    print("4. Log out")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        view_books()
                    elif choice == 2:
                        d = input("Enter Book name: ")
                        c = int(input("Enter Book id: "))
                        book = next((b for b in books if b.bid == c), None)
                        if student.rbook is None and book and book.bkflag == 1:
                            student.rbook = book.bid
                            book.bkflag = 0
                            print(f"{book.bname} Lent Successfully...")
                        elif student.rbook is not None:
                            print("Already you have lent a book...")
                        else:
                            print("Book Not Available...")
                    elif choice == 3:
                        book_id = student.rbook
                        if book_id is not None:
                            book = next((b for b in books if b.bid == book_id), None)
                            if book and book.bkflag == 0:
                                print(f"Book name: {book.bname}")
                                book.bkflag = 1
                                student.rbook = None
                                print("Return Successfully...")
                            else:
                                print("You haven't borrowed a book...")
                        else:
                            print("You haven't borrowed a book...")
                    elif choice == 4:
                        break
                    else:
                        print("Invalid choice...\n")
            else:
                print("\nUser id or password is wrong...\n")
        elif choice == 2:
            sname = input("\nEnter Member name: ")
            spass = input("Enter Password: ")
            sid += 1
            students.append(Student(sname, spass, sid))
            scount += 1
            print(f"Your Membership id is: {sid}")
        elif choice == 3:
            break
        else:
            print("\nInvalid choice...\n")

def report_books():
    with open("out.txt", "w") as f:
        for book in books:
            availability = "Available" if book.bkflag == 1 else "Not Available"
            f.write(f"Book name: {book.bname}\tBook Id: {book.bid}\t{availability}\n")
    print("Report done")

def main():
    while True:
        print("\n1. Admin")
        print("2. Student")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            admin()
        elif choice == 2:
            stu()
        elif choice == 3:
            print("\n         Thank you        ")
            break
        else:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()
