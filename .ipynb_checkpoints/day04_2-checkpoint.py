# 파일 열기
file = open("yesterday.txt", "r")
# 파일 내용 읽기
content = file.read()

# 파일 닫기
file.close()

# "yesterday"의 등장 횟수 세기
count = content.lower().count('yesterday')

# 결과 출력
print(f"'yesterday'는 총 {count}번 나옵니다.")
