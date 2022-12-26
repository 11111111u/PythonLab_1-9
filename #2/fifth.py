class Building:
    def __init__(self,w,c,n=0):
        self.what=w;
        self.color=c;
        self.numbers=n;
        self.mwhere(n)
    def mwhere(self,n):
        if n<=0:
            self.where = "absent"
        elif 0<n<100:
            self.where = "small"
        else :
            self.where = "main"
    def plus(self,p):
        self.numbers = self.numbers+p
        self.mwhere(self.numbers);
    def minus(self,m):
        self.numbers = self.numbers-m;
        self.mwhere(self.numbers)

m1 = Building('wood',"white",50)
m2 = Building('wood',"brown",300)
m3 = Building('brick',"white")
print(m1.what,m1.color,m1.where)
print(m2.what,m2.color,m2.where)
print(m3.what,m3.color,m3.where)
m1.plus(500);
print('//////////////')
print(m1.what,m1.color,m1.where)