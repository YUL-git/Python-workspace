# 파일 입출력, 파일은 만들고 가져오기
''' 파일에 입력하기 2가지 방법 '''
score_file = open("score.py","w", encoding = "utf8") # (파일 이름, writing(쓰기용도), encoding = utf8 한글 지원)
print("수학 : 0", file = score_file) #print()와 file을 이용해서 함
print("영어 : 50", file = score_file)
score_file.close() #항상 파일을 마지막에 .close로 닫아줘야해

# 어떤 내용이 존재하는 파일에다가 추가해서 쓸때 append 사용, w 사용하면 덮어쓰기가 되버려(다른것으로 대체됨)
score_file = open("score.txt", "a", encoding = "utf8")
score_file.write("과학 : 80") # write()를 사용해서 쓸 수있음
score_file.write("\n코딩 : 100") # \n으로 줄바꿈을 할 수 있음
score_file.close()

''' 파일에 있는 내용을 읽어오기 2가지 '''
# 전체 읽어오기
score_file = open("score.txt","r", encoding = "utf8") #read
print(score_file.read()) #파일의 모든 내용을 읽어오기
score_file.close()
# 줄 별로 읽어오기
score_file = open("score.txt","r", encoding = "utf8") #read
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()
# ->여기서는 우리가 몇줄있는지 아니까 4번 print했지

# 몇 줄인지 모를때 
score_file = open("score.txt","r", encoding = "utf8")
while True :
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()

# 마지막 방법은 리스트에다가 값을 다 넣어서 처리할 수 있다
score_file = open("score.txt","r", encoding = "utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines :
    print(line, end = "")

score_file.close()