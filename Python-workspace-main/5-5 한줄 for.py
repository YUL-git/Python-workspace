# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104
students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students] 
#i에다가 100을 더한 값을 넣을건데 students에 있는 아이들을 불러와서 100에 더한 값을 리스트로 바꿔서 여기에 집어넣어라
print(students)

#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]  
#길이는 len()를 쓸 수 있지 i는 students에 들어있는 값을 넣으면서 길이를 리스트로 뽑아내는거지
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)