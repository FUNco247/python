Q1 = "파이썬으로 할수 있는 일은 어떤 것들이 있고, 나는 그중에서 무엇을 하고싶은지 적어봅시다."

A1_FuNco = "웹 서버 개발과 데이터 분석에 쓰고싶습니다."




Q2 = "하드웨어 아키텍쳐에서 CPU와 Main Memory, Secondary Memory의 역할을 간단하게 정리하여 봅시다."

A2_FuNco = "CPU는 연산과 명령 실행을 담당하는 장치입니다, 이 명령들은 Main Memory에 저장되어있습니다. Main Memory에 저장된 정보는 상대적으로 적은 양이고 휘발성이지만 매우 빠르게 작동합니다. 비 휘발성 정보는 Secondary Memory에 저장됩니다. "

Q3 = " syntax error, value error, type error 에러 발생 코드를 2가지씩 만들고 디버깅합니다. 그 외 에러도 3가지를 찾아 디버깅한 코드를 1가지씩 만들어 봅시다."

A3_FUNco = {"syntax": [{"error": "", "debug": ""}, {"error": "", "debug": ""}], "value": [{"error": "", "debug": ""}, {
    "error": "", "debug": ""}], "type": [{"error": "", "debug": ""}, {"error": "", "debug": ""}]}

Q4 = "한국나이를 미국나이로 변환하는 프로그램을 만들어봅니다."

print("이 프로그램은 한국 나이를 미국 나이로 변환합니다!")
kAge = input("한국 나이를 입력해주세요 : ")
while True:
    birthDayPassed = input("생일이 지났습니까?? 맞으면 y 아니면 n 를 입력해주세요 : ")
    if birthDayPassed == "y":
        print(f"당신의 미국 나이는 {int(kAge) - 1}살 입니다.")
        break
    elif birthDayPassed == "n":
        print(f"당신의 미국 나이는 {int(kAge) - 2}살 입니다.")
        break
    else:
        print(" >>> [알림] y 또는 n을 입력해주세요. <<< ")
