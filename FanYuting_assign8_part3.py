# function: bar_chart
# input: x & y value (integers), labels, values and colors (lists)
# processing: draws a bar chart with the origin of the chart being at the x
# and y value supplied. the height of the chart will always be
# 100 units, and the width of each bar in the chart can be
# computed as 50 units for each value in the 'values' list.
# draw two black lines to show these axes.
#
# the height of each bar should be proportionatly scaled so that
# no bar ever ends up having a height of over 100 units. for example,
# with the list [100,200,300] the third bar would be 100 units
# high, the second would only be 66.6 units high and the first would
# be 33.3 units high.
# 
# each value in the 'labels' list indicates the label for each bar
# in the bar chart. these should be written below the x-axis
# using the 'turtle.write' function. Ensure that these labels are
# spaced out accordingly (50 pixels for each bar)
# 
# each bar should be drawn on top of the x-axis with a height defined
# in the 'values' list. the color for each bar can be extracted
# from the 'colors' list. the value of each bar should also be 
# written at the top of each bar.
# output: function returns no value

import turtle
def bar_chart(x, y, labels, values, colors):
    max_value = max(values)
    heights = [values[i] / max_value * 100 for i in range(len(values))]
    for i in range(len(labels)):
        turtle.up()
        turtle.goto(x + 50 * i, y - 20)
        turtle.down()
        turtle.write(labels[i])
        turtle.up()
        turtle.goto(x + 50 * i + 5, y + heights[i] + 10)
        turtle.down()
        turtle.write(values[i])
        drawRectangle(turtle, x + 50 * i, y, 50, heights[i], colors[i])


def drawRectangle(t, x, y, w, h, color):
    t.pencolor("black")
    t.fillcolor(color)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)
    t.end_fill()


turtle.setup(600,600)
bar_chart(-200,-200,["pikachu"], [99999], ['yellow'])
bar_chart(0,-200,["x","y","hello","world"], [1000,900,800,700], ['grey','pink','black','purple'])
bar_chart(-200,0,["apple", "pear", "orange"], [100,200,300], ['red', 'green', 'orange'])
bar_chart(0,0,["a","b","c","d","e"], [50,70,90,10,30], ['blue','pink','red','green','yellow'])


turtle.done()