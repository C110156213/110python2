score = []
tatal = 0
ch = int(input("國文："))
score.append(ch)
en = int(input("英文："))
score.append(en)
ma = int(input("微積分："))
score.append(ma)
pe = int(input("體育："))
score.append(pe)
py = int(input("程式設計："))
score.append(py)

score.sort()

for i in score :
    total = total + score
ave = total/5
print("平均分數： %.2f" % ave)

if score[-1] == ch :
    print("最高分科目：國文" , score[-1] , "分")
elif score[-1] == en :
    print("最高分科目：英文" , score[-1] , "分")
elif score[-1] == ma :
    print("最高分科目：微積分" , score[-1] , "分")
elif score[-1] == pe :
    print("最高分科目：體育" , score[-1] , "分")
elif score[-1] == py :
    print("最高分科目：程式設計" , score[-1] , "分")

if score[0] == ch :
    print("最低分科目：國文" , score[0] , "分")
elif score[0] == en :
    print("最低分科目：英文" , score[0] , "分")
elif score[0] == ma :
    print("最低分科目：微積分" , score[0] , "分")
elif score[0] == pe :
    print("最低分科目：體育" , score[0] , "分")
elif score[0] == py :
    print("最低分科目：程式設計" , score[0] , "分")




