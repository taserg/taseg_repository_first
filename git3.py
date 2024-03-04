class Student:
    pass

f = open('students.csv', encoding="utf8")
t = f.readlines()
students = []
for i in t[1:]:
    info = Student()
    inp = i.split(',')
    info.Id = inp[0]
    info.Fio = inp[1]
    info.Project_id = int(inp[2])
    info.Class = inp[3]
    info.Score = inp[4]
    students.append(info)

what_index = int(input())
if what_index > 500:
    print('Ничего не найдено.')
else:
    for j in students:
        if j.Project_id == what_index:
            print('Проект №', j.Project_id, 'делал: ', j.Fio, 'он(а) получил(а) оценку - ', j.Score, '.')