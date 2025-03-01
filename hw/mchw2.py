#1.1
for i in range(1, 6):
    print('*' * i)
#1.2
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)
#1.3
for i in range(5, 0, -1):
    print('*' * i)
#1.4
for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * i)
#1.5
for i in range(1, 10, 2):
    print(' ' * ((9 - i) // 2) + '*' * i)

#2
menu = ["커피", "우유", "녹차", "떡볶이", "순대", "김밥", "짜장면", "커피"]

reversed_menu = menu[::-1]
print(reversed_menu)

#2
menu = ["커피", "우유", "녹차", "떡볶이", "순대", "김밥", "짜장면", "커피"]

for i in range(len(menu) - 1, -1, -1):
    print(menu[i])

# 3. 5 X 5 배열 만들어서 1~25까지 채우기
matrix = []

rows, cols = 5, 5
num = 1

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(num)
        num += 1
    matrix.append(row)

print(matrix)

