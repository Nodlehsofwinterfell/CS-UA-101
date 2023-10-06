test_score_1 = 97
test_score_2 = 82
test_score_3 = 85

student_first_name = "Grace"
student_last_name = "Hopper"

bonus_points = 2
class_name = "'Introduction to Computer Programming' (no prior experience)"

print("************************************************************")
print(class_name)
print("************************************************************")
print("")
print("")
print("Student:",student_last_name+",",student_first_name)
print("Most recent test scores:", str(test_score_1)+",",test_score_2,"and",test_score_3)
average=float((test_score_1+test_score_3+test_score_2)/3)
print("Average score:", average)
print("Class bonus points:" , bonus_points)
final=float(average+bonus_points)
print("Average score with bonus points added:", final)



