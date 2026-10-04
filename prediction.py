from datetime import datetime

sales = [[2025, 1, 120], [2025, 2, 125], [2025, 3, 130], [2025, 4, 128],
    [2025, 5, 140], [2025, 6, 145], [2025, 7, 150], [2025, 8, 155],
    [2025, 9, 160], [2025, 10, 168], [2025, 11, 175], [2025, 12, 180],
    [2026, 1, 185], [2026, 2, 190], [2026, 3, 195], [2026, 4, 200],
    [2026, 5, 205], [2026, 6, 210], [2026, 7, 215], [2026, 8, 220],
    [2026, 9, 225], [2026, 10, 230], [2026, 11, 235], [2026, 12, 240]]

def search_period(start_year, start_month, end_year, end_month):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    result = []

    for item in sales:
        year = item[0]
        month = item[1]
        value = item[2]
        # 시작 연월 이상이고 종료 연월 이하인지 확인
        if (year, month) >= (start_year, start_month) and \
           (year, month) <= (end_year, end_month):
            result.append(item)

    # 데이터가 없는 경우
    if len(result) == 0:
        print("조회된 데이터가 없습니다.")
        return

    print("\n[조회 결과]")

    for item in result:
        year = item[0]
        month = item[1]
        value = item[2]
        if (year, month) <= (current_year, current_month):
            text = "매출"
        else:
            text = "예상 매출"

        print(
            f"{year}년 {month}월 "
            f"{text} : {value}"
        )

    # 매출값만 별도로 저장
    values = []
    for item in result:
        values.append(item[2])

    # 평균 계산
    average = sum(values) / len(values)
    # 최고 매출 찾기
    max_value = max(values)
    # 최고 매출이 발생한 연월 찾기
    max_year = 0
    max_month = 0

    for item in result:
        if item[2] == max_value:
            max_year = item[0]
            max_month = item[1]
            break

    print("\n[분석 결과]")
    print(f"조회된 데이터 개수 : {len(result)}")
    print(f"평균 매출 : {average:.2f}")
    print(f"최고 매출 : {max_value}")
    print(
        f"최고 매출 발생 시점 : "
        f"{max_year}년 {max_month}월"
    )

while True:
    try:
        print("\n==============================")
        print("      기간별 매출 분석")
        print("==============================")
        start_year = int(input("시작 연도: "))
        start_month = int(input("시작 월: "))
        end_year = int(input("종료 연도: "))
        end_month = int(input("종료 월: "))

        # 월 범위 검사
        if start_month < 1 or start_month > 12:
            print("시작 월은 1~12 사이로 입력하세요.")
            continue

        if end_month < 1 or end_month > 12:
            print("종료 월은 1~12 사이로 입력하세요.")
            continue

        # 시작 연월과 종료 연월 비교
        if (start_year, start_month) > (end_year, end_month):
            print("시작 연월이 종료 연월보다 뒤에 있습니다.")
            continue

        search_period(
            start_year,
            start_month,
            end_year,
            end_month
        )

    except ValueError:
        print("숫자만 입력하세요.")

    answer = input("\n종료하시겠습니까? (y/n): ")

    if answer.lower() == "y":
        print("프로그램을 종료합니다.")
        break