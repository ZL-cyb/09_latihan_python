# OPERATOR GANJIL GENAP
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
    
print("=" * 30 )
print("SELESAI")