# 세트, 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3} #사전과 헷갈릴 수 있는데 사전은 key:value를 사용했었지
print(my_set) #1,2,3만 출력되, 중복을 허용하지 않기 때문

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) #[]이렇게 쓰면 리스트형인데 set()을 붙여줌으로써 집합이 됬어

#교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java&python)
print(java.intersection(python))
# print(java and python) 이렇게 해도 안되나?

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # | = or
print(java.union(python))
#print(java or python) 이렇게 해도 안되나?

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호") # 집합에 값을 추가
print(python)

# java를 까먹었어
java.remove("김태호") # 값을 제거할 수 있어
print(java)

