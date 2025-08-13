class Sinhvien():
    def __init__(self,ma,ten,gt,ns,dc,mst,nkhd):
        self.ma = ma
        self.ten = ten
        self.gt = gt
        self.ns = ns
        self.dc = dc
        self.mst = mst
        self.nkhd = nkhd

    def __str__(self):
        return f"{self.ma} {self.ten} {self.gt} {self.ns} {self.dc} {self.mst} {self.nkhd}"
    
def main():
    a = "00001"
    b = input()
    c = input()
    d = input()
    e = input()
    g= input()
    f = input()
    print(Sinhvien(a,b,c,d,e,g,f))
    
main()