# Input: Menyimpan enam nilai ke dalam List.
nilai = [75, 55, 80, 60, 45, 90]

# Proses: Memilih nilai yang memenuhi batas kelulusan.
lulus = []
for x in nilai:
    if x >= 60:
        lulus.append(x)
    
# Ouput: Menampilkan nilai yang Lulus dan jumlahnya.
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}") 