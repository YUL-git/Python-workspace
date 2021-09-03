# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} #집합이지 {}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu)) #type이 리스트형으로 바꼈어 []

menu = tuple(menu)
print(menu, type(menu)) #튜플로 바뀜 ()

menu = set(menu)
print(menu, type(menu))
