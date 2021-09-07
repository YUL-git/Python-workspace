# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성병에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# 나의 풀이
def std_weight(height, gender):
    weight1 = round(height * height * 22 /10000,2)
    weight2 = round(height * height * 21 /10000,2)
    if gender == "남자" :
        print("키 {0} {1}의 표준 체중은 {2}입니다.".format(height, gender, weight1))
    elif gender == "여자" :
        print("키 {0} {1}의 표준 체중은 {2}입니다.".format(height, gender, weight2))
    return height, gender

std_weight(178, "남자")
std_weight(168, "여자")


# 다른 풀이
# 계산식을 함수로 만들었어
def std_weight(height, gender):
    if gender == "남자" :
        return height * height * 22
    else :
        return height *height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender),2) # 함수 계산식을 이용하기만 함
print("키 {0} {1}의 표준 체중은 {2}입니다.".format(height, gender, weight))
