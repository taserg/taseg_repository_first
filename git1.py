class Student:
    pass

f = open('students.csv', encoding="utf8")
t = f.readlines()
students = []
j=0
for i in t:
    info = Student()
    inp = i.split(',')
    info.Id = inp[0]
    info.Fio = inp[1]
    info.Project_id = inp[2]
    info.Class = inp[3]
    info.Score = inp[4][:-1]
    students.append(info)
    j+=1


for ip in students:
    s = 0
    k = 0
    if ip.Score == 'None':
        for j in students:
            if j.Class == ip.Class and j.Score!='None':
                k += 1
                s += int(j.Score)
        ip.Score = f'{s/k:.3f}'
fo = open('students_new.csv','w')
for jk in students:
    fo.write(f'{jk.Id},{jk.Fio},{jk.Project_id},{jk.Class},{jk.Score}\n')
fo.close()

for ji in students:
    if 'Хадаров Владимир' in ji.Fio:
        print(f'Ты получил: {ji.Score}, за проект - {ji.Project_id}')