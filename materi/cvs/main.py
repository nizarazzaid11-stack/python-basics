import csv

file_path = r"C:\Users\DANANG WAHYUDI\OneDrive\Documents\python\materi b.py\cvs\data.csv"

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



# sama mas dafa 2
import csv
from collections import defaultdict

# Data dalam format CSV (bisa juga dibaca dari file .csv)
data = """Tanggal,Keterangan,Kategori,Jumlah
2025-08-20,Sarapan,Makan,20000
2025-08-20,Naik Angkot,Transportasi,10000
2025-08-21,Makan Siang,Makan,25000
2025-08-21,Beli Pulsa,Komunikasi,15000
2025-08-22,Snack,Makan,10000
2025-08-22,Bensin,Transportasi,30000
2025-08-22,Buku,Belajar,40000"""

# Parsing data
lines = data.strip().split('\n')
reader = csv.reader(lines)

# Lewati header
header = next(reader)

# Buat dictionary untuk menyimpan total per kategori
kategori_total = defaultdict(int)
total_semua = 0

# Proses setiap baris
for row in reader:
    tanggal = row[0]
    keterangan = row[1]
    kategori = row[2]
    jumlah = int(row[3])
    
    kategori_total[kategori] += jumlah
    total_semua += jumlah

# Tampilkan hasil
print("📊 Rekap Pengeluaran per Kategori:")
for kategori, total in kategori_total.items():
    print(f"- {kategori}: Rp{total:,}")

print(f"\n💰 Total Pengeluaran Keseluruhan: Rp{total_semua:,}")

# sam mas dafa 3
import csv
from collections import defaultdict

# Data CSV sebagai string
data = """Tanggal,Keterangan,Kategori,Jumlah
2025-08-20,Sarapan,Makan,20000
2025-08-20,Naik Angkot,Transportasi,10000
2025-08-21,Makan Siang,Makan,25000
2025-08-21,Beli Pulsa,Komunikasi,15000
2025-08-22,Snack,Makan,10000
2025-08-22,Bensin,Transportasi,30000
2025-08-22,Buku,Belajar,40000"""

# Parsing data
lines = data.strip().split('\n')
reader = csv.reader(lines)

# Ambil header
header = next(reader)

# Simpan data & hitung total
kategori_total = defaultdict(int)
total_semua = 0
all_data = []

# Proses setiap baris
for idx, row in enumerate(reader, 1):
    tanggal = row[0]
    keterangan = row[1]
    kategori = row[2]
    jumlah = int(row[3])

    all_data.append((idx, tanggal, keterangan, kategori, jumlah))
    kategori_total[kategori] += jumlah
    total_semua += jumlah

# Tampilkan semua data
print("📋 Semua Data")
print("-" * 60)
print("No | Tanggal     | Keterangan    | Kategori      | Jumlah")
print("-" * 60)
for no, tanggal, ket, kat, jml in all_data:
    print(f"{no:<2} | {tanggal} | {ket:<13} | {kat:<13} | Rp{jml:,}")
print("-" * 60)

# Tampilkan rekap per kategori
print("\n📊 Rekap Pengeluaran per Kategori:")
for kat, total in kategori_total.items():
    print(f"- {kat:<13}: Rp{total:,}")

# Total semua
print(f"\n💰 Total Pengeluaran Keseluruhan: Rp{total_semua:,}")


# sama mas dafa
import csv

file_path = r"C:\Users\DANANG WAHYUDI\OneDrive\Documents\python\materi b.py\cvs\data1.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)
    print("semua keuangan")
    print("tanggal | keterangan | kategori | jumlah")

    print("semua data")
    print("--" * 20)
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori = baris[2]
        jumalah = baris[3]

        print(f"{tanggal} | {keterangan} |  {kategori} | {jumalah} |")

# mas dafa 
with open(file_path, "r") as file_baru:
    next(file_baru)
    rea = csv.reader(file_baru)
    list_read = list(read)
    print("semua data")
    print("--" * 20)
    for baris in list_read:
        nomor = baris[0]
        nama = baris[1]
        kelas = baris[2]
        print(f"{nomor} | {nama} | {kelas} |")

# tambah data
with open(file_path, "r") as file_baru: