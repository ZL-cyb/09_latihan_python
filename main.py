from Data_Handling import urutkan_data
from Data_Handling import cari_data
from mathh_opt import konversi_sudut
from mathh_opt import cek_bilangan_rumus_persegi

while True:
    print("\n" + "=" * 30)
    print("PILIH PROGRAM")
    print("=" * 30)
    print("1. Cek Data")
    print("2. Cari Data")
    print("3. Konversi Sudut")
    print("4. Cek Bilangan Rumus Persegi")
    print("5. Keluar")
    print("=" * 30)
    
    pilihan = input("Pilih menu (1/2/3/4/5) : ")
   
    if pilihan == '1':
       urutkan_data()
    elif pilihan == '2':
        cari_data()
    elif pilihan == '3':
        konversi_sudut()
    elif pilihan == '4':
        cek_bilangan_rumus_persegi()
    elif pilihan =='5':
        break
    else:    
        print("Pilihan tidak valid, silakan coba lagi.")
        
print("\n" + "=" * 30)
print("SELESAI")


