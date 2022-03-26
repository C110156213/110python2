import math


km = float(input("請輸入路程公里數(KM):"))
m = km*1000
if m <= 1500:
    print("所需車資為：75元")
else :
    b = (m-1500) %250
    if b == 0 :
        a = (m-1500) /250
        money = (a*5) + 75
        print("所需車資為：" , money , "元")
    else:
        a = math.ceil((m-1500) /250)
        money = (a*5) + 75
        print("所需車資為：" , money , "元")
    
