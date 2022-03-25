'''
# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용하여 동작하게 만드세요.
#       함수 명은 "calc([문자열인자값])"으로 하세요

def calc(calc):
    if '+' in calc:
        num1,num2 = calc.split('+')
        num1 = int(num1); num2 = int(num2)
        print("계산 결과는 : ",num1+num2)
    elif '-' in calc:
        num1,num2 = calc.split('-')
        num1 = int(num1); num2 = int(num2)
        print("계산 결과는 : ",num1-num2)
    elif '*' in calc:
        num1,num2 = calc.split('*')
        num1 = int(num1); num2 = int(num2)
        print("계산 결과는 : ",num1*num2)
    elif '/' in calc:
        num1,num2 = calc.split('/')
        num1 = int(num1); num2 = int(num2)
        print("계산 결과는 : ",num1/num2)
    else:
        print("수식입력이 잘못됐습니다.")
        
    # 메인
import os
    
while True:
        os.system('cls')
        txt = input("계산할 수식을 입력해주세요[ex) 5+5 : ")
        calc(txt)   # 함수 호출
        sel = input("계속하겠습니까?(Y/n) : ")
        if sel == 'n' :
            break
print("프로그램 종료합니다")




# 예제 3) 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
#       사용자로부터 입력받은 값을 인자값으로 처리하는 함수
#       함수에 return을 사용하여 반환값을 처리하는 예제

# 함수 정의
def pr3(str1):
    """연산 결과 후에 반환값을 전달하는 함수"""
    return "입력한 문자열 : " + str1
    
# 메인
txt = input("입력 : ")
print()
pr_out = pr3(txt)
print(pr_out)

# 실습) 위 내용을 토대로 계산 결과를 반환값으로 처리하는 함수로 변환

def calc(calc):
    if '+' in calc:
        num1,num2 = calc.split('+')
        num1 = int(num1); num2 = int(num2)
        return num1+num2
    elif '-' in calc:
        num1,num2 = calc.split('-')
        num1 = int(num1); num2 = int(num2)
        return num1-num2
    elif '*' in calc:
        num1,num2 = calc.split('*')
        num1 = int(num1); num2 = int(num2)
        return num1*num2
    elif '/' in calc:
        num1,num2 = calc.split('/')
        num1 = int(num1); num2 = int(num2)
        return num1/num2
    else:
        print("수식입력이 잘못됐습니다.")
        
    # 메인
import os
    
while True:
        os.system('cls')
        txt = input("계산할 수식을 입력해주세요[ex) 5+5 : ")
        result = calc(txt)   # 함수 호출
        print("계산 결과 : ",result)
        sel = input("계속하겠습니까?(Y/n) : ")
        if sel == 'n' :
            break
print("프로그램 종료합니다")



# 두 수에 대한 한 번의 계산식을 입력받아서 결과를 출력하는 코드를 이용
# - 사용자가 계산식을 입력. 이것을 이용해서 처리
# - calc()가 인자값으로 두 정수와 계산식을 인자로 받아 처리하는 함수


def calc(num1,num2,sign):
    if sign == '+':
        return num1+num2
    elif sign == '-':
        return num1-num2
    elif sign == '*':
        return num1*num2
    elif sign == '/':
        return num1/num2

# 메인
import os
    
while True:
        os.system('cls')
        txt = input("계산할 수식을 입력해주세요[ex) 5+5 : ")
        if '+' in txt:
            num1,num2 = txt.split('+')
            num1 = int(num1); num2 = int(num2); sign='+'
        elif '-' in txt:
            num1,num2 = txt.split('-')
            num1 = int(num1); num2 = int(num2); sign='-'
        elif '*' in txt:
            num1,num2 = txt.split('*')
            num1 = int(num1); num2 = int(num2); sign='*'
        elif '/' in txt:
            num1,num2 = txt.split('/')
            num1 = int(num1); num2 = int(num2); sign='/'
        else:
            print("수식입력이 잘못됐습니다.")
        result = calc(num1,num2,sign)   # 함수 호출
        print("계산 결과 : ",result)
        sel = input("계속하겠습니까?(Y/n) : ")
        if sel == 'n' :
            break
print("프로그램 종료합니다")


## 함수 인자 기본값 (default) 설정
#   default 이란? 입력 인자값이 없는 경우에 기본적으로 적용되어지는 값

# 형식)
# def 함수이름(param1, param2=1):
#       함수상세문1
#       함수상세문2

# 예제 4) 함수 인자의 기본값 설정 (인자1)
def pr4(par1=10):
    print(par1)
    
#메인
pr4(10)
pr4(20)
pr4(3)
pr4()

# 인자를 2개 가진 경우 (모두 default인 경우)
def pr5(par1=10,par2=20):
    print(par1,par2)
    
# 메인
pr5(100,100)
pr5(100)
pr5(200)
pr5(par2=200)
pr5()

#이 인자가 2개 이상, 기본값 1인 경우
def pr6(par1,par2=20):
    print(par1,par2)
    
pr6(100,100)
pr6(100)
pr6(200)
#pr6()           #에러 : 인자는 반드시 전달되어야 한다

#인자의 기본값이 맨 앞에 있는 경우
#def pr7(par1=10,par2):  # SyntaxError : 기본값 뒤에는 일반 인자가 존재 x
#    print(par1,par2)



#[Quiz]
# 1. 짝, 홀수를 구분하는 함수를 작성해 주세요.
def quiz1(num):
    if num % 2 == 0:
        return "짝수"
    else :
        return "홀수"
num1 = int(input("숫자 입력 : "))
print(num1,"은 ",quiz1(num1),"입니다.")

# 2. "3"의 배수를 판별하는 함수를 작성해 주세요.
def calc(num1,num2,sign):
    if sign == '+' :
        return num1+num2
    if sign == '-' :
        return num1-num2
    if sign == '*' :
        return num1*num2
    if sign == '/' :
        return num1/num2
    
def Output(num1,num2,sign,result):
    print(num1,sign,num2,"=",result)

def Input():
    num1,sign,num2 = int(input("첫번째 정보 입력 : ")) \
        ,input("계산 기호 입력 : "), int(input("두번째 정수 입력 : "))
    result = calc(num1,num2,sign)
    Output(num1,num2,sign,result)

#메인
input()

# 입력 => 계산 처리 => 출력

# 4. 거꾸로 수를 변환하는 함수를 계산, 출력 기능으로 나눠서 작성해 주세요 (예: 123 -> 321)

def reverseCode(result):
    tmp, su = 0,0
    while True:
        tmp = result%10
        result = result // 10
        su = (su + tmp) * 10
        if not result:
            return su // 10
        
def display():
    result, su = 0,0 
    result = int(input("4. 정수 입력 : "))       
    su = reverseCode(result)
    print("변환 전 값 : {} , 변환 후 값 : {}".format(result,su))
    
# 메인
display()

# 5. 친구이름 관리를 함수로 기능을 나눠서 작성해주세요.

def fr_list(lst) : # 친구 목록 보기
    print("="*15,"친구 목록 보기","="*15)
    if lst != []:
        for i in range(len(lst)):
            print(f"{i} : {lst[i]}")
    else:
        print("등록된 친구가 없습니다.")

def fr_add(lst):    # 친구 목록 추가
    name = input("추가할 친구 이름을 입력하세요 : ")
    lst.append(name)
    
def fr_del(lst):    # 친구 목록 삭제
    name = input("삭제할 친구 이름을 입력하세요 : ")
    if name in lst:
        lst.remove(name)
    else:
        print("삭제할 친구가 없습니다.")

def fr_mod(lst):    # 친구 목록 수정
    name = input("수정할 친구 이름 입력하세요 : ")
    if name in lst:
        idx = lst.index(name)
    else:
        print("수정할 친구가 없습니다.")
        return
    name_mod = input("변경 이름을 입력하세요 : ")
    lst[idx] = name_mod
    
# main
import os

fr_lst = []
while True:
    os.system('cls')
    print("="*15,"친구 관리 프로그램","="*15)
    print("1. 친구 목록 보기")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 친구 수정")
    print("0. 종료")
    sel = input("메뉴를 선택해주세요 [0-4] : ")
    if sel == '1':
        fr_list(fr_lst)
        os.system('pause')
    elif sel == '2':
        fr_add(fr_lst)
        os.system('pause')
    elif sel == '3':
        fr_del(fr_lst)
        os.system('pause')
    elif sel == '4':
        fr_mod(fr_lst)
        os.system('pause')
    elif sel == '0':
        print("프로그램을 종료하겠습니다.")
        break
    else :
        print("입력이 잘못되었습니다.")
        
#문제) 알바 시급 프로그램 작성 (default 인자값 사용)
#   시급 : 8500원, 하루 8시간, 한달 30일(기본값)
# 
# 다음과 같이 출력되게 만드세요
# (출력 결과)
# <<시급 계산 프로그램>>
# 1. 기본급
# 2. 일한 날짜 입력
# 번호 입력 >>.

def alba(day=30):
    time = 8; price = 8500
    re = time * price * day
    return re

def display():
    num = input("<<시급 계산 프로그램>>\n1. 기본급\n2. 일한 날짜 입력\n번호 입력>> ")
    if num == '1':
        result = alba()
    elif num == '2':
        day = int(input("일한 일수 입력 : "))
        result = alba(day)
    print("당신의 급여는 {:,}원 입니다.".format(result))
    
#메인
display()
'''
# 인자값 처리 방식1 ==> 연속된 자료를 처리하는 함수의 인자 처리 방식

