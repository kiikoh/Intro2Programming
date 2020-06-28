class Rectangle:
    """The class represents a rectangle object"""

    def __init__(self, wid=10, ht=5, fill="*"):
        """Creates a rectangle object of size wid by ht using character fill"""
        self.myWidth = wid
        self.myHeight = ht
        self.myFillStyle = fill

    def __str__(self):
        """Returns a string representation of a rectangle"""
        return "A {}x{} Rectangle made of {} has area {} and perimeter {}".format(self.myWidth, self.myHeight, self.myFillStyle, self.calcArea(), self.calcPerimeter())

    def drawRectangle(self):
        """Draws the rectangle"""
        for i in range(self.myHeight):
            # print a string of fill style self.myWidth long
            print(self.myFillStyle * self.myWidth)
        print()

    def drawOutline(self):
        """Draws the outline of the rectangle"""
        # Print the top outline
        print(self.myWidth * self.myFillStyle)
        for i in range(self.myHeight - 2):
            # Print the two end characters then fill the inside with spaces
            print(self.myFillStyle + " " * (self.myWidth - 2) + self.myFillStyle)
        # Print the bottom outline
        print(self.myWidth * self.myFillStyle)
        print()

    def getWidth(self):
        """Returns the width of the rectangle"""
        return self.myWidth

    def setWidth(self, newWidth):
        """Sets the width of the rectangle"""
        # Validate the data
        if newWidth > 0:
            self.myWidth = newWidth
        else:
            return "Error: must be greater than 0"

    def getHeight(self):
        """Returns the height of the rectangle"""
        return self.myHeight

    def setHeight(self, newHeight):
        """Sets the height of the rectangle"""
        # Validate the data
        if newHeight > 0:
            self.myHeight = newHeight
        else:
            return "Error: must be greater than 0"

    def getFillStyle(self):
        """Returns the fill style character"""
        return self.myFillStyle

    def setFillStyle(self, newFillStyle):
        """Sets the new fill style"""
        self.myFillStyle = newFillStyle[0]

    def calcArea(self):
        """Returns the area of the rectangle"""
        # A = w*h
        return self.myWidth * self.myHeight

    def calcPerimeter(self):
        """Returns the perimeter of the rectangle"""
        # P = (w+h) * 2
        return (self.myWidth + self.myHeight) * 2

