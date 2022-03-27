m = int(input("請輸入階層值M:"))
i = 1
n = 1
while n <= 1000:
    n=0
    i = i+1
    for i in range(1,i+1):
        n = (i-1)*i

print("超過M為" , m ,"的最小階層值為：" , i)
