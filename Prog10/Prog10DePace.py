from graphics import *

win = GraphWin("Test", 400, 400)

circ = Circle(Point(50, 50), 50)
circ.setFill("red")
circ.draw(win)

win.getMouse()
