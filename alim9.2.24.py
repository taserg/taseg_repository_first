class Student:
    pass

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
    info.score = inp[::-1][4]
    students.append(info)
    print(inp)