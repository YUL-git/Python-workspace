#난수 무작위로 숫자를 뽑아줌
from random import *

print(random()) # 0.0~1.0미만의 임의의값 생성
print(random() *10) #0.0~10.0 미만의 임의의 값 생성
print(int(random()* 10)) #0~10 미만의 임의의 값 생성
print(int(random() *10)+1) #1~10 이하의 임의의 값 생성
print(int(random()*45)+1) #1~45 이하의 임의의 값 생성

print(randrange(1, 45)) #1~45미만의 임의의 값 생성 [) 끝구간이 개구간임
print(randint(1, 45)) #1~45이하의 임의의 값 생성 [] 폐구간임

'''range()는 숫자를 연속적으로 만들어 주는 객체임
range 자체는 리스트가 아닌데 , list() 명령을 활용해서 연속적인 숫자가
요소로 들어가는 리스트를 만들어낼 수 있다'''

n = int(input("인사를 몇번할까요?: "))
for i in range(n) :
    print("안녕하세요")
    