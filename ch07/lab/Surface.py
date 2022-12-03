from Rectangle import Rectangle


class Surface:
    # constructor
    def __init__(self, filename: str, x, y, width, height):
        '''
        constructor
        filename: (str) image file name
        x: (int) the x coordinate of its upper left position
        y: (int) the y coordinate of its upper left position
        width: (int) the width of the rectangle
        height: (int) the height of the rectangle
        '''
        self.image = filename
        self.rect = Rectangle(x, y, height, width)

    def getRect(self):
        '''
        getter for the rect
        return: (Rectangle) rect for the surface
        '''
        return self.rect


v1 = Rectangle(5, 10, 50, 100)
print(v1)

v2 = Rectangle(-5, -10, -50, -100)
print(v2)