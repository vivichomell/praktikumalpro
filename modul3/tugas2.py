n = int(input("masukkan angka akhir : "))

print("angka prima antara 2 dan", n, "adalah")
for m in range(2, n+1):
    if m >1 :
        for i in range(2, m):
            if(m % i) == 0:
                break
        else:
                print(m)