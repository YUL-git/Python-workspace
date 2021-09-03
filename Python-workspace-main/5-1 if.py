weather = "비"
# if 조건:
#     실행 명령문
if weather == "비" :
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물 필요  없어요.")

''' 처음 if문으로 시작을 해 그리고 조건이 맞으면 바로 빠져나와
하지만 조건이 맞지 않으면 밑의 조건으로 들어가 elif이 맞으면 빠져나오고
맞지 않으면 나머지 모든 경우 else로 들어가 
else가 없다면 위의 조건으로만 판단하겠지만 else를 적음으로써 위의 조건이 아니면 이것을 출력해라는 거지'''

#프로그램을 더 매끄럽게 하기위해 input을 써보자 input()은 사용자의 명령을 받는 함수
weather = input("오늘 날씨는 어때요?") 
#이 문장을 실해하고 나서 커서가 사용자 입력을 기다리고 있어 그리고 사용자가 입력을 하면 그 값은 string(문자형)으로 받아
if weather == "비" or weather == "눈" :  #or라는 걸로 다른 정보를 받아줄 수 있어
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물 필요  없어요.") 

temp = int(input("기온은 어때요?")) #input()은 항상 문자열로 값을 받기때문에 int()로 바꿔줘야해
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10<= temp and temp <30 : # 앞조건과 뒷조건 모두 성립할때
    print("괜찮은 날씨에요")
elif 0<= temp and temp <10 : # 0<= temp <10 and를 안쓰고 이렇게 해도돼
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")


''' if와 while 구문의 공통점은 "조건문"을 활용한다는 것'''