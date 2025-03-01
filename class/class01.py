print('"hello"')

# ctrl + shift + p -> Python interpreter -> 3.13.2 클릭

# 컴퓨터는 바보다.
# 1, 0 (이진법) -> 덧셈
# 연산속도가 엄청 빠르다.

# 최초의 컴퓨터 (애니악) -> 전구 켜지면(1), 꺼지면(0)

# ABCD, ㄱㄴㄷㄹ - 아스키 코드(ASCII CODE) -> a : 97, b : 98, ..., A : 76

# 컴파일러(번역기) -> 컴파일(번역)
# 기계어 <- 어셈블리어 <- 고급언어(Python) <- 언어

# (#) : 주석 (컴퓨터는 읽지 못하고 사람만 읽을 수 있는 메모) (단축키 : crtl + /)

# 변수(변하는 수) - 데이터 저장의 최소 단위

a = 20
b = 30
c = a + b # 50

print(c)

# 대입 연산자 (=) : 우항(등호 오른쪽)의 "값"을 좌항(등호 왼쪽)에 대입한다.
# 20 = a (X)

A = 10

# 숫자(Number)
# 정수(Integer) - 양의 정수, 0, 음의 정수 (-123, -5, 0, 1, 234)
# int(4byte), long, short, byte ... 메모리 크기가 다르다.
# 실수(Floating Number) - 유리수, 무리수 (123.456, -123.456)
# double, float ...
# long long double

# 문자(char) - 'a', '가' 
# 문자열(String) - 'abcdef', 'ㄱㄴㄷㄹ' 

# boolean - True(1) or False(0)
# void - 비어있음.

print(type(A))

x = 3.3764
y = 6/2 # 자동 형변환 (정수 -> 실수)
print(x, y)
print(type(x), type(y))

print(A + x) # 정수 + 실수 -> 실수 + 실수 -> 10.0 + 3.3764

z = "''''#$%^"

print(10%3)
print(7//3)
print(2**3)

print(A)

A = A + 2 # A의 값을 2만큼 증가시키겠다.
# +=, -=
A += 2 # A = A + 2
A -= 2 # A = A - 2
A *= 2 # A = A * 2
A /= 2 # A = A / 2
A //= 2 # A = A // 2

x = 20
y = 4

x = y % x
print("1.", x)

y -= x * 2

print("2.", x, ", 3.", y)
#print("2." + x + ", 3." + y)

eng = 80
result = 'English : ' + str(eng) + ' scores'
print(result)

eng_str = str(eng)

print(type(eng), type(eng_str))

math = '90'

math_int = int(math)
print(type(math), type(math_int))

age = 20
a = "I'm %d years old." % age # decimal, %f (float)
print(a)

print("I'm %s years old." % age)

name = 'Hong'
age = 30
height = 173.7
print(name,age, "            ", height)

year = 2020
month = 3
day = 5

print(year, month, day, sep=' ') # 기본값 sep = ' '
print(year, month, day, sep='abc')

# \n (new line) : 줄 바꾸기
# \t : 탭tab
# \v : 수직tab

a = 'Hello.'
b = 'Hi.'
print(a) # print('Hello\n')
print(b) 
print(b, end='\n') # 기본값 end='\n'
print('\n\n') 
print(a, end=' Nice to meet you.\n')
print(b)

print("'\"\"'")

name = input("Name : ")
print('Hi', name)

a = int(input("A : "))
b = int(input("B : "))

print(a + b)

width = 10
height = 3
area = width * height / 2

print('width : ', width)
print('height : ', height)
print('area : %.1f' % area)

name = "Hongil" # 홍길동
age = 30
height = 171.5

print("First : ", name[0])
print("Last : ", name[4:5]) # [1:2] = [1]
print("name : %s, age : %d, height : %.2fcm" % (name, age, height))
