from time import sleep
import math
from clicknium import clicknium as cc

# This function moves the mouse along a circle with a radius of 200 pixels.
# The circle is divided into 20 points, and the mouse moves to each point with a delay of 0.3 seconds between each move.
def circle():
    """Move the mouse along a circle."""
    mouse_x, mouse_y = cc.mouse.position()
    num_points = 20
    angle_between_points = (2 * math.pi) / num_points
    radius = 200
    while True:
        for i in range(0, num_points + 1):
            x = int(mouse_x + radius * math.sin(angle_between_points * i))
            y = int(mouse_y + radius * math.cos(angle_between_points * i))
            cc.mouse.move(x, y)
            sleep(0.9)

if __name__ == "__main__":
    circle()
