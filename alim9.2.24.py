class Student:
    pass
def sort_by_score(students):
    for k in range(1, len(students)):
        temp = students[k]
        j = k - 1
        while (j >= 0 and int(temp.Score) < int(students[j].Score)):
            students[j + 1] = students[j]
            j = j - 1
        students[j + 1] = temp

f = open('students.csv')
f.readline()
students = []
for i in f:
    info = Student()
    inp = i.split(',')
    info.Id = int(inp[0])
    info.Fio = inp[1]
    info.Project_id = int(inp[2])
    info.Class = inp[3]
    info.Score = inp[::-1][4]
    students.append(info)

sort_by_score(students)
for j in students:
    if '10' in j.Class:
        print(students.index(j), j.Fio, j.Class, j.Score)