from Data_Handling import urutkan_data, cari_data

while True:
    print("\n" + "=" * 30)
    print("PILIH PROGRAM")
    print("=" * 30)
    print("1. Urutkan Data")
    print("2. Cari Data")
    print("3. Keluar")
    print("=" * 30)

    pilihan = input("Pilih menu (1/2/3) : ")

    if pilihan == '1':
        urutkan_data()
    elif pilihan == '2':
        cari_data()
    elif pilihan == '3':
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

print("\n" + "-" * 30)
print("SELESAI")