# 1. 사용자로부터 숫자 및 연산자 입력받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 2. 연산자에 따른 조건문 처리 및 계산
if operator == "+":
    result = num1 + num2
    print(f"결과: {num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"결과: {num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"결과: {num1} * {num2} = {result}")
elif operator == "/":
    # 0으로 나누는 경우 예외 처리
    if num2 != 0:
        result = num1 / num2
        print(f"결과: {num1} / {num2} = {result:.2f}")
    else:
        print("오류: 0으로 나눌 수 없습니다.")
else:
    print("잘못된 연산자입니다. +, -, *, / 중 하나를 입력해주세요.")