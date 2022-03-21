#2022.03.20 일요일

#[문제 1]
print("문제1")
su = 5
dan = 800
print(f"su 주소:{id(su)}")
print(f"dan 주소 :{id(dan)}")
print(f"금액 = {su * dan}")
print("")

#[문제 2]
print("문제2")
x = 2
y = (2.5*(x**2))+(3.3*x)+6

print(y)
[print("")]

#[문제 3]
fat = int(input("지방의 그램을 입력하세요 : "))
ch = int(input("탄수화물의 그램을 입력하세요 : "))
prot = int(input("단백질의 그램을 입력하세요 : "))
print("총 칼로리 : {:,} cal".format(fat*9 + prot*4 + ch*4))
