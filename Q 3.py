#Q3. Write a Python program to map two lists into a dictionary 

D1=['Sam','Vel','Ajay','Adhi']
D2=[10,11,12,13,14]

res = {}
for key in D1:
    for value in D2:
        res[key]=value
        D2.remove(value)
        break
print("Dictionary=",str(res))