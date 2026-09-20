while True:
    print("\n===== 메뉴 =====")
    print("1. 데이터 입력")
    print("2. 데이터 보기")
    print("3. 평균")
    print("0. 종료")
 
    menu = input("메뉴 선택: ")

    if menu == "1":
        print("데이터 입력")
    elif menu == "2":
        print("데이터 보기")
    elif menu == "3":
        print("평균 계산")
    elif menu == "0":
        print("종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다.")