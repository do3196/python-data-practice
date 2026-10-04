from datetime import datetime

energy = [[2025, 1, 320], [2025, 2, 300], [2025, 3, 310], [2025, 4, 340],
    [2025, 5, 360], [2025, 6, 390], [2025, 7, 430], [2025, 8, 450],
    [2025, 9, 410], [2025, 10, 380], [2025, 11, 350], [2025, 12, 330],
    [2026, 1, 335], [2026, 2, 315], [2026, 3, 325], [2026, 4, 355],
    [2026, 5, 375], [2026, 6, 405], [2026, 7, 445], [2026, 8, 465],
    [2026, 9, 425], [2026, 10, 395], [2026, 11, 365], [2026, 12, 345]]

# 원하는 연월의 전력 사용량 검색
def search_energy(year, month):
    # 현재 날짜 가져오기
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # energy 데이터 하나씩 확인
    for item in energy:
        # 입력한 연도와 월이 같은 데이터 찾기
        if item[0] == year and item[1] == month:
            value = item[2]
            # 과거 연도
            if year < current_year:
                print(
                    f"{year}년 {month}월 전력 사용량은 "
                    f"{value}kWh입니다."
                )
            # 현재 연도의 현재 월까지
            elif year == current_year and month <= current_month:
                print(
                    f"{year}년 {month}월 전력 사용량은 "
                    f"{value}kWh입니다."
                )
            # 미래
            else:
                print(
                    f"{year}년 {month}월 예상 전력 사용량은 "
                    f"{value}kWh입니다."
                )

            return
    print("해당 연월의 데이터가 없습니다.")

# 프로그램 반복 실행
while True:
    try:
        print("\n==============================")
        print("   전력 사용량 조회 프로그램")
        print("==============================")
        year = int(input("연도를 입력하세요: "))
        month = int(input("월을 입력하세요: "))
        # 월 범위 확인
        if month < 1 or month > 12:
            print("월은 1~12 사이로 입력하세요.")
        else:
            search_energy(year, month)
    except ValueError:
        print("숫자만 입력하세요.")

    # 계속 실행 여부 확인
    answer = input("\n종료하시겠습니까? (y/n): ")

    if answer.lower() == "y":
        print("프로그램을 종료합니다.")
        break