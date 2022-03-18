###input() 함수 : 문자열을 입력 받는 함수로 반환값은 str(문자열)*
#print(type(input()))

#print(input("입력: "))

'''
#문자형 숫자 입력
num = input("숫자 입력 : ")
print('num type : ',type(num))
print('num = ',num)
print('num = ',num*2)

#숫자 연산을 위한 형변환
num1 = int(input("정수 입력 : "))
print('num1 = ',num1*2)

num2 = float(input("실수 입력 : "))
result = num1 + num2
print('result = ', result)

## 정리, 인자(promt)에 입력 받기 위한 설명을 사용할 수 있다.
# input()는 문자열로 입력을 받기 떄문에 숫자로 사용하기 위해서는
# 필요한 형태로 형변환을 반드시 해야 한다.

name = input("이름 입력 : ")
age = int(input("나이 입력 : "))
print("'{}'님의 나이는 {}세 입니다.".format(name,age))
print(f"'{name}' 님의 나이는 {age} 세 입니다.")
'''
'''
### 연산자
#
#
# (1) 산술 연산자
# (2) 비교(관계) 연산자

print(3==3)     #True
print(3!=3)     #False
print(3>2)      #True
print(3<2)      #False
print(3>=2)     #True
print(3<=2)     #False

# (3) 논리 연산자 : 두 항의 값이 참인지 거짓인지 확인하여 판단하는 연산자 -> bool

#   "and(논리곱)"   :   두 항의 값이 모두 True인 경우에 True를 반환
#   "or(논리합)"    :   두 항 중 하나라도 True인 경우에 True를 반환
#   "not(부정)"     :   True이면 False를, False이면 True를 반환

print("bool의 True의 int형변환 값은 : ",int(True))

print( 0 and 0)     #False
print( 1 and 0)     #False
print( 0 and 1)     #False
print( 1 and 1)     #True

print( 0 or 0)      #False
print( 1 or 0)      #True
print( 0 or 1)      #True
print( 1 or 1)      #True

print(not 0)        #True
print(not 1)        #False


# (4) 멤버 연산자
# 왼쪽 피 연산자의 값이 오른쪽 연산자 멤버 중 일치 여부를 확인하는 연산자

# in        : 왼쪽 피 연산자의 값이 오른쪽 피연산자에 존재하는 경우 True
# not in    : 왼쪽 피 연산자의 값이 오른쪽 피연산자에 존재하지 않는 경우 True

print ( 1 in (1,2,3))       #True
print ( 1 not in (1,2,3))   #False


# (5) 식별 연산자
# 식별값을 비교 연산하여 처리하는 연산자
#   is      : 두 피연산자의 식별값(객체 타입)을 비교하여 동일 객체라면 True
#   is not  : 두 피연산자의 식별값을 비교하여 동일하지 않은 객체라면 True

num1, num2 = 1, "1"

print(type(num1) is int)       #True
print(type(num2) is not int)    #True
print(type(num1) is not str)    #True
print(type(num2) is str)        #True

# (6) 비트 연산자

# 비트값을 연산처리하는 연산자들...
# &     : 두 비트 and 연산처리하는 연산자 (논리곱)
# |     : 두 비트 or 연산처리하는 연산자 (논리합)
# ^     : 두 비트 xor 연산처리하는 연산자(배타적 논리합)
# <<    : 왼쪽 피 연산자의 비트를 왼쪽으로 오른쪽 숫자만큼 이동
# >>    : 왼쪽 피 연산자의 비트를 오른쪽으로 오른쪽 숫자만큼 이동

# &     : AND 비트 연산
#           00001010(10)
#         & 00001111(15)
#           ============
#           00001000(8)

print(10&13)

# |     : or 비트 연산
#           00001010(10)
#         | 00000101(5)
#           ============
#           00001111(15)

print(10|5)

# ^     : xor 비트 연산 : 암호문 처리할 경우에 많이 사용됨
#                         두 비교 비트가 동일하면 False(0)를 반환하고, 둘 중 하나라도 1이라면 1
#           00001010(10) - 원본
#         ^ 00001101(13) - 키
#           ============
#           00000111(7)  - 암호
#         ^ 00001101(13) - 키
#           ============
#           00001010(10) - 원본
            
print(10^13)
print(7^13)

# <<    : 왼쪽 shift 연산자
#           00001010(10)
#         <<          3
#          =============
#           01010000(80)
#   특징 : 2제곱승으로 곱하는 정수 곱하기

print(10<<3)

# >>    : 오른쪽 shift 연산자
#           00001010(10)
#         >>          3
#          =============
#           00000001(1)
#   특징 : 2제곱승으로 나누는 정수 곱하기

print(10>>3)
'''


