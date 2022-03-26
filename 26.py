while True :
    test = input("檢測的字串（end結束）：")
    if test == "end":
        break
    else:
        tt = input("檢測的單一字元：")
        c = test.count(tt)
        print("字元" , tt , "出現次數為：" , c)

