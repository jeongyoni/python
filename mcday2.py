'''
for x in range(5):
    print(x,'안녕하세요.')

x=0
while x<5:
    print(x,'hello')
    x+=1

sum=0

for i in range(1,11):
    sum+=i
    print('i의 값 : %d, 합계: %d'%(i,sum))

sum=0
i = 0
while i<10:
    sum +=i
    i +=1
    print('i의 값 : %d, 합계: %d'%(i,sum))

for i in range(10):
    print(i, end=' ')
print()

i=20
while i>0:
    print(i)
    i -= 2
print()


n1 = int(input('n1을 입력하세요: '))
n2 = int(input('n2을 입력하세요: '))


for i in range(n1, n2+1):
    if i % 5 != 0:  
        print('%d' % i, end=' ')
        sum += i 

print('\n' + '-' * 50)
print('n1~n2에서 5의 배수가 아닌 수들의 합계 : %d' % sum)

word = input('영어 문장을 입력하세요 :')

for x in word:
    print(x)

print('-'*50)

for a in range(2,10):
    for b in range(1,10):
        c=a*b
        print('%d x %d=%d'%(a,b,c))

    print('-'*50)


i = 10
while i > 0:
    print(i)
    i -= 1
print('발사')


i = 10
while i > 0:
    print(i)
    if i == 1:
        print('발사')
    i -= 1



num = int(input("단을 선택하세요 (1~9): "))

if num < 1 or num > 9:
    print("잘못된 입력입니다. 1에서 9 사이의 숫자를 입력하세요.")
else:
    if num % 2 == 1:
        print(f"홀수단 {num}단:")
    else:
        print(f"짝수단 {num}단:")
    

    for a in range(1, 10):
        print(f"{num} x {a} = {num * a}")


num = int(input("단을 선택하세요 (1: 홀수단, 2: 짝수단): "))

if num == 1:
    print("홀수단:")
    for i in range(1, 10, 2):  
        print(f"{i}단 : ")
        for j in range(1, 9):
            print(f"{i} x {j}= {i * j}")
        print() 
elif num == 2:
    print("짝수단:")
    for i in range(2, 10, 2):  
        print(f"{i}단 :")
        for j in range(1, 9):
            print(f"{i} x {j} = {i * j}")
        print()  


fruits = ['apple', 'orange', 'banana']
for fruit in fruits:
    for letter in fruit:
        print(letter)

fruits = ['apple', 'orange', 'banana']
for fruit in fruits:
    for i in range(len(fruit)):
        print(fruit[i])
'''
scores = [88,75,90,77,69,80,92]

sum = 0
for score in scores:
    sum+=score
avg=sum/len(scores)

numbers = list(range(1, 101))
print(numbers)




menu = ["커피", "우유", "녹차", "떡볶이", "순대", "김밥", "짜장면"]

choice = input("원하는 메뉴를 입력하세요: ")
count=0
for item in menu:
    if item == choice:
        count += 1

if count>0:
    print(choice + "는 메뉴에 있습니다.")
else:
    print(choice + "는 메뉴에 없습니다.")


s = [3, 5, 6, 2, 272, 111, 67]

# 최소값과 최대값 출력
minimum_value = min(s)
maximum_value = max(s)

print("최소값:", minimum_value)
print("최대값:", maximum_value)
min_index = s.index(min(s))
print(min_index)
s = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]




print(min,max)

s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87, 87, 36, 82, 98, 84, 76, 63, 69, 53, 22]
min = s[0]
max = s[0]


for num in s:
    
    if num < min:
        min = num
   
    if num > max:
        max = num

print(min, max)
# 예시 좌석 배열
seats = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
]

# 좌석 상태 출력
print("좌석 상태:")
for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j] == 0:
            print("%3s" % '[ ]', end="")  # 예약 가능
        else:
            print("%3s" % '[X]', end="")  # 예약 불가
    print()  # 줄 바꿈

print("예약 가능: [ ], 예약 불가: [X]")

