# 2. 로또 번호 생성기 1 ~ 45, 7개 **중복되지 않는 리스트

# 로또 번호 생성기
import random
lotto_numbers = random.sample(range(1, 46), 7)

print("행운의 로또 번호:", lotto_numbers)

import random
numbers = []

for _ in range(7):
    num = random.randint(1,45)

# 3. 공통된 음식 찾기 (컴프리헨션)
# 각각의 음식 리스트 정의
person1 = ["치킨", "피자", "햄버거"]
person2 = ["족발", "삼겹살", "치킨"]
person3 = ["피자", "김밥", "떡볶이", "치킨"]


people = [person1, person2, person3]
common_foods = [food for food in person1 
                if all(food in person for person in people)]

if common_foods:
    print(f"공통된 음식: {common_foods}")
#else:
    #print("공통된 음식이 없습니다.")


