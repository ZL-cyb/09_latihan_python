def urutkan_data():
    print("=" * 30)
    print("PROGRAM URUTKAN DATA")
    print("=" * 30)
    
    while True:
        teks_input = input("\nMasukan angka angka (pisahkan dengan koma) : ")
        #mengubah input "5, 2, 8" menjadi list angka [5, 2, 8]
        angka_list =[int(x.strip()) for x in teks_input.split(",")]
        
        #pengurutan
        angka_list.sort()
        print(f"hasil setelah diurutkan (Kecil ke Besar): {angka_list}")
        
        ulang = input("Apakah mau cek lagi? (y/n): ")
        if ulang.lower() != 'y':
            break
        
def cari_data():
    print("=" * 30)
    print("PROGRAM CARI DATA")
    print("=" * 30)
    
    #user memasukan daftar datanya sendiri
    teks_input = input("\nMasukan angka angka (pisahkan dengan koma) : ")
    #membuat daftar data dan menyamakan ke huruf kecil
    daftar_data =[x.strip().lower() for x in teks_input.split(",")]
    
    print(f"Daftar tersimpan: {daftar_data}")
    
    while True:
      data_cari = input("\nMasukan angka yang ingin dicari : ").strip().lower()
      
      if data_cari in daftar_data:
        posisi = daftar_data.index(data_cari) + 1
        jumlah = daftar_data.count(data_cari)
        print(f"-> '{data_cari}' DITEMUKAN di urutan ke-{posisi} (Total ada {jumlah})")
        
      else:
          print(f"-> '{data_cari}' TIDAK DITEMUKAN")
          
      ulang = input("Apakah mau cek lagi? (y/n): ")
      if ulang.lower() != 'y':
        break

def hapus_data():
    print("=" * 30)
    print("PROGRAM HAPUS DATA")
    print("=" * 30)
    
    while True:
      teks_input = input("\nMasukan data berganda (pisahkan dengan koma) : ")
      # Contoh input: "apel, jeruk, apel, mangga"
      data_list =[x.strip() for x in teks_input.split(",")]
      
      # Menghapus duplikat menggunakan set, lalu diubah kembali ke list
      data_bersih = list(dict.fromkeys(data_list))
      print(f"data asli : {data_list}")
      print(f"data bersih : {data_bersih}")
      
      ulang = input("Apakah mau cek lagi? (y/n): ")
      if ulang.lower() != 'y':
        break
    


      
      

