# Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.
# 이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.
"""
import random


def isValid(prevNums, newNums):
    if len(newNums) > 3 or len(newNums) < 1:
        print("1개 ~ 3개의 수를 입력할 수 있습니다.")
        return False
    elif int(newNums[0]) - int(prevNums[-1]) != 1:
        print("현재 숫자의 다음 수부터 입력할 수 있습니다.")
        return False
    elif len(newNums) > 1:
        for i in range(len(newNums) - 1):
            numCheck = int(newNums[i]) + 1 == int(newNums[i + 1])
            if not numCheck:
                print("숫자들을 순서대로 입력해주세요")
                return False
    return True


def computer(prevNums):
    if 31 - int(prevNums[-1]) == 2:
        maxLen = 2
    elif 31 - int(prevNums[-1]) == 1:
        maxLen = 1
    else:
        maxLen = 3
    numCount = random.randint(1, maxLen)
    newNums = list()
    for i in range(numCount):
        newNums.append(str(int(prevNums[-1]) + (i + 1)))
    return newNums


print("베스킨 라빈스 31 !!!")
step1 = True
while step1:
    isUserFirst = input("선공 / 후공 선택! (선공 or 후공 입력) : ")
    if isUserFirst in ["선공", "후공"]:
        if isUserFirst == "선공":
            isUserFirst = True
        elif isUserFirst == "후공":
            isUserFirst = False
        step1 = False
        break
    else:
        print("선공 또는 후공을 정확히 입력하세요")

progress = ["0"]
gameOn = True
if isUserFirst:
    while gameOn:
        user = input("숫자를 입력하세요 : ").strip()
        userNums = user.split(" ")
        if isValid(progress, userNums):
            progress = progress + userNums
            computerNums = computer(progress)
            progress = progress + computerNums
            print(
                f" 컴퓨터가 {len(computerNums)}개의 숫자를 말했습니다. 마지막 숫자 : {progress[-1]}")
            if computerNums[-1] == "31":
                print("user win !")
                gameOn = False
                break
            if computerNums[-1] == "30":
                print("you loose ...")
                gameOn = False
                break
        else:
            continue
else:
    while gameOn:
        computerNums = computer(progress)
        progress = progress + computerNums
        print(
            f" 컴퓨터가 {len(computerNums)}개의 숫자를 말했습니다. 마지막 숫자 : {progress[-1]}")
        if computerNums[-1] == "31":
            print("user win !")
            gameOn = False
            break
        if computerNums[-1] == "30":
            print("you loose ...")
            gameOn = False
            break
        while True:
            user = input("숫자를 입력하세요 : ").strip()
            userNums = user.split(" ")
            if isValid(progress, userNums):
                progress = progress + userNums
                break
            else:
                continue
            

# Q2. 다음과 같이 학생들의 시험 답지가 있습니다. 그리고 답안지도 있습니다.
# 함수를 하나 만들어 채점을 하고 학생들의 점수를 출력하고 등수도 함께 출력해주세요.

 # 학생 답
s = ["김갑,3242524215",
     "이을,3242524223",
     "박병,2242554131",
     "최정,4245242315",
     "정무,3242524315"]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]


def grader(solutions, answer):
    grades = list()
    for s in solutions:
        student = s.split(",")[0]
        grade = 0
        answerSheet = s.split(",")[1]
        for i in range(len(answerSheet)):
            if answerSheet[i] == str(answer[i]):
                grade = grade + 10
        grades.append(str(grade) + "," + student)
    grades.sort(reverse=True)
    for i in range(len(grades)):
        print(
            f"학생 : {grades[i].split(',')[1]} 점수 : {grades[i].split(',')[0]} 등수 : {i + 1}등")


grader(s, a)


# Q3숫자 맞추기 게임을 만들어 볼게요. 컴퓨터가 임의의 숫자를 3개 만들고 우리가 그것을 맞춰보겠습니다.

# 😲조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
# 😲조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
# 😲조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.


 def guess_number():
    import random
    computerNums = list()
    while True:
        ranNum = random.randint(0, 100)
        if ranNum in computerNums:
            continue
        else:
            computerNums.append(ranNum)
            if len(computerNums) == 3:
                break
            else:
                continue
    computerNums.sort()
    gameCount = 1
    userInputs = list()
    while True:
        print(f"{gameCount}번째 시도!")
        userInput = int(input("0~100 사이의 숫자 한 개를 입력하세요 : "))
        userInputs.append(userInput)
        if userInput in computerNums:
            print(f"{gameCount}번째 시도에 예측 성공!")
            if computerNums.index(userInput) == 0:
                print(f"{userInput}은 최솟값 입니다.")
            elif computerNums.index(userInput) == 1:
                print(f"{userInput}은 중간값 입니다.")
            else:
                print(f"{userInput}은 최댓값 입니다.")
            print(f"정답 : {computerNums}")
            break
        else:
            gameCount = gameCount + 1
            if gameCount % 5 == 1:
                if userInput < computerNums[0]:
                    print(f"힌트! {userInput}은 최솟값보다 작습니다.")
                elif userInput > computerNums[2]:
                    print(f"힌트! {userInput}은 최댓값보다 큽니다.")
                else:
                    print(
                        f"힌트! {userInput}과 중간값의 차이는 {abs(computerNums[1] - userInput)}입니다.")
                print(f"현재 예측한 숫자 : {userInputs}")
            continue


guess_number()
"""

# Q4 Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.

# 날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.

# 😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
# 😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.


def after_100(month, day, DOW):
    daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    remainingDays = daysInMonth[month] - day
    daysCount = 100 - remainingDays
    while True:
        month = month + 1
        if month > 12:
            month = month % 12
        if daysCount > daysInMonth[month]:
            daysCount = daysCount - daysInMonth[month]
            continue
        else:
            break
    result = [month, daysCount - 1]
    dayOfWeek = ["월", "화", "수", "목", "금", "토", "일"]
    index = dayOfWeek.index(DOW)
    newIndex = 100 % 7 + index - 1
    if newIndex > 7:
        newIndex = newIndex % 7
    result.append(dayOfWeek[newIndex])
    print(result)


after_100(6, 21, "월")
