# Q1 가위바위보 게임 만들기

import random


def rsp(user: int or str) -> str or None:
    if type(user) != type(1) and type(user) != type("text"):
        return print("입력값이 유효하지 않습니다.")
    option = ["가위", "바위", "보"]
    if user == "가위" or user == 0:
        user = 0
    elif user == "바위" or user == 1:
        user = 1
    elif user == "보" or user == 2:
        user = 2
    else:
        return print("가위, 바위, 보 또는 0, 1, 2를 정확히 입력해주세요")
    computer = random.randint(0, 2)
    print(f"나 : {option[user]}")
    print(f"컴퓨터 : {option[computer]}")
    if computer == user:
        print("무승부!")
    elif computer - user == 1 or computer - user == -2:
        print("컴퓨터 승리!")
    else:
        print("유저 승리!")


rsp(1)
rsp(2)
rsp(0)
rsp("가위")
rsp("바위")
rsp("보")
rsp("23wdfsfsa")
rsp(4)
rsp(True)


# Q2 연봉계산기

def yearSalCal(monthSal: int) -> str or None:
    if type(monthSal) != type(1):
        return print("입력값이 유효하지 않습니다.")
    yearSal = 12 * int(monthSal)
    if yearSal <= 1200:
        taxRate = 0.06
    elif yearSal <= 4600:
        taxRate = 0.15
    elif yearSal <= 8800:
        taxRate = 0.24
    elif yearSal <= 15000:
        taxRate = 0.35
    elif yearSal <= 30000:
        taxRate = 0.38
    elif yearSal <= 50000:
        taxRate = 0.4
    else:
        taxRate = 0.42
    print(f"세전 연봉 : {yearSal} 만원")
    print(f"세후 연봉 : {int(yearSal * (1 - taxRate))} 만원")


yearSalCal(300)
yearSalCal(700)
yearSalCal("sdfsd")

# Q3 학점 출력기


def getGrade(name: str, score: int) -> str or None:
    if type(name) != type("text") or type(score) != type(1):
        return print("입력값이 유효하지 않습니다.")
    if score < 60:
        grade = "F"
    elif score < 65:
        grade = "D"
    elif score < 70:
        grade = "D+"
    elif score < 75:
        grade = "C"
    elif score < 80:
        grade = "C+"
    elif score < 85:
        grade = "B"
    elif score < 90:
        grade = "B+"
    elif score < 95:
        grade = "A"
    elif score <= 100:
        grade = "A+"
    else:
        return print("점수가 유효하지 않습니다.")
    print(f"학생이름 : {name}")
    print(f"점수 : {score}점")
    print(f"학점 : {grade}")


getGrade("FUNco", 100)
getGrade("FUNco", "100")
getGrade(100, 100)
getGrade("FUNco", 150)

# Q4 버스요금 출력기


def busFare(age: int, method: str) -> str or None:
    if type(age) != type(1) or type(method) != type("text"):
        return print("입력값이 유효하지 않습니다.")
    caseCard = [450, 720, 1200]
    caseCash = [450, 1000, 1300]
    if method == "카드":
        fareList = caseCard
    elif method == "현금":
        fareList = caseCash
    else:
        return print("지불 방법은 현금 또는 카드 입니다.")
    if age < 8:
        fare = 0
    elif age < 14:
        fare = fareList[0]
    elif age < 20:
        fare = fareList[1]
    elif age < 75:
        fare = fareList[2]
    else:
        fare = 0
    print(f"나이 : {age}세")
    print(f"지불유형 : {method}")
    print(f"버스요금 : {fare}")


busFare(5, "현금")
busFare(8, "현금")
busFare(14, "현금")
busFare(20, "현금")
busFare(80, "현금")
busFare(5, "카드")
busFare(8, "카드")
busFare(14, "카드")
busFare(20, "카드")
busFare(80, "카드")
busFare("80", "카드")
busFare(80, "커두")
