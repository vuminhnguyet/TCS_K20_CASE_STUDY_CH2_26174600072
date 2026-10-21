ma_may = input("nhap ma may:")
cong_suat_w = input("nhap cong suat W:")
so_phut = int(input("nhap so phut:"))
dien_nang_kwh = cong_suat_w * so_phut
#loai loi: typeerror
#thong bao loi: unsupported operand type(s) for /: 'str' and 'int'
#nguyen nhan: do ham input() tra ve keu chuoi(str) nen khong the thuc hien phep toan chia voi kieu so nguyen(int)
#cach sua: thuc hien ep kieu cho cong_suat_w sang kieu so thuc(float) hoac so nguyen(int) ngay khi nhap vao tu ban phim
ma_may = input("nhap ma may:")
cong_suat_w = float(input("nhpa cong suat w"))
so_phut = float(input("nhap so phut"))
dien_nang_kwh = cong_suat_w * so_phut /60/1000
print(f"may: {ma_may}")
print(f"dien nang: {dien_nang_kwh:.3f} kWh")
#loi 1: loi kieu du lieu
#loi 2: loi logic dinh dang du lieu