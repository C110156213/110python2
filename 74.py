list1 = []
for i in range(1,11):
    list1 = input("依序輸入四個顏色（中間以空白間隔）：")
    if list1[0] == "red":
        a=1
    elif list1[0] == "blue" or "green" :
        a=2
    else:
        a=3 

    if list1[1] == "blue":
        b=1       
    elif list1[1] == "red" or "green" :
        b=2
    else:
        b=3
    
    if list1[2] == "red":
        c=1
    elif list1[2] == "blue" or "green" :
        c=2
    else:
        c=3

    if list1[3] == "green":
        d=1       
    elif list1[3] == "red" or "blue" :
        d=2
    else:
        d=3

    if a == b == c == d == 1:
        print("正確答案")
    else:
        print(a,b,c,d)