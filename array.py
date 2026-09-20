import random

while True:
    answer = random.randint(1, 100)
    attempts = 0

    print("\n숫자 맞추기 게임을 시작합니다!")

    while True:
        try:
            guess = int(input("1~100 사이의 숫자를 입력하세요: "))
        except ValueError:
            print("숫자만 입력해주세요.")
            continue

        if guess < 1 or guess > 100:
            print("1부터 100 사이의 숫자만 입력해주세요.")
            continue

        attempts += 1

        if guess > answer:
            print("DOWN")
        elif guess < answer:
            print("UP")
        else:
            print(f"정답! {attempts}회 만에 맞혔습니다.")
            break

    again = input("게임을 다시 하시겠습니까? (y/n): ")

    if again.lower() != "y":
        print("게임을 종료합니다.")
        break