# 사전, 단어를 찾으면 단어가 나오고 단어에 대한 정의가 나옴 키와 빌드, 키는 중복이 절대 안돼
cabinet = {3:"유재석", 100:"김태호"} 
#{key:value} 형식으로 함, 캐비넷으로 비유를 하면 유재석씨가 3번 키를 사용하고 김태호씨가 100번키를 사용하는것임
print(cabinet[3])
print(cabinet[100])
print(cabinet[3]+cabinet[100])

print(cabinet.get(3)) #get()함수를 써도돼
print(cabinet.get(5))
print(cabinet.get(5, "사용가능")) 
'''5번이라는 열쇠에 할당된 값이 없어서 none으로 출력 되는데 내가 값으로 출력하고 싶다고 하면 cabinet.get(5, "name")등으로 할당해줄 수 있다
그렇다고 해서 5 번 키에 특정 값이 할당되는 것이 아니라 출력만 내가 지정한 이름으로 출력이 되는 거야'''
#cabinet[5]과 cabinet.get(5)와의 차이점은 전자는 에러가 뜨는 순간 거기서 프로그램이 종료되고 get은 none이라고 뜨고 프로그램이 계속 실행됨 
#print(cabinet[5]) 
# 주의) cabinet[5]라는 정보가 없기 때문에 keyerr가 뜨고 여기서 프로그램이 종료되서 print("hi")가 출력이 안됬어 
#print("hi")

#사전안에 어떤 값이 있는지 확인
print(3 in cabinet) #print(key in 변수) 형식으로 확인
print(5 in cabinet) #없기 때문에 False로 나와

#키 값을 int()가 아닌 str()로도 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"} 
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님이 왔어 ,업데이트하거나 추가 가능
print(cabinet)
cabinet["A-3"] ="김종국"
cabinet["c-20"] = "조세호" 
#새로운 키를 넣을때 c-20이라는 키에 "value"값을 넣어준다, c-20에 이미 값이 있다면 바뀐 값으로 업데이트 된다
print(cabinet)

#간 손님
del cabinet["A-3"]
#del을 이용하여 사전안의 키 값을 지울 수 있어
print(cabinet)

#지금 총 사용중인 key들만 출력
print(cabinet.keys())

#지금 총 사용중인 value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items()) #뒤에서 어떻게 활용하는 나옴

#목욕탕 폐점, 사전안에 모든 키값들을 지움
cabinet.clear()
print(cabinet)


