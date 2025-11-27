import os
import csv


def newBook():
    print("Add a new Book Record")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    f = open("library.csv", "a", newline="\r\n")
    s = csv.writer(f)
    bookid = int(input("Enter book id:"))
    bookname = input("Enter book name:")
    bookauthor = input("Enter author name:")
    price = float(input("Enter price:"))
    copies = float(input("Enter number of copies:"))
    rec = [bookid, bookname, bookauthor, price, copies]
    s.writerow(rec)
    f.close()
    print("★Book Record Saved★")
    input("Press any key to continue..")


def modify():
    print("Modify a Book Record")
    print("--------------------------")
    f = open("library.csv", "r", newline="\r\n")
    f1 = open("temp.csv", "w", newline="\r\n")
    f1 = open("temp.csv", "a", newline="\r\n")
    r = input("Enter bookid whose record you want to modify=")
    s = csv.reader(f)
    s1 = csv.writer(f1)
    for rec in s:
        if rec[0] == r:
            print("----------------------------------------")
            print("Book id=", rec[0])
            print("Book Name=", rec[1])
            print("Author=", rec[2])
            print("Price=", rec[3])
            print("Number of copies=", rec[4])
            print("----------------------------------------")
            choice = input("Do you want to modify this Book Record(y/n)=")
            if choice == 'y' or choice == 'Y':
                bookid = int(input("Enter new book id="))
                bookname = input("Enter new book name=")
                bookauthor = input("Enter new author name=")
                price = float(input("Enter new price="))
                copies = float(input("Enter new number of copies="))
                rec = [bookid, bookname, bookauthor, price, copies]
                s1.writerow(rec)
                print("Book Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)

    f.close()
    f1.close()
    os.remove("library.csv")
    os.rename("temp.csv", "library.csv")
    input("Press any key to continue.." )


def delete():
    print("Delete a Book Record")
    f = open("library.csv", "r", newline="\r\n")
    f1 = open("temp.csv", "w", newline="\r\n")
    f1 = open("temp.csv", "a", newline="\r\n")
    r = input("Enter bookid whose record you want to delete=")
    s = csv.reader(f)
    s1 = csv.writer(f1)
    for rec in s:
        if rec[0] == r:
            print("----------------------------------------")
            print("Book id=", rec[0])
            print("Book Name=", rec[1])
            print("Author=", rec[2])
            print("Price=", rec[3])
            print("Number of copies=", rec[4])
            print("----------------------------------------")
            choice = input("Do you want to delete this Book Record(y/n)")
            if choice == 'y' or choice == 'Y':
                print("Book Record Deleted.....")
                # do not write this record
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)

    f.close()
    f1.close()
    os.remove("library.csv")
    os.rename("temp.csv", "library.csv")
    input("Press any key to continue.." )


def searchBook():
    print("Search a Book Record")
    print("--------------------------")
    f = open("library.csv", "r", newline="\r\n")
    s = csv.reader(f)
    r = input("Enter bookid you want to search = ")
    found = False
    for rec in s:
        if rec[0] == r:
            print("----------------------------------------")
            print("Book id=", rec[0])
            print("Book Name=", rec[1])
            print("Author=", rec[2])
            print("Price=", rec[3])
            print("Number of copies=", rec[4])
            print("----------------------------------------")
            found = True
            break
    if not found:
        print("Record not found")
    f.close()
    input("Press any key to continue.." )


def listBooks():
    print("List of all Books")
    print("--------------------------")
    f = open("library.csv", "r", newline="\r\n")
    s = csv.reader(f)
    count = 0
    for rec in s:
        print("----------------------------------------")
        print("Book id=", rec[0])
        print("Book Name=", rec[1])
        print("Author=", rec[2])
        print("Price=", rec[3])
        print("Number of copies=", rec[4])
        count += 1
    if count == 0:
        print("No records in file")
    print("--------------------------")
    f.close()
    input("Press any key to continue.." )


def mainMenu():
    while True:
        print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
        print("Library Management System")
        print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("        Main Menu           ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Add a new Book Record")
        print("2. Modify Existing Book Record")
        print("3. Delete Existing Book Record")
        print("4. Search a Book")
        print("5. List all Books")
        print("6. Exit")
        print("--------------------------------")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            newBook()
        elif choice == 2:
            modify()
        elif choice == 3:
            delete()
        elif choice == 4:
            searchBook()
        elif choice == 5:
            listBooks()
        elif choice == 6:
            print("Software Terminated.......")
            break
        else:
            print("Invalid choice...")


# start the program
mainMenu()
