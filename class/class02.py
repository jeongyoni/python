"""
x = int(input('숫자를 입력하세요 : '))

# 들여쓰기
if x > 0 :
    print('양수!')
else :
    x *= -1
    print('0 또는 음수!')

print(x)

and
    T   F
T   T   F
F   F   F

or
    T   F
T   T   T   
F   T   F  
"""

print(5 < 6) # True
print(not 5 == 7) # not False -> True

b = 5
# b가 1보다 크고 10보다 작은지?
print(1 < b and b < 10)

if b > 1 and b < 10 :
    print(True)
else :
    print(False)

# if 1 < b < 10:

print(1 < b < 10) # 체이닝(Chaining)

a = -1
# a, b 둘 중 하나라도 음수가 맞는지?
print(a < 0 or b < 0)

# if elif else 순서
# elif, else : 처음에 나올 수 없다. 항상 if문 뒤에 와야한다.
# elif : else 뒤에 나올 수 없다.

score = int(input('점수를 입력하세요 : '))

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'

print('성적 : %d점' % score)
print('등급 : %s' % grade)


# if문으로 배수 판별기 만들기
# 1. 4의 배수이고, 5의 배수이다.
# 2. 4의 배수다.
# 3. 5의 배수다.
# 4. 4의 배수도, 5의 배수도 아니다.

num = int(input("숫자를 입력하세요 : "))

if num % 4 == 0 and num % 5 == 0:
    print("4의 배수이고, 5의 배수이다.")
elif num % 4 == 0 :
    print("4의 배수다.")
elif num % 5 == 0 :
    print("5의 배수다.")
else :
    print("4의 배수도, 5의 배수도 아니다.")

# 중첩 조건문
now_year = int(input('현재년을 입력해주세요 : '))
now_month = int(input('현재월을 입력해주세요 : '))
now_day = int(input('현재일을 입력해주세요 : '))

birth_year = int(input('출생년을 입력해주세요 : '))
birth_month = int(input('출생월을 입력해주세요 : '))
birth_day = int(input('출생일을 입력해주세요 : '))

if now_month > birth_month:
    age = now_year - birth_year
    print('생일이 지났습니다.')
elif now_month == birth_month:
    if now_day >= birth_day:
        age = now_year - birth_year
        print("생일이 지났습니다.")
    else:
        age = now_year - birth_year - 1
        print("생일이 지나지 않았습니다.")
else :
    age = now_year - birth_year - 1
    print("생일이 지나지 않았습니다.")
    
print('현재 나이 :', age)

# 로그인 (1. 사용자 ID확인, 2. 비밀번호 확인)
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("로그인 성공")
elif username == "admin":
    print("비밀번호가 틀렸습니다.")
else :
    print("존재하지 않는 사용자입니다.")

if username == "admin":
    if password == "1234":
        print("로그인 성공")
    else :
        print("비밀번호가 틀렸습니다.")
else :
    print("존재하지 않는 사용자입니다.")

# 1. 키오스크 만들기
# 메뉴를 선택해주세요 (메뉴1 -> 가격, 메뉴2 -> 가격, 메뉴3 -> 가격 ) : (입력)
# 금액을 넣어주세요 : (입력)
# 잔액이 부족합니다. or (메뉴)가 나왔습니다. 거스름돈 ??원이 나왔습니다.

# 2. a = 10, b = 20, c = 30 -> 조건문을 사용하여 'c가 가장 크다.'라고 출력하기 (3가지 방법)