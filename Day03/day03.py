'''
[문제1]
윤년을 구하는 코드를 작성
4의 배수는 윤년, 외에는 평년
4의 배수면서 100의 배수는 평년, 외에는 윤년
100의 배수이면서 400의 배수인 경우에는 윤년, 그 외에는 펴연


year = int(input("연도를 입력하세요 : "))

if year%4 == 0 :
    if year%100 == 0 :
        if year%400 == 0 :
            print(f"{year}년은 윤년입니다.")
        else :
            print(f"{year}년은 평년입니다.")
    else : 
        print(f"{year}년은 윤년입니다.")
else :
    print(f"{year}년은 평년입니다.")


[문제2]
이름, 학번, 3과목의 성적을 입력받아 합계와 평균을 구하고
평균이 90 이상이면 'A', 80 이상 'B', 70 이상 'C', 60 이상 'D', 60미만이면 'F'를 출력


name = input("이름 : ")
no = input("학번 : ")
kor = int(input("국어 성적 : "))
eng = int(input("영어 성적 : "))
math = int(input("수학 성적 : "))

sum = kor+eng+math
avg = sum/3

if avg >= 90 :
    print("A")
elif avg >= 80 :
    print("B")
elif avg >= 70 :
    print("C")
elif avg >= 60 :
    print("D")
else :
    print("F")
    
    

[문제3]
커피의 개당 가격 2000원, 10개 초과시 초과양에 대해 개당 1500원
커피의 갯수를 입력 받아 금액을 출력


price = 2000
amount = int(input("몇 잔을 사시겠습니까? "))

if amount > 10 :
    total = 20000 + (amount-10)*1500
else :
    total = amount*2000
    
print(f"총 가격은 {total}원 입니다.")


[문제4]
정수를 입력 받아 아래와 같이 출력하시오
-3의 배수이면서, 4의 배수입니다.
-3의 배수 입니다.
-4의 배수 입니다.
-3의 배수도, 4의 배수도 아닙니다.
-0은 3의 배수도 4의 배수도 아닙니다.

num = int(input("정수를 입력하세요 : "))

if num == 0 :
    print("0은 3의 배수도 4의 배수도 아닙니다.")
elif num%3 and num%4 == 0 :
    print(f"{num}은 3의 배수이면서, 4의 배수입니다.")
elif num%3 == 0 :
    print(f"{num}은 3의 배수 입니다.")
elif num%4 == 0 :
    print(f"{num}은 4의 배수 입니다.")
else :
    print(f"{num}은 3의 배수도, 4의 배수도 아닙니다.")
    


반복
(형식)
for 변수명 in range(반복횟수):
    종속문장1(for)
    종속문장2(for)
(메인 프로그램 실행 코드 진행)   


for i in range(10) :
    print("A",i)
    
# range(시작값, 끝값, 증감값) : 파이썬의 내장 함수

#사용법 (range())

#   1. range(종료값)    #시작값 0, 증감값 +1 기본값으로 생략
#       : 0부터 시작해서 종료값 이전까지의 값의 범위를 가짐.
#   ex) range(10)   =>  {0,1,2,3,4,5,6,7,8,9}

#   2. range(시작값, 종료값)
#       : 시작값부터 종료값 이전까지의 값의 범위
#   ex) range(5,10)     => {5,6,7,8,9}

#   3. range(시작값, 종료값, 증감값)
#       : 시작값부터 종료값 이전까지 값의 증/감값 간격의 값 범위
#   ex) range(0,10,2)   =>  {0,2,4,6,8}
#       range(10,0,-2)  =>  {10,8,6,4,2}

# range(종료값) 예제
for x in range(10): #{0,1,2,3,4,5,6,7,8,9} , 초기값 : 0, 증가값 : 1, 조건식 : x < 10
    print (x, end= ' ') # print()의 end인자값 설정하면 출력후
                        # 마지막에 사용될 문자를 지정할 수 있음.
                        # 사용 : end='문자열'
print()

# 예제 2) for문(range(시작값, 종료값))                        
for x in range(5,10):   # {5,6,7,8,9}, 초기값 : 5, 증가값 : 1, 조건식 : x < 10
    print(x,end=' ')
print() # "\n" 문자를 출력하기 위해서

# 예제 3) for문(range(시작값, 종료값, 증감값)) - 증가값
for x in range(0,10,2): # {0,2,4,6,8}, 초기값 : 0, 증가값 : +2, 조건식 : x < 10
    print(x,end=' ')
print()

# 예제 4) for문(range(시작값, 종료값, 증감값)) - 증감값
for x in range(10,0,-2): # {10,8,6,4,2}, 초기값 : 10, 증감값 : -2, 조건식 : x > 0
    print(x,end=' ')
print()

# 예제 5) for문 - 문자열
Sum = 0
for x in 'string':  #{'s','t','r','i','n','g'}
    print(x,end=' ')
    Sum += 1
print(); print(Sum)

# 예제 6) for문 - list, tuple, dictionary ...
i = 0
for x in [1,4,78,'test','A',1.80,100]:
    print(x,end = ' ')
    i += 1
print("\n",i,"번 반복함")

# .예제 7) 이중 For 구문 : for 구문을 중첩해서 사용하는 것
Sum = 0
for x in range(10): #상위 for 문
    for y in range(10): #하위 for문
        Sum += 1    # Sum = Sum + 1
print(Sum)

#중첩 For 문 (이중 For 문)은 상위 For 문 한 번 실행할 때에
#하위 For문은 자신에게 주어진 반복 횟수 만큼 실행.
# (하위 For 문은 상위 For문의 종속문장이기 때문)
# 이런식으로 반복하기 때문에 위 예제에서 Sum이 100번 동작하고,
# 결과가 100이 되는 것임 (상위 1회가 하위 10회인 경우)

# (형식)
# for x in range(반복횟수) :
#      for y in range(반복횟수):
#           종속문장1(하위 For문)
#           종속문장2(하위 For문)
#       종속문장3 (상위 for문)
# (메인 실행 코드)

# 예제 8) 이중 For 문 예제
Sum = 0
for x in range(1,5,3): #[1,4] 값으로 두 번 반복함 -> 초기값 : 1, 증가값 : 3, 조건식 : x < 5
    for y in range(5,0,-1): #[5,4,3,2,1] 값으로 5번 반복함
        print("{} 상위 for문의 x의 값, {} 하위 for 문의 y의 값"
              .format(x,y))
        Sum += 1
print(Sum,"횟수 만큼 반복함 !!!")


# 문제 1) 중첩 FOr문을 이용하여 구구단 표를 작성
# (출력 예시)
# 2 x 1 = 2
# 2 x 2 = 4
# ...

for x in range (1,10):
    print("{} x {} = {}".format(2,x,2*x))


# 문제 2) 중첩 For 문을 이용하여 구구단 표를 작성
# 2 x 1 =2  3 x 1 = 3   4 x 1 = 4   5 x 1 = 5   6 x 1 = 6
# 2 x 2 =4  3 x 2 = 6   ...

for x in range (1, 10):
    for y in range (2, 10):
        print("{} x {} = {}".format(y,x,x*y), end='\t')
    print()


# 문제 3) 다음과 같이 출력되게 For문을 작성하세요
# 상위 For 문이 0 일때, 하위 FOr 문 : 0 0 0 0 0
# 상위 For 문이 1 일때, 하위 For 문 : 0 1 2 3 4
# 상위 For 문이 2 일때, 하위 For 문 : 0 2 4 6 8
 
for x in range (5) :
    for y in range (5) :
        print("{}".format(x*y),end=' ')
    print()



# 문제 4) 이중 For문을 사용하여 다음과 같이 출력되게 하세요
# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15

result = 0
for x in range (5) :
    for y in range (5) :
        result += 1
        print(result, end='\t')
    print()
    



# 문제 5)

result = 26
for x in range (5) :
    for y in range (5) :
        result -= 1
        print(result, end='\t')
    print()

print()
    
# 문제 6)

for x in range (5) :
    result = x
    for y in range (5) :
        print(result%5+1,end='\t')
        result += 1
    print()
    
    
# while 구문
# : 조건식이 참인 경우에 반복하는 반복문

# (형식)
# while (조건식):
#   종속문장1
#   종속문장2
# (메인 프로그램 코드 실행)

# 예)
# while x<10 :
#   종속문장1
#   종속문장2
#   x = x + 1   # X += 1 => 조건식에 변화를 주는 값이 필요함.
# (메인 프로그램 코드 실행)

# 예제1)
i = 1
odd_sum = 0
even_sum = 0
while i <= 10:  #조건식
    if i%2==0:
        even_sum += i
    else:
        odd_sum += i
    i += 1 # i = i + 1  #증감식
print("짝수의 합 : {}, 홀수의 합 : {}".format(even_sum,odd_sum))

# while ~ else를 사용 : whle의 조건이 False가 되는 경우에 else가 실행됨.
i = 0
while i < 5:
    print("{}번 종속문장 실행".format(i))
    i += 1
else:
    print("조건식이 거짓인 경우에 실행 문장")
print("메인 프로그램 실행 코드")

# while의 무한 반복
# : while 구문의 조건을 항상 참이 되게 설정한 후에 반복문 내에
# 제어를 위한 명령어를 실행하는 반복 구문
# 제어를 실행하는 명령어 (반복문에 대한 제어)
# 1. break => 반복의 종료
# 2. continue => 반복시 조건문으로 이동

#(형식)
# while True:
#   종속문장1
#   종속문장2
#   (종료하기 위한 조건과 명령어 : break)
# 위와 같은 코드에서는 break를 사용하지 않으면 무한반복함
# 무한히 반복되면서 다음으로 코드 진행되지 않기 때문에 정지한 것
# 같이 보이게 됨. 때문에 반복에서 벗어나기 위해ㅔ서
# "break" 명령어를 적절히 사용해야 함.

#(break 사용 예)
# while True:
#   종속문장1
#   break
#   종속문장2
#(메인 프로그램 코드)

# 프로그램 흐름 : 1) while의 조건식 2) 종속문장1 3) break
#                4) 메인 프로그램 코드

#(continue 사용 예) => 반복문 종료는 아님. 조건식으로 이동

#while True:
#   종속문장1
#   continue
#   종속문장2
#   (메인 프로그램 코드)

#  프로그램 흐름 : 1) while의 조건식 2) 종속문장 1 3) continue
#                 4) while의 조건식 5) 종속문장 1 6) continue
#                 7) while의 조건식...
#   종속문장2는 실행하지 않음

#예제2) break와 continue의 사용 예제
# break 이용
while True:
    a = int(input("정수 입력[0 입력시 종료] : "))
    if a == 0:
        break
    print("입력값 출력 : ",a)
    
# continue 이용
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print("a = {}".format(a))
'''

