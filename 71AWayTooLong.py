for i in range(int(input())):
    n = input()
    if(len(n)>10):
        print(f"{n[0]}{len(n)-2}{n[-1]}")
    else:
        print(n)
