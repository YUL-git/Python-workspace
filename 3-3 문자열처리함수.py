python = "Python is Amazing" #p와 a만 대문자로 적었어
print(python.lower())
print(python.upper())
print(python[0].isupper()) #0번째 문자열에서 대문자인지에 대한 참/거짓 #python[0:1]이런식으로 슬라이싱으로 해도 참/거짓 판정 가능(슬라이싱한 것도 결국 문자열이기때문)
# print(python[0].islower()) #이 같은 경우에도 소문자인지 참/거짓 판정가능
print(len(python)) #이 문자열의 길이를 잼(띄어쓰기도 포함)
print(python.replace("Python", "Java")) #문자를 replace로 바꿀 수 있어

index = python.index("n") #n의 첫번째 위치를 찾음 #숫자 정보로 인식이 됨
print(index)
index = python.index("n", index + 1) #앞에서 나온 5라는 위치에서 1을 더한 6이후의 위치부터 n이 어디에 위치했는지 찾음
print(index)

print(python.find("n")) #find함수로도 n의 첫번째 위치를 찾을 수 있어
#print(python.find("n", index +1)) 이렇게 해도 6이후의 위치부터의 n의 위치를 탐색해
print(python.find("Java")) #이 문자열에 포함되어있지 않으면 -1을 표시해
#print(python.index("Java")) #python이라는 변수에는 Java가 없기 때문에 err가 남 find함수와 차이가남
print("hi")

print(python.count("n")) #python변수에서 n이 몇번 등장하는지 나타냄
''' 변수명.lower upper isupper islower replace index() find()
문자열을 처리한다 = 문자열 관련 명령을 구현하는 함수'''
