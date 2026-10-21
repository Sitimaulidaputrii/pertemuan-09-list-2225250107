# Proses: Membuat fungsi untuk menghitung rata-rata.
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Input: Menyimpan lima nilai ke dalam List.
nilai = [75, 80, 65, 90, 88]

# Output: Menampilkan rata-rata nilai.
print(f"Rata-rata = {rata_rata(nilai):.2f}")