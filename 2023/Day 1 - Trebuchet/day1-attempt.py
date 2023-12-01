# --- Day 1: Trebuchet?! ---

# Combine the first and last digit (in that order) to form a single two digit number.
# Then sum all the calibration values

# Read input file
f = open("input.txt", "r")

calibration_values = []
current_value = 0

for line in f:
    line_digits = []
    cal_val = ""
    digit_string = ""
    line = line.strip()
    for digit in range(0, len(line)):

        #print("Current digit: " + str(line[digit]) + " AND Current digit_string Length: " + str(len(digit_string)))
        if line[digit].isdigit():
            line_digits.append(line[digit])
            #print("Adding " + str(line[digit]))
            digit_string = ""
        
        # first character
        elif len(digit_string) == 0:
            # one
            if line[digit] == "o":
                digit_string = line[digit]
            # two or three
            elif line[digit] == "t":
                digit_string = line[digit]
            # four or five
            elif line[digit] == "f":
                digit_string = line[digit]
            # six or seven
            elif line[digit] == "s":
                digit_string = line[digit]
            # eight
            elif line[digit] == "e":
                digit_string = line[digit]
            # nine
            elif line[digit] == "n":
                digit_string = line[digit]
            else:
                digit_string = ""
            
        # second character
        elif len(digit_string) == 1:
            # one
            if line[digit] == "n":
                if digit_string == "o":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = line[digit]
            # two or three
            elif line[digit] == "w" or line[digit] == "h":
                if digit_string == "t":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = ""
            # four
            elif line[digit] == "o":
                if digit_string == "f":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = line[digit]
            # five (or six or eight or nine)
            elif line[digit] == "i":
                if digit_string == "f" or digit_string == "s" or digit_string == "e" or digit_string == "n":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = ""
            # seven
            elif line[digit] == "e":
                if digit_string == "s":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = line[digit]
            # fresh start
            elif line[digit] == "t" or line[digit] == "f" or line[digit] == "s":
                digit_string = line[digit]
            else:
                digit_string = ""

        # third character
        elif len(digit_string) == 2:
            # one
            if line[digit] == "e":
                if digit_string == "on":
                    digit_string = digit_string + line[digit]
                    line_digits.append("1")
                    #print("Adding 1")
                    digit_string = line[digit]
                else:
                    digit_string = line[digit]
            # two
            elif line[digit] == "o":
                if digit_string == "tw":
                    digit_string = digit_string + line[digit]
                    line_digits.append("2")
                    #print("Adding 2")
                    digit_string = line[digit]
                else:
                    digit_string = line[digit]
            # three
            elif line[digit] == "r":
                if digit_string == "th":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = ""
            # four
            elif line[digit] == "u":
                if digit_string == "fo":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = ""
            # five (or seven)
            elif line[digit] == "v":
                if digit_string == "fi" or digit_string == "se":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = ""
            # six
            elif line[digit] == "x":
                if digit_string == "si":
                    digit_string = digit_string + line[digit]
                    line_digits.append("6")
                    #print("Adding 6")
                    digit_string = ""
                else:
                    digit_string = ""
            # eight
            elif line[digit] == "g":
                if digit_string == "ei":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = ""
            # nine
            elif line[digit] == "n":
                if digit_string == "ni":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = line[digit]
            # fresh start
            elif line[digit] == "t" or line[digit] == "f" or line[digit] == "s":
                digit_string = line[digit]
            else:
                digit_string = ""

        # fourth character
        elif len(digit_string) == 3:
           # three (or five or seven or nine)
            if line[digit] == "e":
                if digit_string == "thr" or digit_string == "sev":
                    digit_string = digit_string + line[digit]
                elif digit_string == "fiv":
                    digit_string = digit_string + line[digit]
                    line_digits.append("5")
                    #print("Adding 5")
                    digit_string = line[digit]
                elif digit_string == "nin":
                    digit_string = digit_string + line[digit]
                    line_digits.append("9")
                    #print("Adding 9")
                    digit_string = line[digit]
                else:
                    digit_string = line[digit]
            # four
            elif line[digit] == "r":
                if digit_string == "fou":
                    digit_string = digit_string + line[digit]
                    line_digits.append("4")
                    #print("Adding 4")
                    digit_string = ""
                else:
                    digit_string = ""
            # eight
            elif line[digit] == "h":
                if digit_string == "eig":
                    digit_string = digit_string + line[digit]
                else:
                    digit_string = ""
            # fresh start
            elif line[digit] == "o" or line[digit] == "t" or line[digit] == "f" or line[digit] == "s" or line[digit] == "n":
                digit_string = line[digit]
            else:
                digit_string = ""

        # fifth character
        elif len(digit_string) == 4:
            # three
            if line[digit] == "e":
                if digit_string == "thre":
                    digit_string = digit_string + line[digit]
                    line_digits.append("3")
                    #print("Adding 3")
                    digit_string = line[digit]
                else:
                    digit_string = line[digit]
            # seven
            elif line[digit] == "n":
                if digit_string == "seve":
                    digit_string = digit_string + line[digit]
                    line_digits.append("7")
                    #print("Adding 7")
                    digit_string = line[digit]
                else:
                    digit_string = line[digit]
            # eight
            elif line[digit] == "t":
                if digit_string == "eigh":
                    digit_string = digit_string + line[digit]
                    line_digits.append("8")
                    #print("Adding 8")
                    digit_string = line[digit]
                else:
                    digit_string = line[digit]
            # fresh start
            elif line[digit] == "o" or line[digit] == "f" or line[digit] == "s":
                digit_string = line[digit]
            else:
                digit_string = ""

    if len(line_digits) == 0:
#        print("A rare line with no digits!")
        cal_val = ""
    elif len(line_digits) == 1:
        cal_val = line_digits[0] + line_digits[0]
        calibration_values.append(cal_val)
    else:
        cal_val = line_digits[0] + line_digits[len(line_digits)-1]
        calibration_values.append(cal_val)
    

sum = 0
for cal_val in calibration_values:
    sum += int(cal_val)

#print(calibration_values)   
print("SUM: " + str(sum))

# Close input file
f.close()