# daftar nama yang mengikuti ukm
data_all = {"madu","vivi","ina","safira","nanda","febi",
            "azli","ana","alin","marsha","rendi","mila",
            "arul", "faisal", "ali", "ani", "dinda", "kafa"}

print("daftar - daftar nama yang mengikuti ukm :") #menampilkan daftar namanya
for x in data_all:
    print(x)

# membuat daftar ukm dan anggotanya
ukm = {
    "futsal" : {"faisal", "arul", "kafa", "rendi", "vivi", "nanda"},
    "bola" : {"kafa", "febi", "madu", "azli", "faisal", "ali","ani"},
    "voli" : {"safira", "ina", "alin"},
    "basket" : {"vivi", "marsha", "madu", "ana"}
}

print("\ndaftar nama ukm dan anggotanya :") #menampilkan dafatr ukm dan anggota tiap ukm nya
for key, value in ukm.items():
    print(key, ":", value)

# menampilkan nama lebih dari satu ukm
print("\nNama yang mengikuti lebih dari satu ukm :")
nama_duplikat = set()
nama_double = set()

for anggota in ukm.values(): 
    for mahasiswa in anggota: 
        if mahasiswa in nama_duplikat: 
            nama_double.add(mahasiswa)  
        else:
            nama_duplikat.add(mahasiswa)  
print(len(nama_double),nama_double)

# menambahkan nama veli ke dalam ukm basket dan voli
ukm["basket"].add("veli")
ukm["voli"].add("veli")
print("\ndaftar nama ukm dan anggotanya yang baru :") #menampilkan daftar ukm dan anggota tiap ukm nya
for key, value in ukm.items():
    print(key, ":", value)

# menghapus nama marsha dan ani dari ukm basket
print("\ndaftar nama yang baru setelah marsha dan ani di hapus :")
ukm["basket"].remove("marsha")
ukm["bola"].remove("ani")
ukm["basket"].remove("ana")
ukm["voli"].remove("alin")
for key, value in ukm.items():
    print(key, ":", value)

# menampilkan data ukm yang anggotanya kurang dari 4
print("\nData UKM dengan anggota kurang dari 4 :")
for key, value in ukm.items():
    if len(value) < 4:
        print(key, ":", value)

# menampilkan nama yang tidak mengikuti satu ukm satupun
nama_tidak_terdaftar = set(data_all)
for anggota in ukm.values():
    nama_tidak_terdaftar -= anggota

# Menampilkan nama yang tidak mengikuti satu UKM pun
print("\nNama yang tidak mengikuti satu UKM pun:")
for nama in nama_tidak_terdaftar:
    print(nama)