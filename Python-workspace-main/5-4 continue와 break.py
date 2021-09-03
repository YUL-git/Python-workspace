absent = [2,5] #결석
no_book =[7] #책을 깜빡했음
for student in range(1,11) : #1,2,3,4,5,6,7,8,9,10
    if student in absent :
        continue
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

#continue를 만나게 되면 밑의 있는 문장을 실행하지않고 skip하고 아래있는 문장을 실행하지 않고
#다음 반복문으로 실행해
#break를 만나면 뒤에 반복값이 있든 없든 상관없이 바로 반복문을 탈출해
