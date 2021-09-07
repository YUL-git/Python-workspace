# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 :{1}\t".format(name,age), end = " ") # end = " "이렇게 써주면 줄바꿈을 하지않고 이문장에 이어서 써준다는 것임
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python","Java", "C", "C++", "C#") # 이런식으로 한문장에 같이 출력됨
# profile("김태호", 25, "KOtlin", "Swift" ,"","","")

# 가변인자 -> 위의 예시로 언어가 5개가 안되면 빈칸을 넣어주어야하고 언어를 5개 보다 많이 하면 함수를 바꿔주어야할때 가변인자를 쓴다
def profile(name, age, *language):  # *로 시작하는 매개변수를 사용해서, *변수명
    print("이름 : {0}\t나이 :{1}\t".format(name,age), end = " ") # , end = " "이렇게 써주면 줄바꿈을 하지않고 이문장에 이어서 써준다는 것임
    for lang in language :
        print(lang, end = "")
    print() # 마지막줄 줄바꿈을 위해서 그냥 넣음

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript") # 이런식으로 한문장에 같이 출력됨
profile("김태호", 25, "KOtlin", "Swift")