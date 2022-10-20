#Input nilai variable
a = input("masukan nilai a:")
b = input("masukan nilai b:")

#Cetak nilai variable
print("nilai a = ", a)
print("nilai b = ", b)

#Cetak Hasil operasi kedua variable dengan string format
print("hasil penggabungan {1}&{0}=%s".format(a, b) %(a + b))

#Konversi nilai variable
a = int(a)
b = int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a, b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a, b) %(a/b))