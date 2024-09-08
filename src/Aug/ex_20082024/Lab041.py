# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else


### logic building
### Step1: input -> score -> int
### Step2: o/p : -> Grade - > str
### Step3: rough logic
## if   90 <= score <= 100: elif 80 <= score <= 89:

Score = int(input("Enter the score:\n"))

if Score >= 90 and Score <= 100:
    grade = "A"
    print(f"your grade is {grade}")

elif Score >= 80 and Score < 90:
    grade = "B"
    print(f"your grade is {grade}")
elif Score >= 70 and Score < 80:
    grade = "C"
    print(f"your grade is {grade}")
elif Score >= 60 and Score < 70:
    grade = "D"
    print(f"your grade is {grade}")
elif Score >= 0 and Score < 60:
    grade = "E "
    print(f"your grade is {grade}")
else:
    grade = "F "
    print(f"your grade is {grade}")