'''
문제1. num1, num2, num3 = 5, 15, 27
   위 변수에 할당된 값을 사용하여 다음의 결과가 나오도록
   산술 연산자를 사용 하시오.
      ㄱ. -12
      ㄴ. 75
      ㄷ. 25
      ㄹ. 5.4
      ㅁ. 3.0

문제2. 다음의 연산자를 보고 True와 False를 구분 하시오. 
      ㄱ. 7 > 18
      ㄴ. 5 < 2
      ㄷ. 6 % 3 > 2
      ㄹ. 5 + 5 != 2 * 5
      ㅁ. True == 1
      ㅂ. 1 == '1'
      ㅅ. 10 // 3 == 10 % 3
      ㅇ. 15 % 4 in (0, 1, 2)

문제3. input()으로 2개의 값을 받은 다음 더하기, 빼기, 곱하기, 나누기 연산을 
    하여 그 결과를 출력하는 코드를 작성하시오.

문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
    코드를 작성하시오.
    
    비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
    표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9

    출력 예제 : 홍길동님의 비만도는 112.15% 입니다.




# 문제 1.
num1, num2, num3 = 5, 15, 27

print(-(num3-num2))
print(num1 * num2)
print((num1*2) + num2)
print(num3/num1)
print(float(num2/num1))

# 문제 2.
# False
# False
# False
# False
# True
# False
# False
# Flase

# 문제 3.
num4 = int(input("첫번째 숫자 : "))
num5 = int(input("두번째 숫자 : "))
print("더하기",num4+num5)
print("뺴기",num4-num5)
print("곱하기",num4*num5)
print("나누기",num4/num5)

# 문제 4.

name = input("이름 : ")
height = float(input("키 : "))
weight = float(input("체중 : "))
stdWeight = (height-100)*0.9
bmi = (weight/stdWeight)*100


print("{}님의 비만도는 {:.2f}% 입니다.".format(name,bmi))
'''

#### 제어문 (if), 반복문 (for, while)
# 제어문 (if)


# 단순 if
#   사용형식 1
# if 조건식 :
#   실행문 (종속문장1)
#   실행문 (종속문장2)      => if 블럭
# 특징 : 조건식이 참일 경우에 종속 문장을 실행
#        파이썬에서는 다른 언어와 다르게 들여쓰기가 중요함.
#       들여쓰기를 가지고 블럭을 구분함...

