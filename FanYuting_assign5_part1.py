


def letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 63:
        return "D"
    elif grade >= 0:
        return "F"

stu_num = int(float(input("How many students are in your class? ")))
print()
test_num = int(float(input("How many tests will you be giving in this class? ")))
print()
extra_credit = input("Is extra credit allowed? This will permit tests scores to exceed 100 points (yes/no): ")
print()
if extra_credit.lower() == "yes":
    extra_credit = float("inf")
else:
    extra_credit = 100

drop_lowest = input("Would you like to drop the lowest test for each student? (yes/no): ")
if drop_lowest.lower()  == "yes":
    drop_lowest = True
else:
    drop_lowest = False

print("\nThanks, here we go!\n")

student_data = [[] for _ in range(stu_num)]
letter_grade_list = [0,0,0,0,0]
sum_grade = 0
for i in range(stu_num):
    size = 0
    print("*** Student #%d ***"%(i+1))
    while size != test_num:
        p = float(input("Enter score for test #%d: "%(size+1)))
        if p < 0:
            print("Score cannot be negative, try again.")
            continue
        elif p > extra_credit:
            print("Extra credit mode is not enabled, try again.")
            continue
        student_data[i].append(p)
        size+=1
    student_data[i].sort()
    print()
    if drop_lowest:
        print("Dropping the lowest test score for this student (%.1f)"%student_data[i][0])
        student_data[i].pop(0)
    grade = sum(student_data[i])/len(student_data[i])
    sum_grade += grade
    if letter_grade(grade) == "A":
        letter_grade_list[0] += 1
    elif letter_grade(grade) == "B":
        letter_grade_list[1] += 1
    elif letter_grade(grade) == "C":
        letter_grade_list[2] += 1
    elif letter_grade(grade) == "D":
        letter_grade_list[3] += 1
    elif letter_grade(grade) == "F":
        letter_grade_list[4] += 1
    print("Average score for student #1 is %.2f (%s)\n"%(grade, letter_grade(grade)))

print("----- REPORT -----")
print("Overall class average: %.2f (%s)"%(sum_grade/stu_num, letter_grade(sum_grade/stu_num)))
print("# of students who earned an 'A' average: %d"%letter_grade_list[0])
print("# of students who earned an 'B' average: %d"%letter_grade_list[1])
print("# of students who earned an 'C' average: %d"%letter_grade_list[2])
print("# of students who earned an 'D' average: %d"%letter_grade_list[3])
print("# of students who earned an 'F' average: %d"%letter_grade_list[4])
