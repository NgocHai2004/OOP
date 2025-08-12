# Xây dựng lớp Học Sinh gồm các thuộc tính :

# Họ tên

# Ngày sinh

# Điểm 3 môn toán, lý, hóa

# Tiến hành nhập thông tin 1 học sinh từ bàn phím và in ra thông tin về họ tên, ngày sinh, tổng điểm 3 môn lấy 1 số đằng sau dấu phẩy.
class Hocsinh():
    def __init__(self,ten,ns,toan,li,hoa):
        self.ten = ten
        self.ns = ns
        self.toan = toan
        self.li = li
        self.hoa = hoa
    
    def tb(self):
        return f"{(self.toan + self.li + self.hoa):.1f}"
    
    def __str__(self):
        return f"{self.ten} {self.ns} {self.tb()}"
    
def main():
    name = input()
    birth_day = input()
    toan = float(input())
    ly = float(input())
    hoa = float(input())

    print(Hocsinh(name,birth_day,toan,ly,hoa))
main()
            