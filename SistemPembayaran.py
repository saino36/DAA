import os
import datetime

class Pesanan:
    def __init__(self, kode, nama, harga, jumlah):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def __str__(self):
        return f"{self.kode} {self.nama} {self.harga} {self.jumlah}"

pesanan = []
hargatotal = 0
discount = 0

def clear():
    os.system('clear||cls')

clear()

while True:
    CS=input ("Masukan Kode CS[KJ/RA/KN] :").strip().upper()
    clear()
    if CS== "KJ":
        nama_CS= "Kevin Januari"
        print("Have a nice day " + nama_CS)
        break
    elif CS== "RA":
        nama_CS= "Raes Ahmad"
        print("Have a nice day " + nama_CS)
        break
    elif CS== "KN":
        nama_CS= "Kevin Nabel"
        print("Have a nice day " + nama_CS)
        break
    else: print('cs tidak ditemukan')

print("============================ MENU ===========================")
print("1. Ayam Tepung Geprek RP.15.000")
print("2. Ayam Goreng Geprek RP.15.000")
print("3. Ayam Bakar Geprek  RP.20.000")
print("4. Sosis Bakar        RP.15.000")
print("5. Cozy Burger        RP.22.000")
print("0. Selesai")

while True:
    print("=============================================================")
    kode = input("Masukan kode paket : ")

    if kode == "1" :
        nama = "Ayam Tepung Geprek"
        harga = 15000
    elif kode == "2" :
        nama = "Ayam Goreng Geprek"
        harga = 15000
    elif kode == "3" :
        nama = "Ayam Bakar Geprek"
        harga = 20000
    elif kode == "4" :
        nama = "Sosis Bakar"
        harga = 15000
    elif kode == "5" :
        nama = "Cozy Burger"
        harga = 15000
    elif kode == "0" :
        break
    else:
        print("=== Makanan Tidak Tersedia, Silahkan pilih Lainnya ===")
        continue

    jumlah = int(input("Masukan Jumlah Pesanan: "))
    
    tempPesanan = Pesanan(kode, nama, harga, jumlah)

    pesanan.append(tempPesanan)

clear()
    
for item in pesanan:
    print("~~~ Makanan                   :", item.nama)
    print("~~~ Jumlah                    :", item.jumlah)
    print("~~~ Harga Satuan              : Rp.", item.harga)
    print()
    hargatotal += (item.jumlah * item.harga)

pembeli = input("Input nama pembeli            : ")

while True:
    tempat = input("Input tempat [Indoor/Outdoor] : ").strip().lower()
    if tempat == 'indoor' or tempat == 'outdoor': break
    else:
        print("Input yang bener")
        continue

nomor = input("Input nomor meja              : ")

if hargatotal >= 100000: 
    discount = hargatotal * 0.1
totalbayar = hargatotal - discount

print("Total Harga                   : Rp. "+str(hargatotal))
print("Discount Didapat              : Rp. "+str(discount))
print("Anda Harus Membayar           : Rp. {}".format(totalbayar))
ub=int(input("Masukan Uang Bayar            : Rp. "))
kembali = ub - totalbayar
print("Kembalian                     : Rp.",+kembali)

Note_Pemesan = input("Catatan lain dari pembeli     : ")

print()
print()
print()

x = datetime.datetime.now()
print("=============================================================")
print("                    The Only One Cbezt UEU                   ")
print("      Jl. Arjuna Utara No.9, Duri Kepa, Kec. Kb. Jeruk       ")
print("Date :", x.strftime("%x"), x.strftime("%X"))
print("=============================================================")
print("~~~ Nama CS               :", nama_CS)
print("~~~ Nama Pembeli          :", pembeli)
print("~~~ Tempat                :", tempat)
print("~~~ Nomor Meja            :", nomor)
print("=============================================================")
for item in pesanan:
    print("~~~ Makanan               :", item.nama)
    print("~~~ Jumlah                :", item.jumlah)
    print("~~~ Harga Satuan          : Rp.", item.harga)
print("=============================================================")
print("Total Harga               : Rp. "+str(hargatotal))
print("Discount Didapat          : Rp. "+str(discount))
print("Anda Harus Membayar       : Rp. {}".format(hargatotal - discount))
print("Kembalian                 : Rp.",+kembali)
print("=============================================================")
print("Catatan lain dari pembeli :", Note_Pemesan)
print("=============================================================")
print("                                                     ")
print("            Terima Kasih Sudah Berkunjung            ")
print("         Kepuasan Anda Merupakan Prioritas Kami      ")
print("                                                     ")