'''
# [예제]
num = int(input("정수 입력 : "))
if num % 2 == 0:
    print("num 변수의 짝수 입니다.")
    print("num 변수의 값은 2의 배수입니다.")
print("if 다음 문장 실행")

# [예제]
print("1. Easy Game")
print("2. Hard Game")
print("3. Exit")
num = int(input("번호선택>> "))
if num == 1 :
    print("Easy Game Start")
if num == 2 :
    print("Hard Game Start")
if num == 3 :
    print("Game Exit")
    
# [예제]
x = 15
if x > 10 and x != 10:
    print("x변수의 값은 10도 크고, 10과 같지 않다.")
if x > 10 or x !=15;
    print("or는 둘 중 하나라도 참이면 참으로 결과를 반환")
    
# [예제]
su = int(input("1~10 사이의 정수를 입력하세요 : " ))
if su in (1, 4, 7):
    print("멤버에 있는 숫자입니다")
    
# if ~ else : if의 조건식이 참이면, if의 종속문장을, 그렇지 않으면 else의 종속문장을 실행
#   사용형식 1
# if 조건식 :
#   실행문 (종속문장1)
#   실행문 (종속문장2)      => if 블럭
# else :
#   실행문 (종속문장1)
#   실행문 (종속문장2)      => else 블럭 둘 다 합쳐 하나의 if문으로 처리



# [ IF 문 문제]

# 1. 입력한 데이터가 3의 배수인 경우 출력하시오
x = int(input("정수 입력 : "))
if x%3 == 0:
    print("입력한 수는 3의 배수입니다.")

# 2. 절대값을 구하는 프로그램을 작성하시오
x = int(input("정수 입력 : "))
if x >= 0:
    print("입력한 수의 절대값은 {} 입니다.".format(x))
else :
    print("입력한 수의 절대값은 {} 입니다.".format(-x))
    
# 3. 수를 입력 받아 짝, 홀수를 구분하여 출력하시오.
x = int(input("정수 입력 : "))
if x%2 == 0:
    print("입력한 수는 짝수입니다.")
else :
    print("입력한 수는 홀수입니다.")
    
#4. 두 수를 입력 받아 큰 수를 출력하시오.
x = int(input("첫번째 수 입력 : "))
y = int(input("두번째 수 입력 : "))
if x < y :
    print("두 수 중 큰 수는 {} 입니다.".format(y))
elif x == y :
    print("두 수는 같습니다.")
else :
    print("두 수 중 큰 수는 {} 입니다.".format(x))

#5. 세 수를 입력 받아 큰 수를 출력하시오.
x = int(input("첫번째 수 입력 : "))
y = int(input("두번째 수 입력 : "))
z = int(input("세번째 수 입력 : "))

if x > y :
    if x > z :
        print("세 수 중 큰 수는 {} 입니다.".format(x))
    else :
        print("세 수 중 큰 수는 {} 입니다.".format(z))
elif y > z :
    print("세 수 중 큰 수는 {} 입니다.".format(y))
else :
    print("세 수 중 큰 수는 {} 입니다.".format(z))
    
#6. 두 수를 입력 받아 큰 수가 짝수이면 출력하시오.
x = int(input("첫번째 수 입력 : "))
y = int(input("두번째 수 입력 : "))

if x > y and x%2 == 0 :
    print(x)
elif y%2 == 0:
    print(y)
    
#7. 두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.
x = int(input("첫번째 수 입력 : "))
y = int(input("두번째 수 입력 : "))

if (x+y)%6 == 0 :
    print(x+y)
    
    
# 중첩 if 구문 : if 구문 안에 if 구문을 사용하는 경우
# 다중 if 구문 : if ~ elif ~ else 구문으로 if와 elif 조건을 확인 부합되면 종속 실행
#                  만약 조건에 부합되지 않는 경우에는 else를 실행.
        
# [예제7] 중첩 if 구문
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))

Sum = num1 + num2


# [Quiz 1]
# - 사용자로부터 Gbyte의 값을 입력받아 byte,Kbyte,Mbyte로 각각 출력되게 만드시오.
# - (1.byte 2.Kbyte 3.Mbyte 선택)
# - 단위 1024

gbyte = int(input("Gbyte를 입력하세요 : "))
unit = int(input("단위를 선택하세요 : 1.byte 2.Kbyte 3.Mbyte : "))

if unit == 1 :
    print("{:,} byte".format(gbyte*1024**3))
elif unit == 2 :
    print("{:,} kbyte".format(gbyte*1024**2))
elif unit == 3 :
    print("{:,} Mbyte".format(gbyte*1024))
else :
    print("잘못 입력하셨습니다.")
    
# [Quiz2]
# - 인증 프로그램을 만드시오.
# 1. 아이디가 틀리면 등록되지 않은 아이디입니다. 출력
# 2. 비밀번호가 틀리면 비밀번호가 틀렸습니다. 출력
# 3. 아이디와 비밀번호가 일치한다면 인증 통과 출력

input_id = input("아이디를 입력하세요 : ")
input_pw = input("비밀번호를 입력하세요 : ")
old_id = "test"
old_pw = "python123"

if input_id == old_id :
    if input_pw == old_pw :
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다.")
else :
    print("등록되지 않은 ID입니다.")
'''

'''
## 삼항 조건문 : 삼항 연산자, 조건식이 참인 경우와 거짓인 경우 처리할 문장을 한 줄로 작성
# 조건식 비교 결과 따라 선택적으로 실행문이 동작합니다.
#
#   (형식)
#   변수 = 참 if (조건문) else 거짓

# 삼항 조건문 예제
# 1) 일반 조건문
num = 9
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2
print("result = ",result)

print("3항 연산자")
result2 = num * 2 if num >= 5 else num + 2
print ("result2 = ",result2)

'''
'''
문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
    코드를 작성하시오.
    
    비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
    표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9
    
    비만도가 100 미만인 경우 "저체중"
    비만도가 100~110 사이인 경우 "정상 체중"
    비만도가 110~120 사이인 경우 "과체중"
    비만도가 120~130 사이인 경우 "비만"
    그 이상인 경우에는 "고도비만"
    

    출력 예제 : 홍길동님의 비만도는 112.15%로 정상체중 입니다.
'''

name = input("이름 : ")
height = float(input("키 : "))
weight = float(input("체중 : "))
stdweight = (height-100) * 0.9
bmi = weight/stdweight*100


if bmi < 100 :
    result="저체중"
elif bmi < 110 :
    result="정상체중"
elif bmi < 120 :
    result="과체중"
elif bmi < 130 :
    result="비만"
else :
    result="고도비만"
    
print("{}님의 비만도는 {:.2f}%로 {} 입니다.".format(name,bmi,result))