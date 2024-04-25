

def sum(k,a,b):
    i = 1
    j = 1
    flag = 0
    c = []
    while i <= len(a) and j <= len(b):
        if flag:
            a[-i]+=1
        if a[-i] + b[-j] > k:
            flag = 1
        else:
            flag = 0
        c[i-1] = (a[-i] + b[-j]) % k
        i += 1
        j += 1
    if i == len(a):

    if j == len(b):
        
    if flag == 1:
        c[i-1] = 1
    flag = 0
    i = 1
    while i <= len(c):
        if flag:
            c[-i] += k
        if c[-i] % 2 == 1:
            flag = 1
        else:
            flag = 0
        c[-i] = c[-i]/2
        i += 1
    if c[-1] == 0:
        i = 2
    else:
        i = 1
    d = []
    j = 0
    while i < len(c):
        d[j] = c[-i]
        i += 1
        j += 1
    return d

k = 6
a = [1,3,5]
b = [2,1]
print(sum(k, a, b))
        


