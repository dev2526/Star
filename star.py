import turtle

turtle.Screen().bgcolor("Orange")
sc= turtle.Screen()
sc.setup(400,300)


turtle.title("welcome to python turtle")

board=turtle.Turtle()

#first triangle
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.left(120)


board.penup()
board.right(150)
board.forward(50)

#second triangle
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)


turtle.done()

