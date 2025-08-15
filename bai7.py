class Nhanvien():
    def __init__(self,ma,ten,luong,nc,cv):
        self.ma = ma
        self.ten = ten
        self.luong = luong
        self.nc = nc
        self.cv = cv
    
    def luongchuan(self):
        return self.nc*self.luong

    def thuong(self):
        if self.nc > 25:
            return self.luongchuan()*0.2
        elif self.nc >22:
            return self.luongchuan()*0.1
        else:
            return 0
    
    def phucap(self):
        if self.cv == "GD":
            return 250000
        elif self.cv == "PGD":
            return 200000
        elif self.cv == "TP":
            return 180000
        else:
            return 150000

    def __str__(self):
        return f"{self.ma} {self.ten} {int(self.luongchuan())} {int(self.thuong())} {int(self.phucap())} {int(self.luongchuan() + self.thuong() + self.phucap())}"
    
def main():
    ma = "NV01"
    ten = input()
    luong = int(input())
    nc = int(input())
    chuc = input()
    print(Nhanvien(ma,ten,luong,nc,chuc))

main()

        