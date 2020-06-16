import collections

def solution(clothes):
    data= []
    for i in range(len(clothes)):
        data.append(clothes[i][1])

    c = collections.Counter(data)
    sum = 1
    if len(c) <=1:
        sum += list(c.values())[0]
    else :
        for j in range(len(c)):
            tmp = list(c.values())[j]+1
            sum = sum * tmp 
    return sum -1
