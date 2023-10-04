# Meminta input
nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))
nilai_tugas_akhir = float(input("Masukkan nilai tugas akhir: "))

# Menghitung rata-rata nilai
rata_rata = (nilai_tugas + nilai_uts + nilai_uas + nilai_tugas_akhir) / 4


# Menentukan nilai berdasarkan ketentuan
if 80 <= rata_rata <= 100:
    nilai = "A"
elif 70 <= rata_rata < 80:
    nilai = "B"
elif 60 <= rata_rata < 70:
    nilai = "C"
elif 40 <= rata_rata < 60:
    nilai = "D"
elif 0 <= rata_rata < 40:
    nilai = "E"
else :
    nilai = "Nilai Tidak Valid"
    
# Menampilkan hasil
print(f"Nama Mahasiswa: {nama}")
print(f"Rata-rata Nilai: {rata_rata:.2f}")
print(f"Nilai: {nilai}")
