print("Name = Ritesh Dhekane")

from pymongo import MongoClient

# -----------------------------
#  FUNCTION: CONNECT TO DB
# -----------------------------
def connect_db():
    # client = MongoClient("mongodb://localhost:27017/")
    client = MongoClient("mongodb+srv://learnriteshdhekane_db_user:Ritesh884@temp-python.1gpstub.mongodb.net/?appName=temp-python")
    db = client["LibraryDB"]
    return db["Book"]       # return the Book collection


# -----------------------------
#  FUNCTION: CREATE COLLECTION & INSERT DOCUMENTS
# -----------------------------
def insert_books(collection):
    print("\nEnter details of 5 books:\n")

    for i in range(5):
        print(f"--- Book {i+1} ---")
        name = input("Enter Book Name: ")
        code = input("Enter Book Code: ")
        author = input("Enter Book Author: ")
        price = float(input("Enter Book Price: "))
        pub_year = int(input("Enter Publication Year: "))

        doc = {
            "Book-name": name,
            "Book-code": code,
            "Book-Author": author,
            "Book-Price": price,
            "Book-publication-year": pub_year
        }
        collection.insert_one(doc)

    print("\nBooks inserted successfully!\n")


# -----------------------------
#  FUNCTION: FIND BOOKS WITH PRICE BETWEEN 500–800
# -----------------------------
def find_books_in_range(collection):
    print("\nBooks priced between 500 and 800:\n")
    result = collection.find({
        "Book-Price": {"$gte": 500, "$lte": 800}
    })

    for book in result:
        print(book)


# -----------------------------
#  FUNCTION: UPDATE PRICE OF A BOOK
# -----------------------------
def update_price(collection):
    book_name = "Python programming"
    new_price = 1000

    result = collection.update_one(
        {"Book-name": book_name},
        {"$set": {"Book-Price": new_price}}
    )

    if result.modified_count > 0:
        print(f"\nPrice updated for '{book_name}'!\n")
    else:
        print(f"\nBook '{book_name}' not found!\n")


# -----------------------------
#  FUNCTION: DISPLAY BOOKS SORTED BY PUBLICATION YEAR
# -----------------------------
def display_sorted_books(collection):
    print("\nBooks sorted by publication year:\n")
    result = collection.find().sort("Book-publication-year", 1)

    for book in result:
        print(book)


# -----------------------------
#  MAIN PROGRAM
# -----------------------------
def main():
    collection = connect_db()

    print("\n--- MENU ---")
    print("1. Insert 5 Books")
    print("2. Find Books with Price 500–800")
    print("3. Update Price of 'Python programming'")
    print("4. Display Books Sorted by Publication Year")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            insert_books(collection)
        elif choice == 2:
            find_books_in_range(collection)
        elif choice == 3:
            update_price(collection)
        elif choice == 4:
            display_sorted_books(collection)
        else:
            print("Invalid choice!")

        cont = input("\nDo you want to continue (y/n)? ")
        if cont.lower() != "y":
            break


main()
