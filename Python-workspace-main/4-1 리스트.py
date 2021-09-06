# 리스트 [] , 순서를 가지는 객체의 집합
# a = [], a = list() 라고 선언할 수 있다

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
subway.append('하하') #append는 = 더하기 , 항상 리스트 맨뒤에 붙어, 하나밖에 추가가 안됨, 맨뒤로 가!!
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") #index(어디에 넣을지), 객체 순서로 적어줘야해
print(subway) #(들어갈 위치, 들어갈 값)을 적어줘야해, x번째로 가!!

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # pop 뒤에서 하나씩 꺼내는 함수, 꺼내고 나면 리스트에서 데이터 삭제됨
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인, 같은 값이 몇개 있는지 확인가능
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort() #sort 정렬하는 함수, 당연히 컴퓨터가 숫자 크기에 대해 베이스가 있지, 숫자형과 문자형은 같이 정렬이 안됨, 오름차순으로 정렬됨
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

기린 = ["사자", "얼룩말", "호랑이", "코끼리"]
기린[2] = "호랑이" #리스트[수정하려는 인덱스 번호] = 내용 으로 해주면 리스트가 수정됨

기린 = ["사자", "얼룩말","악어", "호랑이", "코끼리"]
del 기린[4] #del 리스트 이름[지우려는 인덱스 번호], 기린[4]=''이렇게 하면 안돼

'''
1. 리스트는 상황에 따라 자료의 추가와 삭제가 쉽다
2. 하나의 자료에 대해 다양한 자료를 담기가 쉽다
3. 반복 구분을 활용하는데 좋다'''

a = []
number = int(input("몇 분이 오셨나요? "))
for i in range(number) :
    a.append(input("%d번 손님, 주문하시겠어요?" %(i+1)))
print(a)

# 리스트의 길이
len(기린) # len(변수명)


list 
names = ['김강남','양서초', '유신촌'] # []안에 값들이 ,로 구분해서 값을 저장, 각각 index를 가지고있다
print(names[:2]) #names에 index값이 생겨, 구간 [)
for i in names:
    print(i)
#print(names[2]) #이렇게 지정만 하면 index에 해당하는 하나의 값만 나와
# list 객체로 받기
urls = names
new_list = []
for url in urls:
    new_list.append(url) #append 하나의 값을 추가함
new_list #print를 안쓰네??