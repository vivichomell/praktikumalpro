# Membuat list kosong untuk menyimpan data mahasiswa
data_mahasiswa = []

# Memasukkan data mahasiswa secara dinamis
for i in range(5):
    print()
    print(f"input data mahasiswa ke{i+1}")
    nim = int(input("Masukkan NIM mahasiswa : "))
    nama = input("Masukkan nama mahasiswa : ")
    alamat = input("Masukkan alamat mahasiswa : ")
    prodi = input("Masukkan program studi mahasiswa : ")
    data_mahasiswa.append((nim, nama, alamat, prodi))

print()
print("Data Mahasiswa :")
for (nim, nama, alamat, prodi) in data_mahasiswa:
    print("NIM:", nim)
    print("Nama:", nama)
    print("Alamat:", alamat)
    print("prodi:", prodi)
    print()

# Mencari data mahasiswa berdasarkan Prodi
prodi_cari = input("Masukkan program studi yang ingin dicari: ")
print()
print("Daftar Mahasiswa Program Studi", prodi_cari, ":")
for nim, nama, alamat, prodi in data_mahasiswa:
    if prodi == prodi_cari:
        print("NIM:", nim)
        print("Nama:", nama)
        print("Alamat:", alamat)
        print("prodi:", prodi)
    
