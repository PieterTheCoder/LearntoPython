# fruits = {
# "Orange": "A fruit, the color is green, yellow, and orange itself. It can be sweet or sour.",
# "Apple": "A fruit, the color is red and green. Its taste sweet or sour."
# }
# # print(fruits)
# # fruits["Apple"] = "A fruit."
# # print(fruits)
# for fruit in fruits:
#     print(fruit)
#     print(fruits[fruit])
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
