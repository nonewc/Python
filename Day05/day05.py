'''
# count(value) : 특정 값의 개수를 출력
lst1 = [1,2,3,2,5,6,2,8]
su = lst1.count(2)
print(lst1)
print("2의 값을 가진 멤버의 개수 : ", su)

# index(value) : 특정 값의 인덱스 값을 반환
lst1 = [1,2,3,2,5,6,2,8]
idx = lst1.index(2)
print("idx의 값을 확인 : ",idx)

# reverse() : 리스트 멤버의 순서를 반전 (정렬X)
lst1 = [ 9, 10, 3, 2, 6, 1, 7, 8, 4, 5]
print("reverse() 사용전 : ",lst1)
lst1.reverse()
print("reverse() 사용후 : ",lst1)

# sort() : 리스트를 정렬하는 함수
#       -오름차순(작은 -> 큰) => reverser=False(생략: 기본값)
#       -내림차순(큰 -> 작은) => reverse=True
lst1.sort() # 오름차순 정렬
print("lst1을 오름차순 정렬 : ",lst1)
lst1.sort(reverse = True)
print("lst1을 내림차순 정렬 : ",lst1)

# sort 사용시 주의사항
# 1. 숫자 형식 또는 문자 형식은 분리해서 정렬해야 한다.
# 2. 정수와 실수는 같은 숫자이기 때문에 정렬이 가능하다.

# 3. 정렬된 리스트를 새롭게 만들고 싶은 경우, sorted()를 사용
lst2 = sorted(lst1)
print(lst1,lst2)
lst3 = sorted("I am a student".split())
print(lst3)     # ['I','a','am','student'], ASCII 기준 정렬
lst4 = sorted("I am a student".split(),key=str.lower)
print(lst4)     # ['a','am','I','student']

# split() 문자열을 분리하는 함수
# "()" 안에 아무것도 넣어주지 않으면, 공백(스페이스, 탭, 엔터 등)을
# 기준으로 문자열을 나눠서 사용함. 만약 split(";")을 사용하면
# ";"을 기준으로 문자열을 나누겠다는 의미

# Copy 기능
#   -shallow copy : 서로 다른 변수가 같은 위치에 있는 데이터를 가르키는 경우
#   -deep copy : 두개의 변수가 별도의 공간을 가리키는 경우

print("lst1의 값 : ",lst1,"\tlst1의 주소 값 : ",id(lst1))
print("lst1의 값 : ",lst1,"\tlst1의 주소 값 : ",id(lst2))
lst1[1] = 'a'
print(lst1)
print(lst2)

# (예) deep copy
lst1 = [1,2,3,4,5]
lst2 = list(lst1)       # list() 는 새로운 리스트를 생성하는 메서드
lst1[1] = 'a'
print(lst1,id(lst1))    #[1, 'a', 3, 4, 5] 1624342020864
print(lst2,id(lst2))    #[1, 2, 3, 4, 5] 1624342073600

#복사기능을 제공하는 copy 모듈을 불러서 사용
import copy

lst1 = [1,2,3,4,5]
lst2 = copy.deepcopy(lst1)  # deep copy
lst3 = lst1                 # shallow copy
print(lst1,lst2)
print(id(lst1),"\t",id(lst2),"\t",id(lst3))     #2808170614912    2808170615808   2808170614912
lst2[0] = 100
print(lst1,lst2)


#[ Quiz 1 ] : 리스트 초깃값 [ 30, 20, 10 ] 설정 후
# 아래와 같이 출력되도록 코드를 작성

# 현재 리스트 : [30, 20, 10]
# append(40) 후의 리스트 : [30, 20, 10, 40]
# pop() 으로 추출한 값 : 40
# pop() 후의 리스트 : [30, 20, 10] 
# sort() 후의 리스트 : [10, 20, 30]
# reverse() 후의 리스트 : [30, 20, 10]

lst1 = [30, 20, 10]
print("현재 리스트 : ",lst1)
lst1.append(40)
print("append(40) 후의 리스트 : ",lst1)
print("pop()으로 추출한 값 : ",lst1.pop())
print("pop()후의 리스트 : ",lst1)
lst1.sort()
print("sort()후의 리스트 : ",lst1)
lst1.reverse()
print("reverse()후의 리스트 : ",lst1)

#[ Quiz 2 ] : 리스트 초깃값 [ 30, 20, 10 ] 설정 후
# 아래와 같이 출력되도록 코드를 작성

lst2 = [30, 20, 10]
print("10 값의 위치 : ",lst2.index(10))
lst2.insert(2, 200)
print("insert(2,200) 후의 리스트 : ",lst2)
lst2.remove(200)
print("remove(200) 후의 리스트 : ",lst2)
lst2.extend([555,666,555])
print("extend([555,666,555])후의 리스트 : ",lst2)
print("555 값의 개수 : ",lst2.count(555))

# 2차(원) 리스트
#   : 리스트 안에 멤버 중에 리스트가 존재하는 경우 사용되는 방식
#     리스트 안에 있는 리스트 멤버에 대한 참조 방식

aa = [ [1,2,3,4], # aa[0]
       [5,6,7,8], # aa[1]
       [9,10,11,12]] # aa[2]
    # aa 리스트의 멤버의 개수 : 3
    
print(len(aa))
print(aa)
for x in range(len(aa)):            # aa리스트의 멤버수 : 3
    for y in range(len(aa[x])):     # aa 멤버 리스트의 멤버의 갯수 : 4
        print(aa[x][y], end='\t')
    print()

# 예제 2) 2차 리스트 생성 및 출력
ls_1 = [] ; ls_2 = []; value= 1
# 2차 리스트 생성
for i in range(3):  #상위 리스트의 멤버 갯수
    for j in range(4):  #하위 리스트(멤버)의 멤버 갯수
        ls_1.append(value)
        value += 1
        # 1. ls_1 [1,2,3,4]
        # 2. ls_1 [5,6,7,8]
        # 3. ls_1 [9,10,11,12]
    ls_2.append(ls_1)   # 1. ls_2, [[1,2,3,4]]
                        # 2. ls_2, [[1,2,3,4],[5,6,7,8]]
                        # 3. ls_2, [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ls_1 = []
print(ls_2) # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 출력(읽기)
for x in range(len(ls_2)):            
    for y in range(len(ls_2[x])):     
        print(ls_2[x][y], end='\t')
    print()
    


# 문제1) numbers = [10,20,30,40,50,60,70]
# 위 리스트의 모든 값을 더한 결과를 출력하세요.

numbers = [10,20,30,40,50,60,70]
sum = 0

for x in range(len(numbers)):
    sum += numbers[x]
print(sum)

# 문제2) 1~45 까지 임의의 중복 없이 6개 생성하여 출력
import random

lst1 = []
value = random.randint(1, 45)

for x in range(6):
    while(value in lst1):
        value = random.randint(1,45)
    lst1.append(value) 
print(lst1)
        
# 문제3) lst_sec = [['홍길동','남',36],['김수양','여',32],['박담수','남',28]]
lst_sec = [['홍길동','남',36],['김수양','여',32],['박담수','남',28]]

for x in range(len(lst_sec)):
    print("이름 : ",lst_sec[x][0])
    print("성별 : ",lst_sec[x][1])
    print("나이 : ",lst_sec[x][2])
    print()

# 문제4) 구구단을 출력하는 코드를 작성하되, 2차 리스트에 결과값을 저장하고 출력할 수 있도록 하시오.

lst2 = []
lst2_1 = []

for x in range(2,10):
    for y in range(1,10):
        lst2_1.append("{} x {} = {}".format(x,y,x*y))
    lst2.append(lst2_1)
    lst2_1 = []

print(lst2)


### list 내포 (List Comprehension) : 리스트 안에서 for와 if를 사용하는 문법

# 형식1 (for)
#   변수 = [실행문 for 변수 in 열거형객체]
#   for문의 실행결과가 변수 리스트에 append 처리가 됨.

x = [2,4,1,5,7]
lst = []
for i in x :
    i ** = 2
    lst.append(i)
print(lst)

# 형식 1
lst1 = [i**2 for i in x]    # x열거형자료(list)의 멤버들을 i**2한 처리 결과로 append
print(lst1)



# 형식 2 (for와 if를 같이 사용하는 경우)
#   변수 = [실행문 for 변수 in 열거형객체 if 조건문]

# 형식 2 : 1 ~ 10 -> 2의 배수 추출 -> i*2 -> list에 저장
num = list(range(1,11))     # num 리스트 [1,2,3,4,5,6,7,8,9,10]

lst2 = [i*2 for i in num if i%2 == 0]
print(lst2)


lst_f = []
flag = True

while(flag):
    print("1. 친구 리스트 출력","2. 친구 추가","3. 친구 삭제","4. 이름 변경","0. 종료",sep='\n')
    menu = int(input("메뉴를 선택하세요 : "))

    if menu == 1:
        print(lst_f)
    elif menu == 2:
        value = input("등록할 이름을 입력하세요 : ")
        lst_f.append(value)
        print("입력이 완료되었습니다.")
        continue
    elif menu == 3:
        value = input("삭제할 이름을 입력하세요 : ")
        lst_f.remove(value)
        print("삭제가 완료되었습니다.")
        continue
    elif menu == 4:
        value = input("어떤 이름을 변경하시겠습니까 : ")
        if (value in lst_f):
            value2 = input("변경할 이름을 입력하세요 : ")
            lst_f[lst_f.index(value)] = value2
        else :
            ("잘못된 입력입니다.")
            continue
    elif menu == 0:
            print("종료")
            flag = False
print("프로그램 종료")


# 튜플(tuple)
# : 리스트와 비슷한 자료형으로 튜플 안에 다양한 형태의 값을 사용할 수 있음.

# (형식)
# 튜플 변수명 = (value1,value2,value3,...)

# 리스트와 튜플의 차이점
#   1. 리스트는 "[]"를 사용하지만, 튜플은 "()"을 사용한다.
#   2. 리스트는 그 값을 생성, 삭제, 수정이 가능하지만
#       튜플은 그 값을 바꿀 수 없음(중요)
#   3. 튜플은 멤버(요소)의 값이 1개인 경우 반드시 뒤에 ","를 붙여야 한다.
#       예) tu = (1,) , tu = (1)
#   4. 튜플은 가장 외곽에 있는 "()"는 생략이 가능함.
#        예) tu = 10,20,30

# 튜플의 인덱싱
# : 튜플도 리스트와 같이 인덱싱을 통해서 값에 접근

# 예)
#   인덱스 값 (+) 0 1 2 3 4 5 6 7 8
#   인덱스 값 (-)-9-8-7-6-5-4-3-2-1
#      튜플     (1,2,3,4,5,6,7,8,9)

# 튜플의 슬라이싱(slicing)
# : 튜플의 특정 범위에 값에 접근하기 위한 방법으로 리스트와 동일하게 사용

tu1 = '문자열',100,123,456  # () 생략가능
print(tu1,type(tu1))        #('문자열', 100, 123, 456) <class 'tuple'>
tu2 = (10)      
print(tu2,type(tu2))        # 10 <class 'int'>
tu3 = (10,)
print(tu3,type(tu3))        # (10,) <class 'tuple'>
tu4 = 10,
print(tu4,type(tu4))        # (10,) <class 'tuple'>

# 예제2) 튜플의 특징
tu = (1,2,3,4,5)
#tu[0] = 100        # 튜플은 멤버를 변경할 수 없다.
print(tu)

# 튜플의 결합1(병합)
a = 1,2,3
b = 4,5,6
c = a+b
print(c)

# 튜플의 결합2(확장)
tu1 = 10,20,30
tu2 = 40,50,60
tu1 = tu1 + tu2 # tu1 += tu2

#packing과 unpacking
# : 튜플과 같은 자료형으로 묶어서 사용하는 것을 packing,
#  반대로 묶여진 튜플과 같은 자료형을 나눠서 사용하는 것을 unpacking

# 예) (1,2),(3,4)
# packing => pack = ((1,2),(3,4))
# unpacking => a,b = pack   # a=(1,2) , b = (3,4)
pack = 10,20,30
a, b, c = pack  # unpacking
print(a,b,c)
lst = [100,200,300]
a, b, c = lst
print(a,b,c)
st = 'abc'
a,b,c = st
print(a,b,c)


# print(help('tuple'))
# 튜플의 함수
# -index(value) : 튜플에 있는 값에 해당하는 멤버의 인덱스 값을 반환
# -count(value) : 튜플에 있는 값의 개수를 반환

# 예제4
tu = (100,200,'함수',100,'개수')
#      0   1    2    3    4
print(tu.index(200))       #1
print(tu.index(100))       #0
print(tu.count(100))       #2
'''


