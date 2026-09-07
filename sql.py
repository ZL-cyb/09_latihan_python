import mysql.connector

# Menghubungkan ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cyber123",
    database="db_latihan",
)

cursor = db.cursor()


def registrasi():
  print("\n=== MENU REGISTRASI ===")
  username = input("Masukkan username baru: ")
  password = input("Masukkan password baru: ")

  # Cek apakah username sudah ada
  sql_cek = "SELECT * FROM users WHERE username = %s"
  cursor.execute(sql_cek, (username,))
  result = cursor.fetchone()

  if result:
    print("Registrasi gagal! Username sudah digunakan.")
  else:
    sql_insert = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(sql_insert, (username, password))
    db.commit()
    print("Registrasi berhasil! Silakan login.")


def login():
  print("\n=== MENU LOGIN ===")
  username = input("Masukkan username: ")
  password = input("Masukkan password: ")

  sql = "SELECT * FROM users WHERE username = %s AND password = %s"
  cursor.execute(sql, (username, password))
  result = cursor.fetchone()

  if result:
    print(f"\nLogin berhasil! Selamat datang, {username}.")
    return True
  else:
    print("\nLogin gagal! Username atau password salah.")
    return False


def main():
  while True:
    print("\n--- APLIKASI LOGIN & REGISTRASI ---")
    print("1. Login")
    print("2. Registrasi")
    print("3. Exit")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
      berhasil = login()
      if berhasil:
        # Jika sudah login, bisa tambahkan aksi lanjutan di sini
        pass
    elif pilihan == "2":
      registrasi()
    elif pilihan == "3":
      print("Keluar dari program. Terima kasih!")
      break
    else:
      print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
  main()