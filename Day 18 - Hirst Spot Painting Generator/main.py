import colorgram
import turtle as t
import random
# change color mode to RGB
t.colormode(255)
point = t.Turtle()

# # extract a list of colors from an image
# colors = colorgram.extract("image.jpg", 30)
# color_list = []
# for color in colors:
#     rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
#     color_list.append(rgb)

# list of RGB colors generated from an image using the above code
colors = [(208, 159, 108), (223, 206, 117), (136, 173, 194), (215, 231, 240), (39, 107, 140), (137, 184, 147),
          (13, 52, 76), (219, 87, 63), (145, 80, 71), (70, 165, 119), (30, 129, 106), (125, 80, 96), (10, 58, 50),
          (55, 153, 180), (196, 130, 144), (52, 33, 43), (129, 37, 49), (4, 111, 88), (207, 83, 101), (176, 206, 167),
          (230, 168, 182), (155, 152, 70), (145, 204, 233), (33, 64, 101), (13, 87, 105), (46, 30, 26), (184, 189, 204)]

# position the marker in the left corner of the screen
point.setheading(225)
point.penup()
point.forward(350)
point.setheading(0)

y = -247.49
for i in range(10):
    point.setposition(-247.49, y)
    for m in range(10):
        point.dot(20, random.choice(colors))
        point.forward(1)
        point.penup()
        point.forward(50)
        y += 5
point.hideturtle()

screen = t.Screen()
screen.exitonclick()