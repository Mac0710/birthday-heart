import math
from turtle import *
def hearta(k):
    return 15 * math.sin(k) ** 3
def heartb(k):
    return 12 * math.cos(k) - 5 * \
            math.cos(2 *k) - 2 * \
            math.cos(3 * k) - \
            math.cos(4 * k)
speed(0)
bgcolor("black")
for i in range(384):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(1):
        color("red")
        dot()
    hideturtle()
goto(0, 0)  # center of the heart
color("white")
write("Happy Birthdayyy B!!!", align="center", font=("Ariel", 24, "bold"))
hideturtle()
done()