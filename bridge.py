#Implementor Interface
class Color:
    def apply_color(self):
        raise NotImplementedError("This method should be overridden.")
        
#Concrete Implementors
class RedColor(Color):
    def apply_color(self):
        print("Applying red color.")

class BlueColor(Color):
    def apply_color(self):
        print("Applying blue color.")

        
#Abstraction
class Shape:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        raise NotImplementedError("This method should be overridden.")

#Refined Abstractions
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
        self.color.apply_color()

class Square(Shape):
    def draw(self):
        print("Drawing Square")
        self.color.apply_color()
        
#Client code
if __name__ == "__main__":
    red = RedColor()
    blue = BlueColor()

    red_circle = Circle(red)
    blue_square = Square(blue)

    red_circle.draw()
    blue_square.draw()


