def expanding(lst):
    lst2 = []
    for i in range(1, len(lst)):
        x = lst[i] - lst[i-1]
        lst2.append(abs(x))
    y = True
    for i in range(1, len(lst2)):
        if lst2[i]<=lst2[i-1]:
            y = False
            break


    return y


lst = list(map(int,input().split))
print(expanding(lst))