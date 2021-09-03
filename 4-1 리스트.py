# 리스트 [] , 순서를 가지는 객체의 집합

#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30 #기존에 이렇게 적었던 것을 하나로 연속적인 공간에 묶는다

subway = [10, 20, 30]
print(subway)

subway = ["유재석" , "조세호", "박명수"]

#조세호씨가 몇번째 칸에 타고있는가?, 리스트를 어떻게 활용을 하냐!!
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append('하하') #append는 = 더하기 , 항상 리스트 맨뒤에 붙어, 하나밖에 추가가 안됨
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") #index(어디에 넣을지), 객체 순서로 적어줘야해
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # pop 뒤에서 하나씩 꺼내는 함수, 꺼내고 나면 리스트에서 데이터 삭제됨
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인, 같은 값이 몇개 있는지 확인가능
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort() #sort 정렬하는 함수, 당연히 컴퓨터가 숫자 크기에 대해 베이스가 있지, 숫자형과 문자형은 같이 정렬이 안됨
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#값들을 모두 지우고 싶어
num_list.clear() #clear 지우는 함수 
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
num_list = [5,4,3,2,1]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


