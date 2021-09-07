# 지역변수 = 함수내에서만 쓸 수 있는 것
# 전역변수 = 프로그램내에서 어디서든지 불러올 수있는 변수
gun = 10

def checkpoint(soldiers): # 경계근무자 수
    global gun            # 전역변수인 gun을 사용하고 싶으면 "global 변수명"을 해줘야해, 지역변수와 전역변수가 달라
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총: {}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

#가급적 함수의 전달값과 반환값으로 하는 방법
def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers  # 여기서 gun은 지역변수지 
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총: {}".format(gun))
gun = checkpoint_ret(gun, 2)
