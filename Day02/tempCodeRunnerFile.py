gbyte = int(input("Gbyte를 입력하세요 : "))
unit = int(input("단위를 선택하세요 : 1.byte 2.Kbyte 3.Mbyte : "))

if unit == 1 :
    print("{,}byte".format(gbyte*1024*1024*1024))
elif unit == 2 :
    print("{,}kbyte".format(gbyte*1024*1024))
elif unit == 3 :
    print("{,}Mbyte".format(gbyte*1024))
else :
    print("잘못 입력하셨습니다.")