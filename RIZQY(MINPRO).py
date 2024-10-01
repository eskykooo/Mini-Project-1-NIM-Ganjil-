# Menerapkan login sederhana nama, nim, dan kelas
print("Masukkan Nama, Nim, dan Kelas Anda")
nama = str(input("Masukkan nama anda : "))
nim = int(input("Masukkan NIM anda : "))
kelas = str(input("Masukkan kelas anda : "))
print(f"\nSELAMAT DATANG, {nama} DI PROGRAM PERHITUGAN KAMI")

# Menggunakan proses while, apakah ingin melakukan perhitungan lagi atau keluar dari program
while True:
    jam_kerja = int(input("Masukkan jumlah jam kerja Anda : ")) # Memasukkan jumlah jam kerja
    tarif_kerja = int(input("Masukkan jumlah tarif kerja Anda : ")) # Memasukkan jumlah tarif kerja

# Penerapan bonus tarif kerja sebesar 10% apabila jumlah jam kerja lebih dari 160 jam
# Jika jumlah jam kerja tidak lebih dari 160 jam, maka tidak mendapatakan bonus 10%
    if jam_kerja > 160: 
        tarif_bonus = int((100+10)/100*tarif_kerja) # Perhitungan bonus tarif kerja
        print("\nSelamat gaji anda mendapatkan bonus 10% menjadi", tarif_bonus) # Output yang muncul apabila tarif kerja sudah ditambah 10%
    else:
    # Output yang muncul apabila jam kerja tidak memenuhi syarat dan tarif kerja tidak berubah  
        print(f"\nSayangnya Anda tidak memenuhi syarat untuk mendapatkkan bonus, gajih anda tetap menjadi {tarif_kerja}") 

# Membuat output untuk pemilihan ingin menghitung ulang atau keluar dari program
# Jika jawaban yang diberikan adalah "menghitung ulang" maka program akan mengulang
# JIka jawaban yang dberikan adalah "keluar program" maka akan keluar dari program
    pertanyaan = input("Apakah anda ingin mengulang perhitungan atau keluar dari program? (Ulang/Keluar) ")
    if pertanyaan.lower() == 'ulang': 
        continue
    elif pertanyaan.lower() == 'keluar': 
        print("Terima Kasih sudah menggunakan program saya")
        break
