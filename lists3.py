names = ["John", "Paul", "Luke"]
gradelevels = [12, 11, 10]
GPA = [90, 74, 65]

print(f"student records for {names[0]}. Grade level: {gradelevels[0]} GPA: {GPA[0]}")

for i in range(len(names)):
    print(f"student records for {names[i]}. Grade level: {gradelevels[i]} GPA: {GPA[i]}")