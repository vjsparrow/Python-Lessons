# Udemy Exercise
# Student Grades

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
  if student_scores[i]<=70:
    student_grades[i]="Fail"
  elif student_scores[i]<80:
    student_grades[i]="Acceptable"
  elif student_scores[i]<90:
    student_grades[i]="Exceeds Expectations"
  else:
    student_grades[i]="Outstanding"



# 🚨 Don't change the code below 👇
print(student_grades)
