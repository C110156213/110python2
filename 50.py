allst = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
en = set(['John','Mary','Fiona','Claire','Ben','Bill'])
ma = set(['Mary','Fiona','Claire','Eva','Ben'])
a1 = (allst-ma)


print("英文與數學都及格" , ma&en)
print("數學不及格", allst-ma)
print("英文及格且數學不及格", en&a1)