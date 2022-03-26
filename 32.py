money = int(input("小明身上有幾元："))
kind = int(input("販賣機有幾種飲料："))


for i in range (0,kind):
    mm = int(input())
    if money >= mm :
        ok = ok+1

print(ok)