# 예제
def pr8(a,b,c):
    print(a,b,c)
    
# 메인
pr8(10,20,30)      #10 20 30


# "*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자의 값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking" 하는 방식으로 인자를 전달
x = [100,200,300]
y = [10,20]
z = 1,2,3,4

pr8(*x)        # a,b,c = [100,200,300

pr8(*y,30)

# pr8(*z)     # TypeError

# "*"를 이용하여 연속된 자료(리스트, 튜플)에 데이터를 인자로 전달이 가능하나
# 인자의 개수와 전달되는 자료의 개수는 같아야 한다.

# 인자값 처리방식 2 --> 가변 인자 값 처리...
# - 고정 인자 => 인자값을 반드시 정해진 값으로 1:1로 인자를 전해야하는 인자 (일반)
# - 가변 인자 => 인자값을 정해진 갯수로 전달하지 않고, 가변적으로 전달 가능한 인자

# 가변인자 설정은 함수 정의시에 매개변수 (인자) 앞에 "*"를 사용한다.

# 전달된 인자 값들의 합을 구하는 예제
def sum_func(*par):
    result = 0
    print(par,type(par))    # 전달된 인자값 처리 방식
    for su in par:
        result += su
    return result

def display():
    Sum = 0
    Sum = sum_func()
    print(Sum)
    Sum = sum_func(10,20,30)
    print("인자가 세개(10,20,30)인 경우 결과 : ",Sum)
    Sum = sum_func(10,20,30,40,50)
    print("인자가 다섯개(10,20,30,40,50)인 경우 결과 : ",Sum)
    
#메인
display()

# 주의) 인자값 처리함에 있어 고정인자와 가변인자를 동시에 사용하는 경우,
# 고정인자를 먼저 처리하도록 한다. 즉, 가변 인자는 마지막에 사용되게 해야 한다.

# "*"를 사용하는 경우는 딕셔너리에 대한 packing을 시도한다는 의미로 처리

# 예제) 딕셔너리 자료형을 받아서 처리하는 함수
def dic_func(**par):
    print(par,type(par))
    for k in par:
        print("{}:{}".format(k,par[k]))
        
# 메인
dic_func(피카츄='1마리',파이리='2마리',꼬부기='없음',라이칸=1)

dic = {
    'sep' : '-',
    'end' : '\n\ntest'
}

lst = ['test1','test2','test3','test4']

print('test','test',**dic)
print(*lst,**dic)