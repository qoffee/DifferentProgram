from time import time 

s = time()
def f(n):
    l = [0, 1]
    lEven = [0]
    i, c = l
    while c < n:
        el = l[i+1]+l[i]
        l.append(el)
        if el % 2 == 0: 
            lEven.append(el)
            c += 1
        i += 1
    return lEven

f(40000)
print(time()-s)

# s = time()
# def f(n):
#     def fGen(num):
#         a, b = 0, 1
#         i = 0
#         while i < num:
#             if a % 2 == 0:
#                 yield a
#                 i += 1
#             a, b = b, a + b

#     return list(fGen(n))

# f(40000)

# print(time()-s)