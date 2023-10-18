# mencari nilai faktorial dari suatu bilangan positif
def faktorial(n):
    # jika nilai n adalah 0 atau 1, maka nilainya adalah 1
    if n == 0 or n == 1:      
        return 1    # Rekursif : jika n lebih besar dari 1, maka nilainya adalah n di kali nilai dari n-1
    else:
        return n * faktorial(n-1)

# Input dari pengguna
bilangan = int(input("Masukkan bilangan bulat positif: "))

# Memeriksa apakah bilangan positif
# if bilangan < 0:
#     print("Maaf, finput tidak valid, faktorial hanya di definisikan untuk bilangan bulat positif.")
# else:   
#     # memanggil fungsi faktorial dan mencetak hasilnya
hasil = faktorial(bilangan)
print("Faktorial dari", bilangan , f"adalah {hasil: .2f}") 
# f pada awal string adalah agar dapat menyisipkan {} ke dalam string untuk di isi nilai yang sesuai.
