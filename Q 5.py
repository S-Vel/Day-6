#removing intersection of 2nd set from 1st set:
print("removing intersection of 2nd set from 1st set:")
s1 = {1,2,3,4,5}
s2 = {2,3,8,6,4}
print("original set:")
print(s1,"\n",s2)

s1.difference_update(s2)
print("set 1 : " , s1)
print("set 2 :", s2)