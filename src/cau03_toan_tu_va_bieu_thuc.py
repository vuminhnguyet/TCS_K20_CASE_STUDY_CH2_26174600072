tong_phut = 135
cong_suat_w = 250
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("so gio tron ven:", so_gio)
print("so phut con lai:", so_phut_con_lai)
su_dung_lau = tong_phut > 60
print("su dung lau (>60 phut):", su_dung_lau)
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("du lieu hop le:", du_lieu_hop_le)
ket_qua_1 = 100 + 20*3
ket_qua_2 = (100 + 20) * 3
print("ket qua 100 + 20*3:", ket_qua_1)
print("ket qua (100 + 20) * 3:", ket_qua_2)
#du doan
#ket qua 1 = 160
#ket qua 2 = 360