class Giaovien():
    def __init__(self,chuc,ten,luong:int):
        self.chuc = chuc
        self.ten = ten
        self.luong = luong
    
    def heso(self):
        n = self.chuc[2:4]
        if n[0] == 0:
            return int(n[1])
        else:
            return int(n[0:2])
        
    def thunhap(self):
        n = self.chuc[0:2]
        if n == "HT":
            thuong = 2000000
        elif n == "HP":
            thuong = 900000
        else:
            thuong = 500000
        print(thuong)
        return (self.heso()*self.luong) + thuong
    
    def __str__(self):
        return f"{self.chuc} {self.ten} {self.heso()} {self.thunhap()}"
    
def main():
    a = input()
    b = input()
    c = int(input())
    print(Giaovien(a,b,c))
main()
        