class Rectangle:
    # constructor
    def __init__(self, x, y, width, height):
        '''
        constructor
        x: (int) the x coordinate of its upper left position
        y: (int) the y coordinate of its upper left position
        width: (int) the width of the rectangle
        height: (int) the height of the rectangle
        '''

        if x > 0:
            self.x = x
        else:
            self.x = 0
         
        if y > 0:
            self.y = y
        else:
            self.y = 0

        if height > 0:
            self.height = height
        else:
            self.height = 0

        if width > 0:
            self.width = width
        else:
            self.width = 0    

    def __str__(self):
        '''
        convert to string
        return (str) a string representation of the object.
        '''
        return '(x: ' + str(self.x) + \
              ', y: ' + str(self.y) + \
              ', width: ' + str(self.height) + \
              ', height: ' + str(self.width) + ')'


v1 = Rectangle(5, 10, 50, 100)
print(v1)

v2 = Rectangle(-5, -10, -50, -100)
print(v2)