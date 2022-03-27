llist =[]
while True:
    things = str(input("請輸入事項（若已無事項，請輸入end）："))
    if things == "end":
        break
    llist.append(things)
n = len(llist)
for i in range(1,n+1):
    print(i,".",llist[i-1])
