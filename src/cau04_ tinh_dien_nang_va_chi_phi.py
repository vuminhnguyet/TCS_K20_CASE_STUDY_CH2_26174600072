cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut/60/1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("dien nang tieu thu:", dien_nang_kwh, "kwh - kieu:", type(dien_nang_kwh))
print("chi phi dien:", chi_phi, "dong - kieu:", type(chi_phi))
#dien nang tieu thu = 0.375 kwh
#chi phi dian = 1125 dong
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut/60/1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("dien nang tieu thu:", dien_nang_kwh, "kwh - kieu:", type(dien_nang_kwh))
print("chi phi dien:", chi_phi, "dong - kieu:", type(chi_phi))
#so sanh: dien nang tieu thu va chi phi dien deu be hon khi so phut la 60