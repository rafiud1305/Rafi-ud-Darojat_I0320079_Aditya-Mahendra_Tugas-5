print("===================================================")
print("Soal 1 Tugas 5")
print("===================================================")

# penggunaan if untuk dua kasus
# inputkan nama dan jenis kelamin
nama = (input('Nama:'))
jenis_kelamin = (input('Jenis kelamin (L/P):')).upper()
# memeriksa
if jenis_kelamin == 'L':
    print('Tuan',nama)
else:
    print('Nyonya',nama)
print()