#while문은 맞는 조건이 나올때까지 계속 실행하는 거야 
# 스타벅스에서 손님을 5번 불렀는데 오지않으면 커피를 버리는 정책을 해보자
customer = "토르"
index = 5
#while(조건) : #조건이 만족할때까지 실행하라는 거야 이게 전부 실행되고 나면 while문을 빠져나오는거야
while index>= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index-= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

#손님이 나올때까지 부른다고 해보자
# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index)) #이러면 무한루프에 빠졌어
#     index += 1

#종업원이 손님을 계속 부르긴하지만 손님이 커피가 준비되었나요? 이름을 물어보고 준비되면 주고 아니면 준비하게끔
customer = "토르"
person = "unkown"

while person != customer :
    print("{0},커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?") #input으로 사용자에게 물어볼 수 있어
