class Student:
    pass

f = open('students.csv', encoding="utf8")
t = f.readlines()
students = []
for i in t:
    info = Student()
    inp = i.split(',')
    info.Id = inp[0]
    info.Fio = inp[1]
    info.Project_id = inp[2]
    info.Class = inp[3]
    info.Score = inp[4]
    students.append(info)

for j in students:
    if 'Хадаров Владимир' in j.Fio:
        print(f'Ты получил: {j.Score}, за проект - {j.Project_id}')