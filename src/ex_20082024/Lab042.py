# ✅ Grade Calculator: in simplified chanined
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

if 90 <= Score <= 100:
    grade = "A"
    print(f"your grade is {grade}")

elif 80 <= Score < 90:
    grade = "B"
    print(f"your grade is {grade}")
elif 70 <= Score < 80:
    grade = "C"
    print(f"your grade is {grade}")
elif 60 <= Score < 70:
    grade = "D"
    print(f"your grade is {grade}")
elif 0 <= Score < 60:
    grade = "E "
    print(f"your grade is {grade}")
else:
    grade = "F "
    print(f"your grade is {grade}")
