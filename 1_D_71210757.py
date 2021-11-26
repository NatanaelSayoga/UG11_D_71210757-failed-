makananan = int(input("Harga makanan sebesar Rp "))
snack = int(input("Harga snack sebesar Rp "))
minuman = int(input("Harga minuman sebesar Rp "))
uang = int(input("Uang yang anda bawa sebesar Rp "))
total = makananan + snack + minuman
utang = -1 * (uang - total)
kembalian = uang - total
print("\nTotal yang harus anda bayar sebesar Rp " + str(total))
if uang < total:
    print("Uang Anda kurang! Anda memiliki utang sebesar Rp " + str(utang))
elif uang == total:
    print("Uang anda pas! Tidak ada kembalian dan utang :D")
else:
    print("Anda memiliki kembalian sebesar Rp " + str(kembalian))