

class Rectangle:



    def __init__(self, x: float, y:float):

        self.x: float = x

        self.y: float = y



    def area(self):

        return self.x * self.y

    

    def __str__(self):

        return f'Rectangle(x={self.x}, y={self.y})'

    

rect = Rectangle(2, 15)

area = rect.area()

print(f"L'area di {rect} è {area}")

