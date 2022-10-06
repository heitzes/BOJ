fdict = {0: 0, 2:1, 3:7, 4:4, 5:2, 6:6, 7:8}
def maxi(n):
    num = 0
    if n % 2 == 1:
        two = n//2 - 1
        rem = 7
    else:
        two = n//2
        rem = 0
    for i in range(two):
        num += 10**i
    num += rem * (10**(two)) 
    return num
def mini1(n):
    num = 0
    seven = n // 7
    rem = n % 7
    for i in range(seven):
        num += 10**i*8
    num += 10**(seven)*fdict[rem]
    return num
def mini3(n):
    num = 0
    seven = n // 7
    rem = n % 7
    if rem == 3:
        seven -= 1
        if seven == 0:
            num = 22
        else:
            num += 10**seven*20
            for i in range(seven-1):
                num += 10**i*8
    else:
        seven -= 1
        for i in range(seven):
            num += 10**i*8
        num += 10**seven*20
    return num
def mini2(n):
    num = 0
    seven = n // 7
    rem = n % 7
    if rem == 1:
        num += 10**(seven)
        seven -= 1
        for i in range(seven):
            num += 10**i*8
    else:
        num += 10**(seven)*6
        for i in range(seven):
            num += 10**i*8
    return num
def mini(n):
    if n <= 7:
        return fdict[n]
    else:
        rem = n % 7
        if rem == 0 or rem == 2 or rem == 5:
            return mini1(n)
        if rem == 1 or rem == 6:
            return mini2(n)
        if rem == 3 or rem == 4:
            return mini3(n)
N = int(input())
for i in range(N):
    stick = int(input())
    minn = mini(stick)
    maxn = maxi(stick)
    print("{} {}".format(minn, maxn))
