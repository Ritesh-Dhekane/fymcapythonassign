print("Name = Ritesh Dhekane")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return 3.14159 * (self.radius**2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * 3.14159 * self.radius


# Example usage:
r = float(input("Enter radius of the circle: "))
c = Circle(r)

print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())
