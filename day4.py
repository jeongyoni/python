file_path = "/Users/사용자명/Desktop/yesterday.txt"

try:
    with open(file_path, "r") as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print(f"파일 '{file_path}'를 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")

