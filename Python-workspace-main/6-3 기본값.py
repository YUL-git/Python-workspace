# # 함수에서 기본값 설정 방법
# def profile(name, age, main_lang) :
#     print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'\
#         .format(name, age, main_lang) )   #줄이 너무 길때는 \치고 엔터치면 줄바꿈이 됬지만 하나의 문장으로 인식됨

# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

#같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age = 17, main_lang = "파이썬") :
    print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'\
        .format(name, age, main_lang) )   #줄이 너무 길때는 \치고 엔터치면 줄바꿈이 됬지만 하나의 문장으로 인식됨


profile("유재석")
profile("김태호") #이렇게 이름만 적었는데도 나이랑 언어가 나와 이것이 기본값을 배정해주는 것임