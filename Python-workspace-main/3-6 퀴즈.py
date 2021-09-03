# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http://부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제와 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                 nav             (5)         (1)             (1)
# 예) 생성된 비밀번호 : nav51!

# 나의 풀이
passward = "http://naver.com"
passward2 = passward[7:] #규칙1 
passward3 = passward2[:-4]
lastpassward = passward3[:3] + str(len(passward3)) + str(passward3.count("e")) + "!"
print(lastpassward)

'''풀이를 보고 느낀 것은 변수를 굳이 다른 이름으로 계속 바꿔줄 필요가 없다->가장 밑의 변수로 최신화 되기때문!
문자열처리함수 replace를 생각하지 못했다
슬라이싱을 할때 [:my_str.index(.)]'''
#풀이
url = "http://naver.com"
my_str = url.replace("http://","") #규칙1 빈칸으로 만드는거야
#print(my_str)
my_str = my_str[:my_str.index(".")] #규칙2
# my_str[0:5] -> 0~5 직전까지.
#print(my_str)
passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, passward))