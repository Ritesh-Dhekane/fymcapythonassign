print("Name = Ritesh Dhekane")


class Product:
    def __init__(self, name, amount, price):
        self.name = name  # product name
        self.amount = amount  # items in stock
        self.price = price  # regular price per item

    def get_price(self, quantity):
        """Return cost based on discount rules."""
        if quantity < 10:
            discount = 0
        elif 10 <= quantity <= 99:
            discount = 0.10  # 10% discount
        else:
            discount = 0.20  # 20% discount for 100+

        final_price = self.price * quantity * (1 - discount)
        return final_price

    def make_purchase(self, quantity):
        """Deduct purchased items from stock."""
        if quantity > self.amount:
            print("Not enough stock available!")
            return False
        else:
            self.amount -= quantity
            print(f"{quantity} items purchased successfully.")
            return True


# Example usage:
name = input("Enter product name: ")
amount = int(input("Enter number of items in stock: "))
price = float(input("Enter price per item: "))

product = Product(name, amount, price)

qty = int(input("\nHow many items do you want to buy? "))

cost = product.get_price(qty)
print(f"Total cost = {cost:.2f}")

# Make the purchase
product.make_purchase(qty)

print(f"Remaining stock: {product.amount}")
