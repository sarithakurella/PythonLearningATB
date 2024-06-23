= {1,2,3,4,5,6,7}
set2 = {2,4,7,8,9,10,11}
myset1 = set1.union(set2)
print(myset1)
myset2 = set1.intersection(set2)
print(myset2)
myset3 = set1.difference(set2)
print(myset3)
myset4 = set2.difference(set1)
print(myset4)
myset5 = set1.issubset(set2)
print(myset5)
set3={2,5,4}
print(set3.issubset(set1))