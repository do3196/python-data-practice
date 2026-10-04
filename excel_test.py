from openpyxl import Workbook

# 새로운 Excel 파일 만들기
workbook = Workbook()
# 현재 시트 가져오기
worksheet = workbook.active
# 시트 이름 변경
worksheet.title = "학생점수"

# 첫 번째 행에 제목 저장
worksheet.append(["이름", "점수"])

# 학생 데이터 저장
worksheet.append(["김민수", 80])
worksheet.append(["이영희", 90])
worksheet.append(["박철수", 85])


# Excel 파일 저장
workbook.save("students.xlsx")
print("students.xlsx 파일이 생성되었습니다.")