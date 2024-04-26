N = int(input())
schools = {}
for _ in range(N-1):
    informationAboutStudent = list(map(str, input().split()))
    schoolNumber = informationAboutStudent[-2]
    score = int(informationAboutStudent[-1])
    if schoolNumber not in schools:
        schools[schoolNumber] = [1, score]
        print('True')
    else:
        if score > schools[schoolNumber][1]:
            schools[schoolNumber][1] = score
            schools[schoolNumber][0] = 1
        elif score == schools[schoolNumber][1]:
            schools[schoolNumber][0] += 1
maxCount = 0
maxSchoolNumber = ''
maxScore = 0
for j in schools:
    score = schools[j][1]
    count = schools[j][0]
    if score > maxScore:
        maxScore = score
        maxCount = count
        maxSchoolNumber = j
    elif score == maxScore and maxCount < count:
        maxCount = count
        maxSchoolNumber = j
print("номер школы:",maxSchoolNumber,"максимум:",maxScore,"количество",maxCount)