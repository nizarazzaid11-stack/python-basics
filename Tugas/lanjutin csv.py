anime_file_path = r"C:\Users\DANANG WAHYUDI\OneDrive\Documents\python\anime.csv"
data_anime = [] # list kosong
with open(anime_file_path, "r") as file_anime:
    # baca dgn fungsi reader() darfi modul csv
    baca_file_anime = csv.reader(file_anime)
    # ubah dada per baris indek
    for item in data_anime:
     if item[1] == "wildan":
        print("item wildan ditemukan, ubah data nya...")
        item[2] = "demon slayer"
        item[3] = 9.5
print("-----update csv-----")
 # mode "w" [write] dari nodule csv
with open (anime_file_path, 'w' new line='') as file_anime:
write_anime = csv.write(file_anime)
# fungsi wirterow() dtk sama dgn writrows()
# wirtrow() -> 1 baris
# writerows() -> seuruh baris 




