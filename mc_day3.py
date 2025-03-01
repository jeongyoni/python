tuple1 = ('apple', 'banana', 'cherry')
tuple2 = ('orange', 'melon', 'strawberry')
tuple3 = tuple1 + tuple2
print(tuple3)
print(len(tuple3))
for x in tuple1 :
    print(x)

members = {'name': 'yun' , 'age':26,'email':'jungyoni@hufs.ac.kr'}
print(members)
print(members['name'])
print(members['age'])

scores = {'김예진': 90, '박영진': 95, '김소희': 84}
sum = 0
for key in scores:
    sum += scores[key]  # ❶
    print('%s : %d' % (key, scores[key]))  # ❷
avg = sum / len(scores)  # ❸
print('합계 : %d, 평균 : %.2f' % (sum, avg))


words = {'사과': 'apple', '컴퓨터': 'computer', '학교': 'school', '책상': 'desk', '의자': 'chair'}

for key in words:
    in_word = input('%s에 해당되는 영어 단어를 입력해주세요: ' % key)  # ❶
    if in_word == words[key]:  # ❷
        print('정답입니다!')
    else:
        print('틀렸습니다!')
