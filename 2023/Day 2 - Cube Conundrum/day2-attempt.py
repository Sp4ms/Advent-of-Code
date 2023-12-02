# --- Day 2: Cube Conundrum ---
import re, sys

# For each game, find the minimum set of cubes that must have been present. 
# What is the sum of the power of these sets?

def conundrum(line):
    bT, gT, rT = 0, 0, 0
    
    # split line (by each game)
    for n in re.split('; |: |\n', line):
        blue, green, red = 0, 0, 0

        # split each game by color
        for nn in re.split(', ', n):
            if "blue" in re.split('\s', nn):
                blue = int(re.split('\s', nn)[0])
                if blue > bT:
                    bT = blue
            elif "green" in nn.split():
                green = int(re.split('\s', nn)[0])
                if green > gT:
                    gT = green
            elif "red" in nn.split():
                red = int(re.split('\s', nn)[0])
                if red > rT:
                    rT = red

    return bT * gT * rT

# Open input file for reading and print sum
print(sum(map(conundrum, open(sys.argv[1], "r"))))
