print("Pilihlah Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
ulang1 = int(input("masukkan model matematika yang diinginkan 1/2 :"))
ulang2 = int(input("menampilkan tabel matematika dari angka:"))
kali1=3
kali2=10
for i in range(1, ulang1 + 10):
    print(i,"x", kali1, "= ", i * kali1)
for i in range(1, ulang1 + 10):
    print(i,":", kali2, "=", i * kali2)
