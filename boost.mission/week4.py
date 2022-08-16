# Q1 3자리마다 콤마 찍어주는 함수 만들기

def make_comma(number):
    minus = False
    number = str(number)
    if number.startswith("-"):
        minus = True
        number = number.replace("-", "")
        newNumber = ""
        commaCount = len(number) // 3
        if commaCount > 0:
            leftOfComma = len(number) % 3
            newNumber = newNumber + number[0:leftOfComma]
            number = number[leftOfComma:len(number)]
            index = 0
            while index < len(number):
                if index % 3 == 0 and len(newNumber) > 0:
                    newNumber = newNumber + "," + number[index]
                else:
                    newNumber = newNumber + number[index]
                index = index + 1
        else:
            newNumber = number
        if minus:
            return print("-" + newNumber)
        else:
            return print(newNumber)


make_comma(123)
make_comma(1234)
make_comma(12341234)
make_comma(123412341234)
make_comma(-123)
make_comma(-1234)
make_comma(-12341234)
make_comma(-123412341234)

# Q2. 문자열 안에 특정 문자 개수 구하기 & txt file 생성하기


def count_word(stringOrigin, stringIndex):
    count = stringOrigin.count(stringIndex)
    newFile = open("새파일.txt", "w")
    newFile.write(stringOrigin)
    newFile.close()
    return print(count)


count_word("안녕하세요 네모 4팀입니다. 우리 팀 화이팅", "팀")


# Q3 방명록 잘못 쓴 사람 찾기
guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""


def wrong_guest_book(list):
    newFile2 = open("방명록.txt", "w")
    newFile2.write(list)
    newFile2.close()
    guestList = list.split("\n")
    for line in guestList:
        name = line.split(",")[0]
        number = line.split(",")[1]
        check010 = number.startswith("010")
        checkLength = len(number)
        checkDash = len(number.split("-"))
        if not check010 or checkLength != 13 or checkDash != 3:
            print(f"잘못 쓴 사람 : {name}\n잘못 쓴 번호 : {number}")


wrong_guest_book(guest_book)

# Q4 주민등록번호로 몇년 몇월생인지 남자인지 여자인지 출력하고 주민등록번호 초건이 만족하지 않으면 "잘못된 번호입니다" 출력


def check_id(id):
    idFront = id.split("-")[0]
    idRear = id.split("-")[1]
    year = idFront[0:2]
    month = idFront[2:4]
    gender = ""
    checkAfter2000 = input("2000년 이후 출생자입니까? 맞으면 o 아니면 x : ")
    if checkAfter2000 == "o" and idRear.startswith("3"):
        male = "남자"
    elif checkAfter2000 == "o" and idRear.startswith("4"):
        male = "여자"
    elif checkAfter2000 == "x" and idRear.startswith("1"):
        male = "남자"
    elif checkAfter2000 == "x" and idRear.startswith("2"):
        male = "여자"
    else:
        return print("잘못된 번호입니다\n올바른 번호를 넣어주세요")
    print(f"{year}년{month}월{gender}")


check_id("500629-2222222")
check_id("000629-2222222")
check_id("000629-4222222")
check_id("000629-3222222")
check_id("500629-3222222")
check_id("500629-4222222")
