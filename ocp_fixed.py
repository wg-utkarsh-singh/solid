from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle:
    def __init__(self, length, breadth):
        pass

    def area(self):
        pass


class DrawableRectangle(Drawable, Rectangle):
    def draw(self):
        pass


class Square:
    def __init__(self, side):
        pass

    def area(self):
        pass


class DrawableSquare(Drawable, Square):
    def draw(self):
        pass


def draw_all_shapes(shapes):
    for shape in shapes:
        shape.draw()
