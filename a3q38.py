print("Name = Ritesh Dhekane")


class StringClass:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        """Reads a string from the user."""
        self.my_string = input("Enter a string: ")

    def printString(self):
        """Prints the string in upper case."""
        print("String in UPPERCASE:", self.my_string.upper())


# Example usage:
obj = StringClass()
obj.getString()
obj.printString()
