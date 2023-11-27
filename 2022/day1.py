# --- Day 1: Calorie Counting ---

# Read input file
f = open("day1-input.txt", "r")
calories = 0
largestElf = 0
currentElf = 0
largestCals = 0

calorieList = []
elfList = []

for line in f:
    if line in ['\n', '\r\n']:
        currentElf += 1
        calorieList.append(calories)
        elfList.append(currentElf)
        if largestCals >= calories:
            calories = 0
        else:
            largestCals = calories
            calories = 0
            largestElf = currentElf
            print("Elf " + str(largestElf) + " carrying: " + str(largestCals))
    else:
        calories += int(line)

top3 = sorted(zip(calorieList, elfList), reverse=True)[:3]
print(top3)
top3Calories = top3[0][0] + top3[1][0] + top3[2][0]
print(top3Calories)
#print("The Elf with the most calories was: " + str(largestElf) + " and they were carrying " + str(largestCals) + " calories")

# Close input file
f.close()