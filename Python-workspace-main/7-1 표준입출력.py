print("Python", "Java") # , 로 쓰면 띄어쓰기가 자동으로 되지
print("Python" + "Java") # + 를 쓰면 붙어서 나와

# 사실 , 사용에 비밀이 있었는데 ,sep = " (변수 사이에 넣고 싶은 값, 기호) " string형만 가능하다
print("Python", "Java", sep= ",",end = "?") # ,end ="변수" 문장의 끝부분을 변수로 바꿔달라 /이전에는 문장이 끝나면 줄바꿈이 기본형이였지
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout) # stdout -> 표준 출력으로 문장이 찍힘
print("Python", "Java", file=sys.stderr) # stderr -> 표준 에러로 처리됨

#출력 포맷
scores = {"수학":0, "영어":50, "코딩":100} # 사전형
for subject,score in scores.items(): # key,value를 for문에서 활용할 수 있어
    # print(subject,score, end = "  ")
    print(subject.ljust(8),str(score).rjust(4), sep=":") 
    # .ljust(8)같은 경우 8칸을 띄어서 왼쪽 정렬을 의미
    # .rjust(4)같은 경우 4칸을 띄어서 오른쪽 정렬을 의미 , score가 int()형이기에 str()로 바꿔줘야해

# 은행 대기순번표
#001, 002, 003, ...
for num in range(1,21):
    print("대기번호: " + str(num).zfill(3)) 
    # .zfill(3) 3만큼의 공간을 차지하고 값을 집어 넣는데, 값이 없는 공간에 대해서는 0으로 채움

#표준입력, 사용자 입력으로 값을 받을때는 기본적으로 str()로 받게됨
answer = input("아무 값이나 입력하세요 : ") #input()에 적는 값은 str()으로 나와
print("입력하신 값은 " + answer + "입니다.")
