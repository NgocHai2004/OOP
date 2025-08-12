
# Xây dựng lớp phân số gồm 2 thuộc tính là tử số và mẫu số đều là số nguyên. Tiến hành nhập 1 phân số từ bàn phím và in ra nó ở dạng tối giản.
def gcd(a:int,b:int):
    if b == 0:
        return a
    return gcd(b,a%b)

class Phanso():
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    
    def ps(self):
        ucln = gcd(self.tu,self.mau)
        a = int(self.tu//ucln)
        b = int(self.mau//ucln)
        return f"{a}/{b}"
    
def main():
    a,b = map(int,input().split())
    print(Phanso(a,b).ps())
main()