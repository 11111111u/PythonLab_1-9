try:
    N = int(input("Enret N="))
except Exception:
    print("Enter a number")
else:
    M=N
    pp=''
    while M!=0:
        i=M
        L=[]
        while i!=0:
            if i <= M:
                L.append(str(i))
                i-=1
        a = list(L)
        pp=''.join(a)
        print(pp)
        M=M-1