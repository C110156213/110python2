n1 = str(input("請輸入第一組數字："))
n2 = str(input("請輸入第二組數字："))
count = len(n1)
b=0
a=0

for i in range(0,count+1):
    if n2[i] in n1 :
        b = b+1

for j in range(0,count+1):
    if n2[j] == n1[j]:
        a = a+1

if a == count and b == 0:
    print(a,"A",b,"B 全對")
else:
    print(a,"A",b,"B 加油")


