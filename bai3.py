class Sinhvien():
    def __init__(self,ma,ten,lop,ns,gpa):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.ns = ns
        self.gpa = gpa
    
    def chuanhoa(self):
        n = self.ns.split("/")
        ns_new = ""
        for i in n:
            if len(i)<2:
                ns_new += f"0{i}/"
            else:
                if len(i)==4:
                    ns_new += f"{i}"
                else:
                    ns_new += f"{i}/"
        return ns_new
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.lop} {self.chuanhoa()} {self.gpa}"
    
def main():
    ma = "SV001"
    ten = input()
    lop = input()
    ns = input()
    gpa = float(input())

    print(Sinhvien(ma,ten,lop,ns,gpa))

main()

        