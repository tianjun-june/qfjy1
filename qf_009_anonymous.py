from functools import reduce


tuple1 = (3,5,7,9,8,2)

result = reduce(lambda x,y:x+y,tuple1)

print(result)

list1 = [12,6,8,98,34,36,2,8,0]

result1 = filter(lambda x:x>10,list1)
print(list(result1))
