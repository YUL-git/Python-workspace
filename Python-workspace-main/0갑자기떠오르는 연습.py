profile1 = input("고객님 이름이 어떻게 되나요? ")
profile2 = input("고객님의 나이가 어떻게 되나요?")
check = input("고객님의 이름: {0} \t나이: {1} 정확하게 맞나요?(예/아니요)".format(profile1,profile2))

if check == "예" :
    print("환영합니다")
else :
    profile1 = input("고객님 이름이 어떻게 되나요? ")
    profile2 = input("고객님의 나이가 어떻게 되나요?")

