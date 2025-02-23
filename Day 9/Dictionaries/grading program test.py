student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    if student_scores[name] >= 91:
        student_grades[name] = "Outstanding"
    elif student_scores[name] >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"
