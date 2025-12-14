angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /, %): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == '+':
    print("Hasil:", angka1 + angka2)
elif operator == '-':
    print("Hasil:", angka1 - angka2)
elif operator == '*':
    print("Hasil:", angka1 * angka2)
elif operator == '/':
    if angka2 != 0:
        print("Hasil:", angka1 / angka2)
    else:
        print("Error: Tidak bisa membagi dengan nol!")
elif operator == '%':
    if angka2 != 0:
        print("Hasil:", angka1 % angka2)
    else:
        print("Error: Tidak bisa modulus dengan nol!")
else:
    print("Operator tidak valid!")
