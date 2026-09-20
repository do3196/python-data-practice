values = []

def show_average(data):
    if len(data) == 0:
        print("데이터가 없습니다.")
    else:
        average = sum(data) / len(data)
        print(f"평균: {average:.2f}")

def add_data():
    try:
        number = int(input("숫자를 입력하세요: "))
        values.append(number)
        print("저장되었습니다.")
    except ValueError:
        print("숫자만 입력하세요.")

def show_data():
    print(values)

def show_max_min():
    if len(values) == 0:
        print("데이터가 없습니다.")
    else:
        print(f"최대값: {max(values)}")
        print(f"최소값: {min(values)}")

print("\n========== 메뉴 ==========")  
while True:
    try:
        menu = int(input("1.입력  2.보기  3.평균  4.최소값/최대값  0.종료: "))
    
        if menu == 1:
            add_data()
        elif menu == 2:
            print(values)
        elif menu == 3:
            show_average(values)
        elif menu == 4:
            show_max_min()
        elif menu == 0:
            break
        else:
            print("1, 2, 3, 4, 0 중에서 선택하세요.")
    except ValueError:
        print("숫자만 입력하세요.")
        break

