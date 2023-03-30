class Rectangle:
    def __init__(self, length, breadth):
        pass

    def area(self):
        pass


class DrawableRectangle(Rectangle):
    def draw_rectangle(self):
        pass


class Square(Rectangle):
    def __init__(self, side):
        pass


class DrawableSquare(Square):
    def draw_square(self):
        pass


def draw_all_shapes(shapes):
    for shape in shapes:
        if isinstance(shape, DrawableRectangle):
            pass
        elif isinstance(shape, DrawableSquare):
            pass
