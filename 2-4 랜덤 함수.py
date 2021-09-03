#난수 무작위로 숫자를 뽑아줌
from random import *

print(random()) # 0.0~1.0미만의 임의의값 생성
print(random() *10) #0.0~10.0 미만의 임의의 값 생성
print(int(random()* 10)) #0~10 미만의 임의의 값 생성
print(int(random() *10)+1) #1~10 이하의 임의의 값 생성
print(int(random()*45)+1) #1~45 이하의 임의의 값 생성

print(randrange(1, 45)) #1~45미만의 임의의 값 생성 [) 끝구간이 개구간임
print(randint(1, 45)) #1~45이하의 임의의 값 생성 [] 폐구간임