'''
### 변수의 범위
# 변수를 특정 지역에서만 사용되는 지역변수 (블럭내 사용)와
# 지역에 상관없이 전 영역에서 사용되는 전역변수로 분류. (변수의 스코프 - 범위)
# 특정 영역(블럭)은 함수 또는 블럭(if, for, while등)등을 의미함.


# 예제 1, 전역변수의 영역 : 블럭에서만 동작

# global 변수, 전역 변수
var2 = 2

# 함수 정의
def func(arg):
    var1 = 1
    print(var1,var2,arg)
    
#메인
func(var2)
#print(var1) #함수 func에 블럭 내에 선언된 변 - 함수가 종료되면서 사라짐


# 예제 2, 블럭에서 전역변수를 사용

# global 변수, 전역 변수
var2 = 2

# 함수 정의
def func(arg):
    global var2           # 전역 변수 var2를 호출
    var2 = 10             # 전역변수 var2에 10 대입
    print(var2,arg+2)
    
#메인
func(var2)
print(var2)

# 함수 또는 블럭에서 변수명으로 데이터에 접근시 우선순위 : 가까운 local -> global

# 예제 3

# global 변수, 전역 변수
var2 = 2

# 함수 정의
def func(arg):
    global var2           # 전역 변수 var2를 호출
    var2 = 10             # 전역변수 var2에 10 대입
    var1 = 1
    print(var2,arg+2)
    def func2(var2):
        var2 = 1
        print(var2,arg,var1)   # 1, 10, 1 -> local을 먼저 보기 떄문
    func2(var2)
    
#메인
func(var2)
print(var2)


## 중첩함수
# 중첩함수란, 함수 내부에 또 다른 함수가 내장된 형태.
# 내부 함수를 포함한 함수를 외부함수라고 표현한다.
#
#   (형식)
#   def 외부함수 (인수) :
#       함수 정의문1
#       def 내부함수(인수):
#           함수정의문(내부)1
#           return 값
#       return 내부함수
#
# 파이썬의 중첩함수는 외부함수나 내부함수를 변수에 저장할 수 있다.
# 이런 특징을 가지는 함수를 일급함수(First class Function)이라고 한다.
# 특히, 내부함수는 외부함수의 return 명령문을 이용하여 변환하는 형태의 함수를
# 클러져(Function closer)라고 한다. 특징은 외부함수가 종료되어도 내부함수에서
# 선언된 변수가 메모리에서 소멸하지 않는 상태로 내부함수를 사용할 수 있다.


def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b

b = a() # 외부 함수 호출 : a 함수가 출력
b()     # 내부 함수 호출 : b 함수가 출력

###
data = list(range(1,101))

# outer
def outer_func(data):
    dataSet = data  #data로 받은 값을 dataSet 변수에 집어넣음
    
    #inner
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    
    return tot, avg     #inner 반환 (tuple)

# 메인
# 외부함수 호출 : data 생성
tot, avg = outer_func(data)     # tot, avg = tot avg (outer_func()의 return 값) > unpacking

# 내부함수 호출
tot_val = tot() # outer_func 내에 있는 tot() 함수
print("tot = ",tot_val)
avg_val = avg(tot_val)
print("avg = ",avg_val)


# 역할
# 외부 함수 : 함수에서 사용할 자료를 만들고, 내부함수를 포함하는 역할
# 내부 함수 : 외부함수에서 만든 자료를 연산하고 조작하는 역할을 담당



#[Quiz]
# 디폴트 매개변수를 이용한 요금 구하는 프로그램 만들기
# 기본 요금은 500원
# 환승이 없거나 환승 1회까지는 기본요금
# 1회를 초과하는 환승의 경우 환승 1회마다 요금이 2배씩 증가
# [EX) 환승 2회인 경우 : 1000원, 환승 3회인 경우 : 2000원]
# [장거리는 10000원으로 처리한다.]
# 1. 환승 안함
# 2. 환승 함            #(몇번 환승하는지 질의 후 요금 계산)
# 3. 장거리
# <<** 함수화하여 작업>> -> 요금계산하는 함수, 화면에 표시하는 함수

def fee_no():
    fee = 500
    return fee

def fee_yes(time):
    fee = 500*(2**(time-1))
    return fee

def fee_long():
    fee = 10000
    return fee

def print_fee():
    fee1 = 0
    dest = input("목적지를 입력하세요 : ")
    sel = input("1.환승 안함\n2.환승 함\n3.장거리\n이용 방법을 선택하세요 : ")
    if sel == '1':
        fee1 = fee_no()
    elif sel == '2':
        time = int(input("몇 회 환승하시겠습니까 : "))
        fee1 = fee_yes(time)
    elif sel == '3':
        fee1 = fee_long()
    else:
        print("입력 오류")
        return
    print("{}까지 요금은 {:,} 원 입니다.".format(dest,fee1))

print_fee()


# match~case 구문 : 파이썬 3.10.0 이후에 도입
#   다른 언어의 switch ~ case 구문과 같은 동작

# 예제1
from re import A


def num_chk(st):
    match st:
        case 1 :
            return "일"
        case 2 :
            return "이"
        case 3 :
            return "삼"
        case _ :            # default
            return "선택 범위를 벗어났습니다."
        
st1 = int(input("1에서부터 3까지의 숫자를 입력하세요 : "))
print("입력값은 : "+num_chk(st1)+"입니다.")

# 예제2
def alpha_chk2(chk):
    match chk:
        case 'a'|'A' :
            return 'A'
        case 'b'|'B' :
            return 'B'
        case 'c'|'C' :
            return 'C'
        
st2 = input("알파벳 a~C 중 한 개를 입력하세요 : ")
print("입력한 알파벳은 : ",alpha_chk2(st2))


## 연습 : 국가명을 입력받아 해당 국가 폰 번호를 출력하는 함수 구현.
# 01 - UnitedState
# 33 - France
# 34 - Spain
# 81 - Japan
# 82 - SouthKorea
# 코드가 없는 경우에는 "-1" 출력
# (예) getPhoneCode("SouthKorea") -> 82

def getPhoneCode(natn):
#def getPhoneCode(contry:str) -> int  ## 인자값을 str로 받고, 리턴값을 int로 준다.
    match natn.lower() :
        case 'unitedstate' :
            return '01'
        case 'france' :
            return '33'
        case 'spain' :
            return '34'
        case 'japan' :
            return '81'
        case 'southkorea' :
            return '82'
        case _ :
            return '-1'
        
temp = 'Japan'
print(getPhoneCode(temp))


#lambda 함수
# 익명 함수로 일시적으로 사용하는 함수를 의미함.
# 사용은 함수가 생성된 곳에서 필요한 경우, 사용한 후 버리는 함수

# (형식)
# lambda 인자리스트 : 표현식

# 예) lam = lambda x : x**2
#     print(lam(8))     =>  출력결과 : 64#
#
#     lam2 = lambda x,y : x+y
#     print(lam2(2,5)) => 출력결과 : 7
# 람다는 어디든지 사용할 수 있는 임시함수




lam = lambda x : x**2
print(lam(8))

lam2 = lambda x,y : x+y
print(lam2(2,5))

# 예제1) 다음과 같은 함수를 lambda로 표현

# 함수
def swap(a,b):
    return b,a
a = 100
b = 200
print("swap전 : ",a,b)
a,b = swap(a,b)
print("swap후 : ",a,b)

# 람다 사용
lam_swap = lambda x,y : [y,x]
print(lam_swap(a,b))

# 예제2)
lam = lambda a: a*10
lam2 = lambda a,b : a+b
noData = lambda : print("인자가 없는 lambda")

# 결과 확인
print(lam(10))
print(lam2(10,20))
noData()

# 예제3)
def str_len(s):
    return len(s)

string = ['bob','charles','alexander3','teddy']
# 알파벳 순서로 정렬 => string.sort(key="str_len") => 문자열의 길이를 기준으로
string.sort(key=str_len)
#string.sort(key=lambda s:len(s))
print(string)

## lambda가 유용하게 사용되는 3가지 대표적 함수
# filter : 특정 조건을 만족하는 요소만 남기고 필터링
# map : 각 원소를 주어진 수식에 따라 변경하여 새로운 리스트를 반환
# reduce : 차례대로 앞 23개의 원소를 가지고 연산. 연산 결과가 또 다음 연산의 입력으로 진행됨.
#           따라서 마지막까지 진행되며 최종 출력은 한개의 값만 남게 됨


# filter(함수, 리스트)
#filter(function, iterable) -> 특정 조건의 요소만 남기고 필터링
#                               리스트에 있는 내용은 함수에 대입하여 결과값을 처리 (True or False)

# 함수를 사용
def even(n):
    return n%2 == 0

print(even(4))

nums = list(range(1,11))
filter_list = list(filter(even, nums))
print(filter_list)          # [2, 4, 6, 8, 10]


# lambda를 사용
filter2_list = list(filter(lambda n:n%2==0, nums))
print(filter2_list)

# map : 특정 조건에 맞는 새로운 리스트를 생성
# 주어진 리스트, 리스트의 제곱은 한 숫자 새로운 리스트

# map(func.iter1) : 각 멤버를 func으로 동작시킨 후에 새롭게 리스트 생성
nums = [1,2,3,4,5]
print(list(map(lambda n:n**2,nums)))        # [1, 4, 9, 16, 25]

# reduce 함수 : functools 모듈 내에 존재함.
import functools

a = [1,2,3,5,8]
# 리스트 내의 모든 숫자의 합
print(functools.reduce(lambda x,y:x+y,a))       #19



# 람다 함수를 이용하여 사칙연산
lam_pl = lambda x,y:x+y
print(lam_pl(1,2))

lam_mi = lambda x,y:x-y
print(lam_mi(2,1))

lam_mult = lambda x,y:x*y
print(lam_mult(2,1))

lam_div = lambda x,y:x/y
print(lam_div(2,1))

import os

while True:
    os.system('cls')
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))
    sign = input("계산 기호를 입력(+,-,*,/) : ")
    if sign == '+':
        print("계산 결과 : ",lam_pl(num1,num2))
    elif sign == '-':
        print("계산 결과 : ",lam_mi(num1,num2))
    elif sign == '*':
        print("계산 결과 : ",lam_mult(num1,num2))
    elif sign == '/':
        print("계산 결과 : ",lam_div(num1,num2))
    else :
        print("계산 기호를 잘못 입력했습니다.")
        os.system('pause')
    sel = input("계속하겠습니까? (Y/n) : ")
    if sel == 'n' :
        break
    
### 획득자 (getter), 지정자(setter), nonlocal
# 내부 함수는 중첩함수에서 함수 클로져 역할도 하지만, 함수 내 자료를 외부로 획득하거나
# 자료를 수정하는 역할도 한다.
# 이런 내부 함수들을 획득자(getter), 지정자(setter)라고 부르며
# 역할과 필요 조건은 다음과 같다.

# 획득자 함수 : 함수 내부에 생성한 자료를 외부로 반환하는 함수로 반드시 return 명령 갖는다.
# 지정자 함수 : 함수 내부에 생성한 자료를 외부에서 수정하는 함수로 반드시 매개변수를 갖는다.
#               만약 외부함수에서 생성된 자료를 수정할 경우 해당 변수에 nonlocal 명령어를 쓴다

# (형식)
#   def 외부함수() :
#       변수명 = 값
#       def 내부함수() :
#           nonlocal 변수명

# 예시) 획득자와 지정자 함수 그리고, nonlocal 명령어를 이용하여 외부함수에서 생성한 자료를
#       외부에서 획득하고, 수정하는 예문

# 함수 정의
def main_func(num) :
    num_val = num   #자료를 생성
    def getter():   #획득자 함수...return
        return num_val
    def setter(value) :     #지정자 함수 인수 있음..
        nonlocal num_val    # nonlocal 명령어
        num_val = value
    return getter, setter   #함수 클러져 반환    
    
    
# 함수 호출

getter, setter = main_func(100)     # num 생성

# 획득자 getter 호출
print("num = ",getter()) # 획득한 num 확인 num = 100

# 지정자 setter 획득
setter(200)
print("num = ", getter())   # num 값 수정 확인 num = 200


## 함수 장식자(decoration)는 기존 함수 시작부분과 종료 부분에 기능을 장식하여 추가해주는
# 별도의 함수를 의미함.
# 즉, 현재 실행되는 함수를 파라미터로 받아서 꾸며줄 내용과 함께 해당 함수를 감싸주는
# 함수(Wrapping function)

# (형식)
#   @함수 장식자       => 사전에 만들어져 있어야 함. @wrapping함수명
#   def 함수명():
#       함수 실행문
#

# wrapper 함수
def wrap(func):
    def decorated():
        print("반가워요~~~!!")     # 시작 부분에 삽입
        func()                     # 인수로 넘어온 함수를 실행
        print("반가웠어~~ 안녕!!")  # 종료 부분에 삽입        
    return decorated                #클로저 함수 반환

# 장식자 적용할 함수
@wrap
def hello():
    print("hi~~", '홍길동^^')

#함수 호출
hello()

'''
## 재귀함수(Recursive Function)
# 함수 내부에서 자신의 함수를 반복적으로 호출하는 함수
#

# 재귀함수는 반복적으로 호출하기 때문에 반드시 함수 내에 반복을 탈출(exit) 조건이 필수
# 재귀함수는 반복적으로 변수를 조금씩 변경하여 연산을 수행하는 알고리즘에서 이용됨.
#
# 예제로 팩토리얼(Factorial)계산

# 예제) 카운트 -> 1~n까지의 정수를 count하는 과정
# 재귀함수 정의
def Counter(n):
    if n == 0:
        return 0    # 종료 조건
    else:
        print(n)
        Counter(n-1)    # 재귀함수 호출

# 함수 호출1
print("n = 0 : ", Counter(0))       # n = 0, 0

# 함수 호출2
Counter(5)


# 예제) 누적합
# 1~n까지 정수를 카운트한 값을 누적하여 반환하는 경우

# 재귀함수 정의
def Adder(n):
    if n == 1 : # 종료조건
        return 1
    else :
        result = n + Adder(n-1) #재귀 호출
        
        print(n, end=' ')   #스택 영역 : 만약 n = 5 (시작) -> 2 3 4 5
        return result 
    
# 함수 호출
print("n = 1 : ",Adder(1))

print("n = 5 : ",Adder(5))