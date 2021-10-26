# Take the following list

students = [{"name": "Steve", "score": 88}, {"name": "Becky", "score": 99}, {"name": "Chad", "score": 76}]

# And print out each of the students' names, scores, and grade they would receive (90-100 A, 80-90 B, etc)
# "Steve got a(n) 88, so this student received a(n) B"

for student in students:
    # {"name": "Steve", "score": 88}
    nm = student["name"]
    sc = student["score"]
    grade = ""
    if sc >= 90:
        grade = "A"
    elif sc >= 80:
        grade = "B"
    elif sc >= 70:
        grade = "C"
    elif sc >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{nm} got a(n) {sc}, so this student received a(n) {grade}")
