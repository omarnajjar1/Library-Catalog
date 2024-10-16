import os
library_catalog = {}
def clear_terminal():
    os.system ("cls")

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

     def add_book():
         clear_terminal()
         isbn = input ("Enter ISBN: ").replace(" ","")

         # The ISBN must be a number
         if not isbn.isdigit():
            print ("That is not a number.")
            again = input ("Do you want to try again? (y/n): ").lower()
            add_book() if again == "y" else print ()
          
         # The ISBN of the added book must be different from the others
         elif isbn in library_catalog:
              print ("This book is already in the catalog.")
              again = input ("Do you want to try again? (y/n): ").lower()
              add_book() if again == "y" else print ()
         else:
            title = input ("Enter title: ").strip()
            author = input ("Enter author: ").strip()
            library_catalog [isbn] = {"title": title, "author": author, "available": True}
            print (f"Book '{title}' by {author} added to the catalog with ISBN {isbn}.")

            choice = input ("Do you want to add another book? (y/n): ").lower()
            if choice == "y":
               clear_terminal()
               add_book()
            else:
               print()
         
     add_book()
     
    # Check Out Book
    elif choice == "2":
        
     def check_out_book():
         clear_terminal()
         isbn= input ("Enter ISBN to check out: ").replace(" ","")

         # The ISBN of the added book must be in the catalog to check it out
         if isbn in library_catalog:
            if library_catalog [isbn] ["available"]:
               library_catalog [isbn] ["available"] = False
               print (f"Book '{library_catalog [isbn] ["title"]}' checked out successfully.")
            elif library_catalog [isbn] ["available"] == False: # The book is currently borrowed
                 print ("Sorry, the book is currently checked out.")
         else:
            print ("Book not found in the catalog.")

         choice= input ("Do you want to check out another book? (y/n): ").lower()
         if choice == "y":
            clear_terminal()
            check_out_book()
         else:
            print()
    
     check_out_book()

    # Check In Book
    elif choice == "3":

        def check_in_book():
            clear_terminal()
            isbn = input ("Enter ISBN to check in: ").replace(" ","")

            # If the book is actually available in the catalog or has been returned
            if isbn in library_catalog:
               if library_catalog [isbn] ["available"]:
                  print ("Sorry, this book is already available in library.")

               else: # Returning the book to the library
                  library_catalog [isbn] ["available"] = True
                  print (f"Book '{library_catalog [isbn] ["title"]}' checked in successfully.")
            else:
                  print ("Book not found in the catalog")
          
            another = input ("Do you want to check in another book? (y/n): ").lower()
            if another == "y":
               clear_terminal()
               check_in_book()
            else:
               print()
    
        check_in_book()

    # List Books
    elif choice == "4":

     def list_books():
         clear_terminal()
         print ("Library Catalog:")

         # To obtain the ISBN of each book 
         for isbn in library_catalog:
             List_Books = (f"ISBN: {isbn}, Title: {library_catalog [isbn] ["title"]}, Author: {library_catalog [isbn] ["author"]}, Available: {library_catalog [isbn] ["available"]}" )
             print (List_Books)

         choice = input ("Do you want to go back to the main menu? (y/n): ").lower()
         list_books() if choice != "y" else print()
     
     list_books()

    # Exit 
    elif choice == "5":
       input ("Exiting the program . . .")
       break

    # Invalid
    else:
        print ("Invalid choice. Try again")
        input ("Press any key to continue . . .")
        print ()
