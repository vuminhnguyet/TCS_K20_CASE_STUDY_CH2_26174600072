from datetime import datetime
ma_phien = input("nhap ma phien: ")
ma_may = input("nhap ma may: ")
cong_suat_w = float(input("nhap cong suat thiet bi (W): "))
thoi_gian_phut = float(input("nhap thoi ian su dung (phut): "))
don_gia = float(input("nhap don gia dien (VND/kWh): "))
dien_nang_kwh = (cong_suat_w / 1000) * (thoi_gian_phut / 60)
chi_phi = dien_nang_kwh * don_gia
tren_60_phut = thoi_gian_phut > 60
thoi_diem_hien_tai = datetime.now()
thoi_diem_text = thoi_diem_hien_tai.strftime("%Y-%m-%d %H:%M:%S")
print(f"ma phien: {ma_phien}")
print(f"may: {ma_may}")
print(f"cong suat: {cong_suat_w:.2f} W")
print(f"thoi luong: {int(thoi_gian_phut)} phut")
print(f"dien nang: {dien_nang_kwh} kwh")
print(f"chi phi: {chi_phi:.2f} VND")
print(f"tren 60 phut: {tren_60_phut}")
print(f"ghi nhan luc: {thoi_diem_text}")