pemain1 = input("Pemain 1, masukkan pilihan Anda : ")
pemain2 = input("Pemain 2, masukkan pilihan Anda : ")

if pemain1 == pemain2:
    print("Seri")
elif pemain1 == "gunting" :
    if pemain2 == "batu" :
        print("pemain 2 : menang!!")
    else :
        print("pemain 1 : menang!!")
elif pemain1 == "batu" :
    if pemain2 == "kertas" :
        print("pemain 2 : menang!!")
    else :
        print("pemain 1 : menang!!")
elif pemain1 == "kertas" :
    if pemain2 == "gunting" :
        print("pemain2 : menang!!")
    else :
        print("pemain 1 : menang!!")
else :
     print("input tidak valid")


