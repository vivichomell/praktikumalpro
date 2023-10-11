while True:
        denda_perhari = 2000
        denda_perminggu = 5000
        max_peminjaman = 7
        lama_peminjaman = int(input("lama peminjaman : "))
        total_denda = 0
        telat_hari = 0

        if lama_peminjaman > max_peminjaman :
            telat_hari = lama_peminjaman - max_peminjaman
        print("anda telat", telat_hari, "hari")
        for i in range (telat_hari):
            total_denda += denda_perhari
        if telat_hari >= max_peminjaman :
            for i in range(7, telat_hari+1, 7):
                total_denda += denda_perminggu
    
        print("Total denda anda adalah : ", total_denda)
        ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").lower() #agar inputan user menjadi huruf kecil
        if ulangi != "ya":
            break
print("suwonnnn")