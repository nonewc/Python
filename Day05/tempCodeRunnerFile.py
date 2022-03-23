#k fromkeys(iter,value)
ke = ['a','b','c','d']
dic1 = {}.fromkeys(ke)          # {'a':None, 'b':None, 'c': None, 'd' : None}
dic2 = {}.fromkeys(ke,1)        # {'a' : 1,}
print(dic1)
print(dic2)