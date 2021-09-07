# 백화점에서 신용정보를 받는다고 생각해보자
# 고객의 이름과 나이를 물어보고 맞으면 환영합니다 하고 스크린 도어가 열리지만
# 아닐 경우 계속해서 개인정보를 물어본다

profile1 = input("고객님 이름이 어떻게 되나요? ")
profile2 = input("고객님의 나이가 어떻게 되나요?")
check = input("고객님의 이름: {0} \t나이: {1} 정확하게 맞나요?(예/아니요)".format(profile1,profile2))
while True :
    if check == "예" :
        print("환영합니다")
        break
    else :
        profile1 = input("고객님 이름이 어떻게 되나요? ")
        profile2 = input("고객님의 나이가 어떻게 되나요?")
        check = input("고객님의 이름: {0} \t나이: {1} 정확하게 맞나요?(예/아니요)".format(profile1,profile2))
        continue
