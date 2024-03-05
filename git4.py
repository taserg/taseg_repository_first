import random
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
    info.Score = inp[4][:-1]
    info.Login = inp[1].split()[0]+'_'+inp[1].split()[1][0]+inp[1].split()[2][0]
    info.Password = ''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)])
    students.append(info)

fo = open('students_password.csv', 'w')
fo.write('id,Name,titleProject_id,class,score,login,password\n')
for j in students:
    fo.write(f'{j.Id},{j.Fio},{j.Project_id},{j.Class},{j.Score},{j.Login},{j.Password}\n')
fo.close()