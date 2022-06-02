n = 10000
count = 0
divideMe = 0
for i in range(1,n+1):
    more = True
    divideMe = i
    while(more == True):
        if (divideMe % 5 == 0):
            count = count + 1
            divideMe = divideMe / 5
        else:
            more = False

print(count)
