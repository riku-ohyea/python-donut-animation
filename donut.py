import os
import time
import math
import sys

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Donut parameters
A = 1
B = 1

# Rotating donut animation
def rotating_donut():
    global A, B  # Declare A and B as global
    while True:
        clear_terminal()
        z = [0] * 1760
        b = [' '] * 1760
        for j in range(0, 628, 7):  # Angle in radians
            for i in range(0, 628, 2):  # Angle in radians
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(A)
                f = math.sin(j)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = int(x + 80 * y)
                # Ensure N is within range
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - c * d * n))
                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o] = D
                    # Constrain N to be between 0 and 7
                    b[o] = '.,-~:;=!*#$@'[min(max(N, 0), 7)]

        # Render the donut
        for k in range(1760):
            print(b[k], end=('\n' if k % 80 == 79 else ''))

        A += 0.04
        B += 0.02
        time.sleep(0.1)  # Delay to control speed

# Run the animation
try:
    rotating_donut()
except KeyboardInterrupt:
    sys.exit()
