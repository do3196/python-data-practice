from openpyxl import load_workbook

# 기존 Excel 파일 열기
workbook = load_workbook("students.xlsx")

# 학생점수 시트 선택
worksheet = workbook["학생점수"]

# 사용자 입력
name = input("학생 이름을 입력하세요: ")

try:
    score = int(input("점수를 입력하세요: "))
    # Excel 마지막 행에 데이터 추가
    worksheet.append([name, score])
    # 수정한 Excel 파일 저장
    workbook.save("students.xlsx")
    print("학생 정보가 저장되었습니다.")
except ValueError:
    print("점수는 숫자로 입력하세요.")