# Kerucut
def luas_kerucut(r,s):
    p = 3.14
    luas_permukaan = p * r * (r + s)
    # definisi fungsi luas_kerucut, dua parameter,yaitu jari-jari(r)dan panjang selimut(s).
    # menghitung luas permukaan dengan menggunakan rumus pi * r * (r + s) dan mengembalikan nilai luas tersebut.
    return luas_permukaan

def luas():
    r = int(input("Masukkan nilai jari-jari kerucut : ")) #menggunakan fungsi input untuk memasukkan jari-jari kerucut dan panjang selimut kerucut
    s = int(input("masukkan nilai panjang selimut kerucut : "))

    hasil = luas_kerucut(r, s)
    print(f"Luas permukaan kerucut adalah  {hasil:.2f}")
    # .2f, hasil akan diformat sebagai bilangan desimal dengan dua angka dibelakang koma.
luas()
# untuk memanggil fungsi yang akan di jalankan terlebih dahulu

## limas segilima
def luas_permukaan_limas_segilima(sisi, tinggi):
    luas_permukaan = (5 / 4) * sisi ** 2 + (5 / 2) * sisi * tinggi
    return luas_permukaan

def luas():
    sisi = int(input("masukkan panjang sisi limas segilima: "))
    tinggi = int(input("masukkan tinggi limas segilima: "))

    hasil = luas_permukaan_limas_segilima(sisi, tinggi)
    print(f"luas permukaan limas segilima adalah {hasil:.2f}")
    
luas()

## prisma segilima
def luas_permukaan(la, kel, t):
    luas = (2 * la) + (kel * t)
    return luas

def prisma():
    la = int(input("Masukkan luas alas prisma :"))
    kel = int(input("masukkan keliling alas prisma : "))
    t = int(input("masukkan tinggi prisma: "))

    hasil = luas_permukaan(la, kel, t)
    print("Luas permukaan prisma segilima adalah", hasil)

prisma()