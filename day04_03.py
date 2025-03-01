#모듈 : 여러 함수들이 선언되어 있는 하나의 .py 파일
#패키지 : 여러 개의 모듈을 그룹화 한 것 
#copy.py->import deepcopy.copy

#from greet import*   <- *이 해당 모듈 전부를 가지고옴

def hello1(name) :
    x = '%s님 안녕하세요.' % name 
    return x 
def hello2(name) : 
    x = '%s님 반갑습니다.' % name 
    return x 
def hello3(name) : 
    x = '%s님 만나서 반가워요.' % name 
    return x

import greet
import math
print(greet.hello1('김영진'))
print(math.sqrt(100))

import greet as gr
import math as m
print(gr.hello2('박소정'))
print(m.sqrt(100))

from greet import hello3
from math import sqrt
print(hello3('한은정'))
print(sqrt(100))

from greet import *
from math import *
print(hello2('한은정'))
print(sqrt(100), sin(1))

import math as m

import random
for i in range(3) :
    print(random.random()) #<-0.01,,,,~0.99,,

import random
for i in range(3) :
    print(int(random.random()*10))#<-int 하면 일단 0~9
    print(int(random.random()*10)+1) #<-+1하면 1~10 

import random
for i in range(5) :
    print(random.randrange(1, 11, 2))

import random
for i in range(5) :
    print(random.randint(1, 6))

import random
toss = ['가위', '바위', '보']
for i in range(5) :
    print(random.choice(toss)) #<-choice는 리스트 안에 있는 값 뽑는거

import random
fruits = ['사과', '바나나', '오렌지']
for i in range(3) :
    random.shuffle(fruits)
print(fruits)

import pickle

data = {"no" : 1, "title":"제목", "content":"내용"}

print(data)

with open('data.p','wb') as f:
    pickle.dump(data,f)

d = dict()
print(d)

with open('data.p','rb') as f:
    d = pickle.load(f)

print(d)

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

with open("yesterday.txt","r")as f:
    text = f.read()
lst = text.split()
print(lst)
cleaned_lst = []

for word in lst:
    cleaned = ""
    for char in word:
        if not char in punctuations:
            cleaned += char
    cleaned_lst.append (cleaned)
print(cleaned_lst.count("yesterday"))

a = [] #0..9

for i in range(10):
    a.append(i)

print(a)

a = [i for i in range(10)]
#a=[1] : a에 1을 넣겠다
# i 가 뭔데?
#for i in range(10) : 0...9
# a = [0..9]

a = [1**2 for i in range(10)]
print(a)

a = [i for i in range(0,10,2)]
print(a)

a= [1 for i in range(10) if 1%2==0]
#a=[i]를 넣겠다 
# 1이 뭔데? 
# for i in range(10): 0...9 
# 조건 : 1%2==0

a = [i*j for i in range(2,10) for j in range(1,10)]
#a = [i*j]를 넣겠다 
# i가 뭐야? f
# or i in range(2,10):2...9 

print(a)

a=[0,0,0,0,0,0,0,0,0,0]
a=[0] *10
a=[i*0 for i in range(10)]
a=[i-i for i in range(10)]
a=[0 for i in range(10)]
a=[0 for _ in range(10)]

word = ["school","coding","python","data structure","algorithn","java"]
a = []

for w in word:
    if len(w) ==6:
        a.append(w)

print(a)

a = [i for i in word]
a = [i for i in word if len(i) ==6]
print(a)
a = [word[i]for i in range(len(word))if len(word[i])==6]
print(a)


word = ["school", "coding", "python", "student", "data structure", "algorithm", "java"]

a = []
for w in word:
    a.append(len(w))

print(a)

word = ["school", "coding", "python", "student", "data structure", "algorithm", "java"]

a = [len(w) for w in word]

print(a)

number = [i+1 for i in range(10)] # range(1,11)
print(number)
#"홀수, 짝수"
a = ["짝수" if n % 2 == 0 else "홀수" for n in number]
print(a)

#3*3 배열 ( 순서쌍) (0,0),(0,1),...(2,2)

b = [(i, j) for i in range(3) for j in range(3)]
print(b)


