import random

# 1


def gugudan(number):
    i = 1
    print(f"{number}단 시작!")
    while i < 10:
        result = i * number
        if result <= 50:
            print(f"{number} X {i} = {result}")
        i = i + 2


print(" welcome to 구구단! ")
try:
    number = int(input(" 몇 단인지 알려주세요! 숫자만 입력! : "))
    gugudan(number)
except:
    print("error!")

# 2


def rsp_advanced(games):
    on_game = True
    game_count = 1
    computer_win = 0
    user_win = 0
    draw = 0
    while on_game:
        user = input("가위(0) 바위(1) 보(2) 입력! : ")
        option = ["가위", "바위", "보"]
        if user == "가위" or user == "0":
            user = 0
        elif user == "바위" or user == "1":
            user = 1
        elif user == "보" or user == "2":
            user = 2
        else:
            print("가위, 바위, 보 또는 0, 1, 2를 정확히 입력해주세요")
            continue
        computer = random.randint(0, 2)
        print(f"나 : {option[user]}")
        print(f"컴퓨터 : {option[computer]}")
        if computer == user:
            draw = draw + 1
            print(f"{game_count} 번째 판 무승부!")
        elif computer - user == 1 or computer - user == -2:
            computer_win = computer_win + 1
            print(f"{game_count} 번째 판 컴퓨터 승리!")
        else:
            user_win = user_win + 1
            print(f"{game_count} 번째 판 유저 승리!")
        game_count = game_count + 1
        if games < game_count:
            print("게임이 모두 끝났습니다!")
            print(f"나의 전적 {user_win}승 {draw}무 {computer_win}패")
            on_game = False
            break


try:
    games = int(input("가위 바위 보 몇판을 할까요? (숫자만 입력) : "))
    rsp_advanced(games)
except:
    print("error!")


# 3

def find_even_number(n, m):
    median = (n + m) / 2
    if median % 2 == 0:
        median_exist = True
    else:
        median_exist = False
    numbers = [i for i in range(n, m+1) if i % 2 == 0]
    if median_exist:
        for number in numbers:
            if number == median:
                print(number, "짝수")
                print(number, "중앙값")
            else:
                print(number, "짝수")
    else:
        for number in numbers:
            print(number, "짝수")


try:
    n = int(input("첫번째 숫자를 입력해주세요! : "))
    m = int(input("마지막 숫자를 입력해주세요! : "))
    find_even_number(n, m)
except:
    print("error!")


# 4


def count_prime_number(n, m):
    a = 0
    for i in range(n+1, m+1):
        b = 0
        for j in range(2, i):
            if i % j == 0:
                b = 1
        if b == 0:
            a = a+1
    print("소수개수", a)


try:
    n = int(input("첫 숫자를 입력하세요 : "))
    m = int(input("마지막 숫자를 입력하세요 : "))
    count_prime_number(n, m)
except:
    print("error!")
