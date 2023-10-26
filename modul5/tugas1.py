# Membuat list kosong untuk menyimpan data makanan dan harga
menu = []

# Memasukkan data makanan dan harganya secara dinamis 
for i in range(5):
    makanan = input("Masukkan nama makanan ke-{}: ".format(i + 1))
    harga = float(input("Masukkan harga {}: ".format(makanan)))
    menu.append((makanan, harga))

# Mencetak daftar makanan beserta harganya
print("Daftar Makanan:")
for makanan, harga in menu:
    print("{}: Rp {:.2f}".format(makanan, harga))