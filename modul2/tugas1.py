# Membaca umur dari pengguna
umur = int(input("Masukkan umur Anda: "))

# kategori berdasarkan umur
if umur > 50:
    kategori = "Tua"
elif umur > 25:
    kategori = "Dewasa"
elif umur > 17 :
    kategori = "Muda"
elif umur > 7 :
    kategori = "Anak-anak"
else :
    kategori = "Umur tidak valid"

# Menampilkan hasil kategori umur
print("umur termasuk dalam kategori:", kategori)

