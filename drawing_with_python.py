
import turtle

def drawShape(sides,length):
  direction = 360 / sides
  for i in range(1,sides + 1):
    turtle.forward(length)
    turtle.right(direction)

drawShape(4,50)
drawShape(5,50)