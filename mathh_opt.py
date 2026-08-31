#Program Ganjil/Genap
def cek_ganjil_genap():
    print("=" * 30)
    print("PROGRAM CEK GANJIL/GENAP")
    print("=" * 30)

    while True:
     #meminta input angka dari user
        angka= int (input("\nMasukan angka :"))
    
     #mengecek apakah genap atau ganjil
        if angka % 2 == 0:
            print(f"{angka} adalah bilangan GENAP")
        else:
            print(f"{angka} adalah bilangan GANJIL")
        
        #tanya user ingin mengulang?
        ulang= input("Apakah mau cek angka lagi? (y/n): ")
    
        #jika user mengetik selain 'y' loop akan berhenti
        if ulang.lower() != 'y':
            break
    
# OPERATOR BILANGAN PRIMA
def cek_bilangan_prima():
    print("\n" + "=" * 30)
    print("PROGRAM CEK BILANGAN PRIMA")
    print("=" * 30)
    
    while True:
        angka = int(input("\nMasukan angka : "))
        
        if angka > 1:
            is_prima = True
            for i in range(2, angka):
                if angka % i == 0:
                    is_prima = False
                    break
                
            if is_prima:
                print(f"{angka} adalah bilangan PRIMA")
            else:
                print(f"{angka} BUKAN bilangan PRIMA")
        else:
            print(f"{angka} BUKAN bilangan PRIMA")
        ulang = input("Apakah mau cek angka lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

#Operator bilangan rumus persegi
def cek_bilangan_rumus_persegi():
    print("\n" + "=" * 30)
    print("PROGRAM CEK BILANGAN RUMUS PERSEGI")
    print("=" * 30)
    
    while True:
        panjang = int(input("\nMasukan panjang persegi : "))
        lebar = int(input("\nMasukan lebar persegi : "))
        
        if panjang * lebar == 1:
            print(f"{panjang} x {lebar} adalah bilangan RUMUS PERSEGI")
        else:
            print(f"{panjang} x {lebar} BUKAN bilangan RUMUS PERSEGI")
        ulang = input("Apakah mau cek panjang persegi lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

import math
#Operasi konversi sudut
def konversi_sudut():
    print("\n" + "=" * 30)
    print("PROGRAM OPERASI KONVERSI SUDUT")
    print("=" * 30)
    
    while True:
        derajat = float(input("\nMasukan derajat : "))
        
        radian = derajat * (math.pi / 180)
        print(f"{derajat}° adalah {radian:.4f} RADIAN")
        
        Ulang = input("Apakah mau cek derajat lagi? (y/n): ")
        if Ulang.lower() != 'y':
            break 
     

# MENU UTAMA
while True:
    print("\n" + "=" * 30)
    print("PILIH PROGRAM")
    print("=" * 30)
    print("1. Cek Ganjil / Genap")
    print("2. Cek Bilangan Prima")
    print("3. Keluar")
    print("=" * 30)
    
    pilihan = input("Pilih menu (1/2/3) : ")
   
    if pilihan == '1':
       cek_ganjil_genap()
    elif pilihan == '2':
        cek_bilangan_prima()
    elif pilihan =='3':
        cek_bilangan_rumus_persegi()
    elif pilihan =='4':
        konversi_sudut()
    elif pilihan =='5':
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        
print("\n" + "=" * 30)
print("SELESAI")
                    
                    
