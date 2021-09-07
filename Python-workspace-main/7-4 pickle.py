# pickle은 유용한 라이브러리
'''라이브러리(영어: library)는 주로 소프트웨어를 개발할 때 컴퓨터 프로그램이 사용하는 비휘발성 자원의 모임이다. 
여기에는 구성 데이터, 문서, 도움말 자료, 메시지 틀, 미리 작성된 코드, 서브루틴(함수), 클래스, 값, 자료형 사양을 포함할 수 있다.'''

# 프로그램상에서 사용하는 데이터를 파일 데이터로 저장하는 것, 다른 사람들에게 전송하고 다른사람이 pickle을 이용해서 사용가능
import pickle
profile_file = open("profile.pickle", "wb")
# wb = writing binary (바이너리는 보통 이진법, 둘로 나누어져 있다고 생각하면 편해) 
# pickle에서는 따로 encoding을 만들어줄 필요가 없어, 대신 바이너리는 꼭 정해줘야해
profile = {"이름":"함도윤","나이":24,"취미":["코딩","농구","책읽기"]}
print(profile)
# 이제 여기서 pickle을 이용해서 데이터에 씀
# 여기서 pickle.dump(파일에 저장할 내용, 변수명)
pickle.dump(profile, profile_file) #profile 에 있는 정보를 profile_file에 저장 
profile_file.close()

# 이번에는 profile.pickle의 파일을 가져와 보자
profile_file = open("profile.pickle", "rb") #rb = reading binary
# 여기서 pickle.load(변수명)
profile = pickle.load(profile_file) # profile이란 변수를 만들고 file에 있는 정보를 profile에 불러오기
print(profile) # 잘 불러왔는지 확인 해보자
profile_file.close()