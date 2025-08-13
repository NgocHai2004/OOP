def chuanhoa(ns:str):
    n = ns.split("/")
    chuoi = ""
    for i in n:
        if len(i) <2:
            chuoi += f"0{i}/"
        else:
            if len(i) == 4:
                chuoi += f"{i}"
            else:
                chuoi += f"{i}/"
    return chuoi
def chuanhoa2(ten:str):
    ds = ten.split(" ")
    ten_new = ""
    for ten1 in ds: 
        n = len(ten1)
        for i in range(n):
            if i == 0:
                ten_new += ten1[i].upper()
            else:
                ten_new += ten1[i].lower()
        ten_new += " "
    return ten_new

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
        return f"{self.ma} {self.ten}{self.gt} {self.ns} {self.dc} {self.mst} {self.nkhd}"
    
def main():
    a = "00001"
    b = chuanhoa2(input())
    c = input()
    d = chuanhoa(input())
    e = input()
    g= input()
    f = chuanhoa(input())
    print(Sinhvien(a,b,c,d,e,g,f))
    
main()