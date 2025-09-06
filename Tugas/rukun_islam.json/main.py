import ranking

datalist[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

nilaitertinggi = 100
nilaiterendah = 10

print(rangking.urutkan_nilai(nilai))
print(rangking.nilai_trtinggi(nilai))
print(ranking.nilai_terandah(nilai))


# sama mas dafa 
import csv

file_path = r""

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("semua data")
    print("--" * 20)
    for baris in list_read:
        nomor = baris[0]
        nama = baris[1]
        kelas = baris[2]

        print(f"{nomor} | {nama} | {kelas} |")