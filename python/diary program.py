#diary program
#1.날짜를 입력하고 일기를 작성, 2. 날씨를 입력하고 작성된 일기를 출력
#dd-mm-yyyy.txt

#프로그램을 실행하고, 읽기, 쓰거나, 종료
#1. 쓰기 2. 읽기, 3. 종료

date = input("날짜(DD-MM-YYYY): ")
weather = input("날씨: ")
contents = input("일기 작성: ")


file_name = date + ".txt"
file = open(file_name, 'a', encoding='utf-8') 
file.write("날씨: %s\n내용: %s\n\n" % (weather, contents))  
file.close()  
print("일기가 추가되었습니다.")

def menu():
    choice = int(input("어느 것을 선택하시겠습니까? (1: 일기 쓰기, 2: 일기 불러오기, 3: 다이어리 덮기): "))

    print("1. 일기 쓰기")
    print("2. 일기 불러오기")
    print("3. 다이어리 덮기")

    if choice == 1:
        write_diary()
    elif choice == 2:
        read_diary()
    elif choice == 3:
        return 1

def write_diary():
    date = input("날짜를 입력하세요(dd-mm-yyyy): ")
    text = input("오늘 하루는 어땠나요??\n")
    with open(f"{date}.txt", "w", encoding="utf-8") as file:  # date+".txt"
        file.write(text)
        print("일기 저장이 완료되었습니다.")

def read_diary():
    date = input("보고 싶은 일기의 날짜를 입력하세요(dd-mm-yyyy): ")
    with open(f"{date}.txt", "r",) as file:
            content = file.read()
            print(f"{date}의 일기 내용:\n{content}")




