
import os
def clear():
    os.system ("cls")

Books = {}
Out_Books = {}
Total_Books = {}

while True:
    
    #Main Menu
    print ("Menu:")
    print ("1. Add Book")
    print ("2. Check Out Book")
    print ("3. Check In Book")
    print ("4. List Books")
    print ("5. Exit")
    choice = input ("Enter your choice (1-5): ").strip()

    # Add Book
    if choice == "1":

     def Add():
         clear()
         Book_ISBN = input ("Enter ISBN: ").replace(" ","")
         # The ISBN must be a number
         if not Book_ISBN.isdigit():
            print ("That is not a number.")
            again = input ("Do you want to try again? (y/n): ").lower()
            Add() if again == "y" else print ()
          
         # The ISBN of the added book must be different from the others
         elif Book_ISBN in Books:
             print ("This book is already in the catalog.")
             print ()
         else:
            Book_title = input ("Enter title: ").strip()
            Book_author = input ("Enter author: ").strip()
            Books [Book_ISBN] = [Book_title, Book_author]
            Total_Books [Book_ISBN] = Books [Book_ISBN]
            print (f"Book '{Books [Book_ISBN] [0]}' by {Books [Book_ISBN] [1]} added to the catalog with ISBN {Book_ISBN}.")

            another = input ("Do you want to add another book? (y/n): ").lower()
            if another == "y":
               clear()
               Add()
            else:
               print()
         
     Add()
     
    # Check Out Book
    elif choice == "2":
        
     def Check_Out():
         clear()
         check_out = input ("Enter ISBN to check out: ").replace(" ","")
         # The ISBN of the added book must be in the catalog to check it out
         if check_out in Books:
            value1 = Books.pop(check_out)
            Out_Books [check_out] = value1
            print (f"Book '{Out_Books [check_out] [0]}' checked out successfully.")

         # If it has already been checked out
         elif check_out in Out_Books: 
            print ("Sorry, the book is currently checked out.")
         else:
            print ("Book not found in the catalog.")

         another = input ("Do you want to check out another book? (y/n): ").lower()
         if another == "y":
            clear()
            Check_Out()
         else:
            print()
    
     Check_Out()

    # Check In Book
    elif choice == "3":

        def Check_In():
            clear()
            check_in = input ("Enter ISBN to check in: ").replace(" ","")
            # To retrieve the book that has been checked out from the catalog
            if check_in in Out_Books:
               value2 = Out_Books.pop(check_in)  #To remove the key and store it in a variable
               Books [check_in] = value2  # To put the value back in the catalog
               print (f"Book '{Books [check_in] [0]}' checked in successfully.")

            # If the book is actually available in the catalog or has been returned
            elif check_in in Books:
               print ("The book is already in the catalog.")
            else:
               print ("Book not found in the catalog.")

            another = input ("Do you want to check in another book? (y/n): ").lower()
            if another == "y":
               clear()
               Check_In()
            else:
               print()
    
        Check_In()

    # List Books
    elif choice == "4":
     clear()
     print ("Library Catalog:")

     # To obtain the ISBN of each book in the "key"
     for key in Total_Books:
         available = key in Books
         List_Books = (f"ISBN: {key}, Title: {Total_Books [key] [0]}, Author: {Total_Books [key] [1]}, Available: {available}" )
         print (List_Books)

     menu_back = input ("Press any key to go back to the main menu . . . ")
     print ()

    # Exit 
    elif choice == "5":
       input ("Exiting the program . . .")
       break

    # Invalid
    else:
        print ("Invalid choice. Try again")
        input ("Press any key to continue . . .")
        print ()