# 문제1)
# 살 100통이 저장되어 있는 창고에 암수 1 쌍의 쥐가 있습니다.
# 쥐 한 마리가 하루 20g씩 쌀을 먹고 있습니다.
# 10일마다 쥐의 수가 2배씩 증가하고 있다면,
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까?
# 또, 이 때에 쥐는 총 몇 마리가 되어 있을까?
# (쌀 한통은 1kg, 쥐는 쌀을 먹은 후 2배로 증가하는 조건)

rice = 100000
mouse = 2
day = 0

while rice > 0 :
    rice -= (mouse*20)
    day += 1
    if day%10 == 0:
        mouse *= 2
print(day,mouse)    


# 문제2) 1~100 까지의 합

i = 1
sum = 0
while i < 101:
    sum += i
    i += 1     
print(sum)

# 문제3) 1부터 1씩 증가하는 값에 대해 누적합을 구할 때 10,000보다 큰 누적합 값에 대해
#           마지막 더해진 값이 얼마인지 구하시오      

i = 1
sum = 0
while sum < 10000 :
    sum += i
    i += 1
print(i)

# 문제4) 1부터 100 사이의 소수를 출력하고 갯수를 구하시오

count = 0
for x in range(2,101) :
    flag = True     # flag가 True면 소수 - 2진 알고리즘, flag기법
    ## 소수 판별
    for y in range(2,x):
        if x % y == 0:
            flag = False
            break   # for문에 대한 break
    if flag:
        print(x,end=' ')
        count += 1
print()
print(f"1 ~ 100 사이에 소수의 갯수는 {count}개 입니다.")