res = 0
for i in range(int(input())):
    a,b,c = map(int,input().split())
    if(a == 1 and b == 1) or (b == 1 or c == 1) or (a == c):
        res += 1
print(res)
