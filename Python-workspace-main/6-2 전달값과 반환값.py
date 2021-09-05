# 함수에서 () 괄호 안에 전달하는 값이 없는 경우도 있고 있는 값을 전달하고 돌려받는(반환값) 경우도 있음
def open_account() : # def 함수 이름 () :  
    print("새로운 계좌가 생성되었습니다") # 여기까지는 함수가 실행이 안돼

open_account() # 함수명() 을 해줘야 함수가 실행이 돼  ->반환값

def deposit(balance, money) : #입금, def 함수명 (전달값) :    balance: 잔액  money : 새로 입금받는 금액
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money  # return이 반환이다. 

# balance = 0 #잔액
# balance = deposit(balance, 1000)
# print(balance) # return balance + money 에 의해서 함수값에 balance = 1000 이 반환되서 저장됨

def withdraw(balance, money) : #출금
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

# balance = 0 #잔액
# balance = deposit(balance, 1000)
# balance = withdraw(balance,2000)

def withdraw_night(balance, money) : #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission #튜플 형식, 두개의 값을 콤마로 나눔, 여러개의 값을 한번에 반환 할 수 있어

balance = 0 #잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance,2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# balance = 0 #잔액
# balance = deposit(balance, 1000)
# #balance = withdraw(balance, 1000)
# #balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))