class Calculator :
    def set(self,x,y):
        self.first=x
        self.second = y
    def add(self):
        result = self.first + self.second
        return result
    
call = Calculator()

call.set(10,20)
print('%d + %d = %d' % (call.first,call.second, call.add()))

call.set(100,200)
print('%d + %d = %d' % (call.first,call.second, call.add()))

cal2 = Calculator()
cal2.set(1,2)

class Member :
    def __init__(self, name, age) :  #__init__ 메서드는 생성자를 의미한다
        self.name = name
        self.age = age
    def showMember(self) :
        print('이름 : %s' % self.name)
        print('나이 : %d' % self.age)
mem1 = Member('홍지수', 24)
mem1.showMember()
mem2 = Member('안지영', 20)
mem2.showMember()

s = "hello"

print(s.upper())

class MyClass :
    def __init__(self, number) :
        self.number = number 
    def inc_10(self):
        self.number += 10
    def inc_20(self):
        self.number += 20
# 인스턴스 속성
obj1 = MyClass(100)
obj1.inc_10()
obj1.inc_20()
print(obj1.number)

obj2 = MyClass(200)
obj2.inc_10()
obj2.inc_20()
print(obj2.number)



class Person:
    def __init__(self, info):
        self.name, self.email, self.phone = info

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPhoneNum(self):
        return self.phone

info = ['김지혜', 'rubato@hanmail.net', '010-1234-4567']
person = Person(info)
print('성명 : %s' % person.getName())
print('이메일 : %s' % person.getEmail())
print('전화번호 : %s' % person.getPhoneNum())




class EngSentence :
    def __init__(self, sentence) :
        self.sentence = ❶__________ ❷__________
= len(self.sentence)
    def reverse(self) :
        tmp = '‘
        for i in range(self.length) :
            tmp += (self.sentence[❸_____________)
    return tmp
def insertHypen(self) :
    tmp = '‘
    for i in range(self.length) :
        if self.sentence[i] == ❹__________ :
            tmp += '-‘
        else :
        tmp += self.sentence[i]
    return tmp
a = 'We are the champions!'
eng1 = EngSentence(a)
print('역순 : %s' % ❺_____________)
print('하이픈(-) 삽입 : %s' % eng1.insertHypen())

class EngSentence:
    def __init__(self, sentence):
        self.sentence = sentence                   # ❶: 문장을 초기화합니다.
        self.length = len(self.sentence)           # ❷: 문장의 길이를 저장합니다.

    def reverse(self):
        tmp = ''                                   # ❸: 빈 문자열로 초기화합니다.
        for i in range(self.length):
            tmp += self.sentence[self.length - i - 1]  # 문자를 역순으로 추가합니다.
        return tmp

    def insertHypen(self):
        tmp = ''                                   # 하이픈을 삽입하기 위한 빈 문자열
        for i in range(self.length):
            if self.sentence[i] == ' ':            # ❹: 공백을 찾습니다.
                tmp += '-'                          # 하이픈 추가
            else:
                tmp += self.sentence[i]           # 문자를 추가
        return tmp
        