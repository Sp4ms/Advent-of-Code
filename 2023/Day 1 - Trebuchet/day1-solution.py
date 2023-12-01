# --- Day 1: Trebuchet?! ---

# Combine the first and last digit (in that order) to form a single two digit number.
# Then sum all the calibration values
import sys, re

def calibrate_value(line):
    num_words = ['one','two','three','four','five','six','seven','eight','nine']
    for i, n in enumerate(num_words):
        # add digit + keep word on both sides (handles overlapping edge cases)
        line = line.replace(n, n + str(i+1) + n)
    regex = re.findall(r'(\d)', line)
    # return integer of first and last digits combined
    return int(regex[0] + regex[-1])

# Open input file for reading and print sum
print(sum(map(calibrate_value, open(sys.argv[1], "r"))))