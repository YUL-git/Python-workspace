# 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3") 이런식으로 대기번호를 뽑아주거나 반복적인 실행을 해야할때 1000번이면 다 적을 수가 없지

for waiting_no in [0,1,2,3,4] :
    print("대기번호 : {0}".format(waiting_no)) 
#{0} 값에 .format(0)의 값이 들어가는데 여기서 변수는 리스트형임으로 실행이 종료될때까지 돌아간다
#값이 별로 없을때는 [0,1,2,3,4]로 쓸 수 있지만 값이 순차적으로 많이 커질때는 range를 쓸 수 있다
#randrange() random배울때 배웠지
for waiting_no in range(5): #0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6) : #1,2,3,4,5 6직전까지
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨","토르","아이엠 그루트"]
for customer in starbucks :
    print("{0}, 커피가 준비되었습니다.".format(customer))


''' for "문은 뭔가 반복할 값들이 있는 대상"에 대해서 "차례대로" 값을 받아와서 일정한
내용을 반복하는 데 매우 유용함 
1. 출력할 대상이 정해져 있다. 조건에 의해 반복하는 것이 아니다
2. 대상에 대해서 동일한 것을 반복함. 반복문의 전형적이 상황
따라서 다루고자 하는 값들의 대상이 있고, 이들에 대한 반복적인 작업이 필요할 때는 for 문을 사용'''

'''반복 횟수만 필요할 때 = for 문 + range 함수
'''