#100 이하의 소수로 이루어진 1차원 리스트( 약수가 1과 자기자신)
prime =[2]

for i in range(2,101):
    for j in range(2,1):
        if i%j == 0:
            break # break 는 가장 가까운 반복문에 해당.
        elif j == i-1: #else를 쓰면
            prime.append(i)
print(prime)

#prime = [i for i in range(2,101) if i%j !=0 for j in range(2,i)]
#prime =[1]를 넣을 거야 
#  i 가 뭔데? 2...100 
# 근데i%j==0 이 되면 안돼
# j 가 뭔데? 2...i-1
#근데 순서가 잘못되었다 for -> if


print (prime)
#al고 함수, any 함수
# 여러 개의 조건 아 값이 있는 자료구조 값의 조건에 따라 True or False 반환-> 값들을 True or False
print(prime)

res = all(x%2==0 for x in number)

print(res)

res = all(x<100 for x in number)
print(res)

#prime = [i for i in range(2,101)if all(1%j !=0)for j in range(2,1)]

stars = ["*****"] * 5

print(stars)

stars = []
for _ in range(5):
    stars.append("*****")
print(stars)

for i in range(5):
    temp = ""
    for _ in range(5):
        temp +="*"
    lst.append(temp)

for i in lst:
    print(i)
print()

lst = ["*"*5 for _ in range(5)]
for i in lst:
    print(i)

lst = ["*" for _ in range(5)]
print(lst)

# map 함수 
# 주어진 함수를 반복가능한 객체의 각 원소에 적용하고 결과를 반환한다.

#map(function, iterable) -> 각 요소에 함수를 적용한 결과

def square(x):
    return x*x

lst = [1,2,3,4,5]
sq_lst = map(square, lst)

print(list(sq_lst))

sq_lst = map(lambda x : x*x, lst)
print(list(sq_lst))

a= [1,2,3,4,5,6,7,8,9,10]

for i in range(len(a)):
    if a[i]%2 ==0:
        a[i]=0
print(a)

a= [1,2,3,4,5,6,7,8,9,10]
def func(x):
    if x%2==0:
        return 0
    else:
        return x
print(list(map(func, a)))

a= [1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x :0 if x%2 ==0 else x ,a)))

#filter 함수
# 주어진 함수를 반복 가능한(iterable) 객체의 결과가 참인 요소들만 반환한다.

#filter(function, iterable)

a= [1,2,3,4,5,6,7,8,9,10]

def is_even(x):
    return x%2 ==0

even_list = filter(is_even,a)
print(list(even_list))



a= [1,2,3,4,5,6,7,8,9,10]
odd_list = filter(lambda x: x % 2 != 0, a)

print(list(odd_list)) 

scores =[10,20,30,40,50,60,70,80,90,100,45,87,68,95,91]
#70 점 이상 합격, 50 미만 불합격, 50~69 : 재시험



scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 45, 87, 12, 68, 55, 91]

result = list(map(lambda x: "합격" if x >= 70 else "재시험" if x >= 50 else "불합격", scores))

print(result)

files = ["memo.txt", "1.jpg", "dog-jpg", "cat.jpg", "bird-png", "05-07.txt"]
#.jpg만 필터링 가져오기
files = ["memo.txt", "1.jpg", "dog-jpg", "cat.jpg", "bird-png", "05-07.txt"]

jpg_files = list(filter(lambda file: file.endswith('.jpg'), files))

print(jpg_files)

files = ["memo.txt", "1.jpg", "dog-jpg", "cat.jpg", "bird-png", "05-07.txt"]

jpg_files = [file for file in files if file.endswith('.jpg')]

print(jpg_files)

# 리스트 세 개의 곱
lst1 = [1,2,3,4,5]
lst2=[1,3,5,7,9]
lst3=[2,4,6,8,10]
print(list(map(lambda x,y,z : x*y*z, lst1,lst2,lst3)))
print(list(zip(lst1,lst2,lst3)))
print(list(map(lambda x : x[0]*x[1]*x[2], zip(lst1, lst2,lst3)))) #가장 작은

