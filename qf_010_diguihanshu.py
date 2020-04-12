#递归函数

def sum(n):
    if n==0:
        return 9
    else:

        return n+sum(n-1)

result = sum(10)

print(result)