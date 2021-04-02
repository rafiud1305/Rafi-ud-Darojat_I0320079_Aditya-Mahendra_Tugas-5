print("===================================================")
print("Soal 2 Tugas 5")
print("===================================================")

# penggunaan if untuk tiga kasus dan selebihnya
# inputkan bilangan
print('Isi data di bawah ini!')
x = (input("Nama: "))
y = int(input("Nilai: "))
info = 'Halo, ' + str(x) + '! Nilai anda setelah dikonversi adalah '
# memeriksa nilai x dan y
if y > 85 and y <= 100:
    print( info + 'A')
elif y < 85 and y >= 80:
    print(info + 'A-')
elif y < 80 and y >= 75:
    print(info + 'B+')
elif y < 75 and y >= 70:
    print(info + 'B')
elif y < 70 and y >= 65:
    print(info + 'C+')
elif y < 65 and y >= 60:
    print(info + 'C')
else:
    pass
print ()


