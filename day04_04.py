# 컬렉션 : 파이썬에서 여러 요소들을 한번에 저장하고 처리할 수 있게 만들어진 데이터 구조 
# # 리스트, 튜플, 딕셔너리
# 집합(Set) : 순서가 없고, 중복된 값을 허용하지 않는 요소의 모음
#중괄호 {}를 사용한다. 단일 데이터만 요소로 가진다.

s = {1,2,3}

print(s)

s.add(4)
print(s)

s.add(3)
print(s)

s.add(-1)
print(s)

lst = [1,2,3,4,5]

s= set(lst)
print(s)

s=set("helllllo") #순서 보장 x
print(s) # s[0] 인덱스 접근x

s.update([1,2,3])
print(s)

# A,B 집합
# A∪B 합집합 : 전체 -A|B
# A∩B 교집합 : 공통된 부분만 - A&B
# A-B 차집합 : 겹치는 부분 제외  A-B
# A△B 대칭차집합 : 합집합- 교집합 A^B

A={1,2,3,4}
B={3,4,5,6}

print(A|B) # 합집합
print(A&B) #교집합
print(A-B) #차집합
print(A^B) #대칭차집합

num = [1,1,1,2,3,4,5,1,2,4,3,1,2,3,4,5]
uni_num =list(set(num))
print(uni_num)

C= {1,3,5}
print(A&B&C) #3
print(A|B) 

#lower() : 소문자 변환
#upper() : 대문자 변환
#title() : 각 단어의 첫글자만 대문자 변환
# caplaize() : 첫 글자만 대문자
# strip() : 앞 뒤 공백 제거
# lsttrip(), rstrip() : 왼쪽 , 오른쪽 공백 제거
# replace(old, new) : old 문자열 new 문자로 변환

print("       hello",strip())
print("Hello World".replace("Hello","Hi"))

#문자열 검증 -> Bool(True,False)
#startswith(prefix) : 문자열이 prefix으로 시작 하는 확인
#endswith(prefix) : 문자열이 prefix으로 끝나는ㅈㅣ 확인
#isalum() : 문자+숫자로만 이루어져 있는지 확인
#isdigit() : 숫자로만 이루어져 있는지 확인
#islower() : 소문자로만 이루어 지는지 확인
#isuper() : 대문자로만 이루어져있는지 확인
print("12345".isalpha())
print("12345".isdigit())

#문자열 찾기 -> 인덱스(위치)
#find(sub) : sub 의 첫번째 위치 없으면 -1
#rfind(sub) : sub 의 마지막 위치 없으면 -1
#index(sub) : sub의 첫번째 위치 없으면 오류
#rindex(sub) : sub의 마지막 위치 없으면 오류
#count(sub) : sub의 개수 변환

#문자열 분할 및 결합
#split(sep) :sep 을 기준으로 나눠서 리스트를 반환
# rsplit(sep) : 오른쪽 기준으로 split

print("a,b,c,d".rsplit(",",2))
print("---- ".join(["a","b","c","d"]))

#문자열 정렬
#center(width) :  가운데 정렬 후 공백 ㅊㅐ우기
#ljust(width) : 왼쪽 정렬 후 공백 채우기
# rjust(width) : 오른쪽 정렬 후 공백 채우기
# zfill(width) : 길이를 맞추고 빈공간을 0으로 채우기
print("hello".center(20))
print("1".zfill(4))