# (문제)
# 1. numbers = (10,20,30,40,50,60,70)
# 위 튜플 자료에서 30과 40을 따로 num1, num2 변수에
# 할당하시오.

numbers = (10,20,30,40,50,60,70)
num1 = numbers[2]
num2 = numbers[3]
print(num1,num2)

# 2. menu = (('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))
# 위 자료의 값을 다음의 양식처럼 출력하시오.
# 칼국수 - 6000 원
# 비빔밥 - 5500 원
# 돼지국밥 7000 원

menu = (('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))

for i in range(len(menu)) :
    print("{} - {}원".format(menu[i][0],menu[i][1]))
    
    
# [ Tuple 종합 문제 ]
# 1. 여러 개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 출력 하시오. (5개 값 저장)
#   ( Tuple의 값을 리스트에 저장하시오. 단, Len함수를 이용 )

# 2. 아래와 같이 출력 시키시오
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자','Galaxy','100원','미정']
print("-"*40)
print(" "*5,"(Tuple)\t\t(List)")
for i in range(len(tu)):
    print(" "*5,"{}\t\t{}".format(tu[i],lst[i]))
print("-"*40)

# 3. 위에서 출력한 내용을 업데이트 하시오.
# [단, Index, Insert, Remove 함수를 전부 사용할 것 ]
# 가 격 : 100 -> 110
# 출시일 : 미정 - > 이번 달 말
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자','Galaxy','100원','미정']
price = lst.index("100원")
out = lst.index('미정')
lst.remove("100원")
lst.remove("미정")
lst.insert(price,"110원")
lst.insert(out,"이번 달 말")
print("-"*40)
print(" "*5,"(Tuple)\t\t(List)")
for i in range(len(tu)):
    print(" "*5,"{}\t\t{}".format(tu[i],lst[i]))
print("-"*40)

#딕셔너리 (Dictionary)
# 1.List와 비슷한 자료형. List는 요소(멤버)에 대한 접근시 첨자(Index)를 사용
# 2. 딕셔너리도 첨자를 사용한다. 사용하는 첨자는 "key"
# 3. 딕셔너리는 key가 가리키는 곳에 값(value=데이터)이 존재함.
#   key 값을 사용하는 장점:
#           1) 빠른 탐색
#           2) 사용이 편리
# 4. 딕셔너리를 정의할 때는 "{}"를 사용함.
# 5. 특정 슬롯에 대해서 참조할 때에 key-value를 입력하거나
#    딕셔너리 안에 있는 요소를 참조할 경우에 "[]"를 사용한다.

# (형식)
#   변수명 = {} # 비어있는 딕셔너리 선언
#   변수명 = {key1:value1,key2:value2,key3:value3 ...}

# dict()를 이용해서 선언하는 경우,
# 변수명 = dict([(k1,v1),(k2,v2),(k3,v3),...])

# (접근방식)
# dic = {key:value}
# dic[key] = value1
# print(dic[key]) => value1

print(dict([('a',100),(1,'test')]))
dic = {'a':100,1:'test'}
print(dic['a'])     #100
print(dic[1])       #'test'

# 예제 1) 딕셔너리에 대한 정의 및 접근방법
dic = {'a':1,'b':2,'c':3}
print(dic['c'])
dic['c'] = 5*dic['b']
print(dic['c'])
dic['d'] = 100
print(dic)

# 예제 2) 딕셔너리에 for문을 사용하는 경우
for k in dic:   # 딕셔너리 자료형을 이용한 for문에서는 변수는 "key"갑을 지정 !!
    print(k)
    print("키값 : {}, 키를 이용한 참조값 : {}".format(k,dic[k]))
    
# 예제 3) 딕셔너리와 리스트를 같이 사용하는 경우(딕셔너리안에 값을 리스트로 사용)
dl = {'음료' : ['탄산','과일','우유','물'],
      '식사' : ['김밥','라면','돈까스','비빔밥']}

for key in dl:
    print(dl[key])
    for i in dl[key]:
        print(i,end=' ')
    print()
    for j in range(4):
        print(dl[key][j],end=' ')
    print()

# 예제 4) 리스트 안에 딕셔너리가 있는 경우
ld=[{'name':"홍길동",'age':18,'blood':'A'},
    {'name':"이방원",'age':24,'blood':'B'}]
for dic in ld:
    print(dic['name'],dic['age'],dic['blood'])

# 예제 5) 딕셔너리 안에 딕셔너리가 있는 경우
dd={'홍길동':{'age':18,'blood':'A'},
    '이방원':{'age':24,'blood':'B'}}
for name in dd:
    print(name,dd[name]['age'],dd[name]['blood'])
    

# 딕셔너리에서 사용되는 함수들
#   -update(dict) : 사전형 자료에 값을 추가 (key:value)
#   -fromkeys(iter[,value]) : iter에 리스트, 튜플의 값을 딕셔너리의 키로 사용하는 딕셔너리를 생성하여 반환
#   -get(key[,value]) : 사전형의 키를 사용하여 값을 얻어오는 함수
#   -keys() : 사전형 자료에서 모든 키를 반환하는 함수
#   -values() : 사전형 자료에서 모든 값을 반환하는 함수
#   -items() : 사전형의 모든 "키(key):값(value)"의 쌍으로 튜플로 반환
#   -pop(key) : 사전형 자료의 키를 통해서 값을 반환한 후에 삭제
#   -popitem() : 사전형 자료의 마지막 "키:값" 쌍을 튜플로 반환 후 삭제
#   -clear() : 사전형의 모든 "키:값"을 삭제하여 빈 사전형 자료로 만듦.    

# update()
dic = {'a':1, 'b':2, 'c':3}
dic.update({'d':4})
print(dic['a'])
print(dic['d'])
print(dic)

#k fromkeys(iter,value)
ke = ['a','b','c','d']
dic1 = {}.fromkeys(ke)          # {'a':None, 'b':None, 'c': None, 'd' : None}
dic2 = {}.fromkeys(ke,1)        # {'a': 1, 'b': 1, 'c': 1, 'd': 1}
print(dic1)
print(dic2)

# get(key[,value]) **
dic = {'a':1,'b':2,'c':3}
value = dic.get('b')
print(value)
print(dic.get('d'))

# keys()
dic = {'a':1,'b':2,'c':3}
for key in dic.keys() :
    print(key,end=' ')
print(type(dic.keys()))
print(dic.keys())
print()

# values()
dic = {'a':1,'b':2,'c':3}
for values in dic.values():
    print(values,end=' ')
print()
print(dic.values())

# items()
dic = {'a':1,'b':2,'c':3}
for key,value in dlc.items():   # unpacking
    print("{}:{}".format(key,value),end="\t")
print()

# pop(key)
dic = {'a':1,'b':2,'c':3}
value = dic.pop('b')
print(value)
print(dic)

# popitem()
dic = {'a':1,'b':2,'c':3}
tu1 = dic.popitem()
print(dic)
print(tu1)

#clear()
dic = {'a':1,'b':2,'c':3}
print(dic)
dic.clear()
print(dic)

# <<문제>>
# 1. 이름, 전화번호, 이메일, 주소를 키로 사용하는 사전 자료를 생성하시오

# 2. 리스트형 변수에 1번 문제와 같은 사전 자료가 여러개 생성될 수 있게
#   하시오.(입력값을 받아서 자료를 생성)

# 3. 2번에서 입력한 자료가 출력될 수 있도록 하시오.
#    (출력예시)
#    이름 : 홍길동
#    전화번호 : 010-xxxx-xxxx
#    이메일 : xxxx@xxx.com