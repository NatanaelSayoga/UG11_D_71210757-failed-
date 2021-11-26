belanja = (input("Masukkan daftar belanja Anda : "))
himp_belanja = belanja.title().split(", ")
print("Daftar belanja : " + str(himp_belanja))
barang = input("Masukkan barang yang ingin ditambahkan : ")
akan_ditambahkan = barang.upper().split(", ")
himp_kumulatif = belanja.upper().split(", ")
if str(akan_ditambahkan[0]) == str(himp_kumulatif[0]):
    print("Barang " + str(akan_ditambahkan) + " sudah berada dalam daftar belanja")
elif str(akan_ditambahkan[0]) == str(himp_kumulatif[1]):
    print("Barang " + str(akan_ditambahkan) + " sudah berada dalam daftar belanja")
elif str(akan_ditambahkan[0]) == str(himp_kumulatif[2]):
    print("Barang " + str(akan_ditambahkan) + " sudah berada dalam daftar belanja")
else:
    himp_kumulatif.extend(akan_ditambahkan)
    himp_belanja.extend(akan_ditambahkan)
    print("Hasil penambahan pada daftar belanja : " + str(himp_belanja))