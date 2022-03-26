main = str(input("請選擇請選擇主餐及升級的套餐："))
a = str(input("是否升級成大杯的套餐："))
b = str(input("是否換成大薯："))
money = 0

if a == "是":
    money = money +7
if b == "是":
    money = money +13

if main[0] == "1":
    money = money +72
    if main[1] == "A":
        money = money +55
    else :
        money = money +68
elif main[0] == "2":
    money = money + 62
    if main[1] == "A":
        money = money +55
    else :
        money = money +68
elif main[0] == "3":
    money = money + 82
    if main[1] == "A":
        money = money +55
    else :
        money = money +68
elif main[0] == "4":
    money = money + 44
    if main[1] == "A":
        money = money +55
    else :
        money = money +68
elif main[0] == "5":
    money = money + 60
    if main[1] == "A":
        money = money +55
    else :
        money = money +68

print("總共為：" , money ,"元")