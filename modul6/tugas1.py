# data awal
data_mahasiswa = {
    "Nama": "Susanti",
    "Alamat": "Surakarta",
    "Prodi": "Sistem Informasi",
    "Semester": 5,
    "Angkatan": 2015
}
for key,values in data_mahasiswa.items():
    print(key,values)

# Meminta pengguna untuk memasukkan tahun pindah tempat tinggal dan perpindahan prodi
thn_pindah = int(input("Masukkan Tahun Pindah Tempat Tinggal dan pindahan Prodi : "))

# Update data saat pindah ke Madura dan berpindah prodi
if thn_pindah >= data_mahasiswa["Angkatan"]:
    data_mahasiswa["Alamat"] = input("Masukkan Alamat Baru: ")
    data_mahasiswa["Prodi"] = input("Masukkan Program Studi Baru: ")

# Tampilkan data terbaru
print("\nData Mahasiswa:")
for key, value in data_mahasiswa.items():
    print(f"{key}: {value}")


# apakah susanti memutuskan untuk berhenti sebagai mahasiswi
thn_berhenti = int(input("Masukkan Tahun Berhenti menjadi Mahasiswi (atau 0 jika belum berhenti): "))

# Jika pengguna memutuskan untuk berhenti, perbarui status
if thn_berhenti > 0:
    data_mahasiswa["Status"] = "Tidak Aktif"

# Tampilkan tahun Susanti berhenti
if "Status" in data_mahasiswa and data_mahasiswa["Status"] == "Tidak Aktif":
    print(f"{data_mahasiswa['Nama']} berhenti menjadi mahasiswi pada tahun {thn_berhenti}.")

# Tampilkan data terbaru
print("\nData Mahasiswa:")
for key, value in data_mahasiswa.items():
    print(f"{key}: {value}")
