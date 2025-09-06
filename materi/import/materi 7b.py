# set -> {} -> {tidadak berurutan, berrubah, tidak duplikat}
game_azka = {"valorant", "drak soul"}
game_evan = {"gensin", "mlbb"}
print("evan games:", game_evan)
print("azka games:", game_azka)

# .add() -> menambahkan item baru
game_azka.add("elden ring")
game_azka.add("valorant") # tikdak akan menambah

# .remove() ->menghapus item
game_evan.remove("mlbb")
# len() menghitung jumlah item
print("azka ada", len(game_azka)," games: ", game_azka)
print("evan ada", len(game_evan), "games: ", game_evan)

# union() -> menggabung 2 set berbeda
game_berdua = game_azka.union




# intersion() -> mencari item
# difference() -> mencari item beda
game_kembar = game_azka.intersection(game_evan)
game_beda = len(game_beda)
print("game yg kembar", total_game_kembar," games ", game_kembar)
print("game yg beda", total_game_beda," games ", game_beda)


# key tidak boleh duplikat
koloksi_anime = {
    "re_zero": "subaru",
    "onepice": "usop",
    "waifu": {
        "re_zero": "rem-chan",
        "demon_slayer": "nezuko"
    }
}
print("koleksi anime:", koleksi_anime)
print("mc one pice:", koleksi_anime["onepice"])
print("waifu re zero:" koleksi_anime["waifu"]["re_zero"])