print("Name = Ritesh Dhekane")


class Library:
    def __init__(self):
        self.acc_number = ""
        self.title = ""
        self.author = ""
        self.publisher = ""

    # Method to read book details
    def read(self):
        self.acc_number = input("Enter Accession Number: ")
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Author Name: ")
        self.publisher = input("Enter Publisher Name: ")

    # Method to compute fine
    def compute(self):
        days_late = int(input("Enter number of days late: "))
        fine = days_late * 5  # ₹5 per day
        print(f"Fine Amount: ₹{fine}")

    # Method to display details
    def display(self):
        print("\n===== BOOK DETAILS =====")
        print("Accession Number:", self.acc_number)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publisher:", self.publisher)


book = Library()
book.read()
book.compute()
book.display()

