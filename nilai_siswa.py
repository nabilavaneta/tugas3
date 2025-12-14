nilai_a = int(input("Masukkan Nilai A (angka bulat): "))
nilai_b = int(input("Masukkan Nilai B (angka bulat): "))

rata_rata = (nilai_a + nilai_b) / 2

if rata_rata >= 75:
    status = ("Lulus")
else:
    status = ("Tidak lulus")
    
print("nilai a : ", nilai_a)
print("nilai b : ", nilai_b)
print("Status : ", status)  
print("Rata-rata : ", rata_rata)
       