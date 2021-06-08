import time
import cv2

daftar_judul = ["A Quiet Place Part 2", "Cruella", "The Unholy", "Invisible Hopes"]

informasi = [
    {"Usia": 13, "Harga": 70000, "Jenis": "Thriller"},
    {"Usia": 17, "Harga": 65000, "Jenis": "Comedy"},
    {"Usia": 18, "Harga": 55000, "Jenis": "Horror"},
    {"Usia": 17, "Harga": 60000, "Jenis": "Documentary"},
]

recommended = ["Yes", "No", "Yes", "No"]

jam_tayang = ["14.30", "16.40", "18.55", "21.00"]

# film A Quiet Place Part 2
studio_a = ["Studio 1", "Studio 2", "Studio 3", "Studio 4"]
# film Cruella
studio_b = ["Studio 2", "Studio 3", "Studio 4", "Studio 1"]
# film The Unholy
studio_c = ["Studio 3", "Studio 4", "Studio 1", "Studio 2"]
# film Invisible Hopes
studio_d = ["Studio 4", "Studio 1", "Studio 2", "Studio 3"]

# Menu utama yang dapat dipilih oleh pengguna
def menu_utama():
    try:
        print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
        print("1. NOW SHOWING")
        print("2. MOVIE RECOMMENDATIONS")
        print("3. INFORMATION")
        print("4. COUPON CODE")
        print("5. BUY TICKET")
        print("6. SYNOPSIS")
        print("7. SEE THE POSTER")
        print("0. EXIT")
        pilihan = int(input("PILIH : "))

        if pilihan == 1:
            now_showing()
        elif pilihan == 2:
            rec()
        elif pilihan == 3:
            informasi_film()
        elif pilihan == 4:
            code()
        elif pilihan == 5:
            pembelian()
        elif pilihan == 6:
            synopsis()
        elif pilihan == 7:
            movie_poster()
        elif pilihan == 0:
            exit()
        else:
            print("Pilihan Error")
            menu_utama()

    except ValueError:
        print("Pilihan Error")
        menu_utama()


# Menampilkan jam tayang dan judul film yang tersedia
def now_showing():
    i = 0
    j = 0
    a = 1

    print()
    while i < len(jam_tayang):
        print(str(a) + ")", jam_tayang[i])
        a += 1
        i += 1
    print()

    while j < len(daftar_judul):
        print("*", daftar_judul[j])
        j += 1

    print("=========================")
    milih_beli()


# Menampilkan daftar film yang direkomendasikan
def rec():
    i = 0

    print()
    print("=========================")
    print("==Movie Recommendations==")
    print("=========================")

    while i < len(recommended):
        if recommended[i] == "Yes":
            print(daftar_judul[i])
        i += 1

    print("=========================")
    menu_utama()


# Menampilkan informasi seputar film
def informasi_film():
    i = 0
    info = len(daftar_judul)

    print()
    while i < len(daftar_judul):
        for info in informasi:
            print(
                daftar_judul[i],
                "\nUsia",
                str(info["Usia"]) + "+ \nGenre :",
                str(info["Jenis"]),
                "\n=========================",
            )
            i += 1

    milih_beli()


# Menampilkan daftar kode kupon yang dapat digunakan
def code():
    print("=======Coupon Code=======")
    print("(1) NONTONBARENG")
    print("(2) CUMADIFOXID")
    print("(3) FOXIDAJA")
    menu_utama()


# Logika apakah akan melanjutkan pembelian tiket atau tidak
def milih_beli():
    try:
        print("Beli Tiket Sekarang?")
        print("1. Ya, 2. Tidak")
        jawab = int(input("= "))

        if jawab == 1:
            pembelian()
        elif jawab == 2:
            menu_utama()
        else:
            print("Pilihan Error")
            milih_beli()

    except ValueError:
        print("Pilihan Error")
        milih_beli()


# Menu pembelian tiket bioskop
def pembelian():
    i = 0
    a = 1

    print()
    while i < len(daftar_judul):
        print(str(a) + ")", daftar_judul[i])
        i += 1
        a += 1

    try:
        print()
        nonton = int(input("Mau nonton yang mana? "))

        if 0 < nonton < 5:
            nonton_a = nonton - 1
            harga = informasi[nonton_a]["Harga"]
            orang = int(input("Berapa tiket? "))
            beli = orang * harga
        else:
            print("Pilihan Error")
            pembelian()

    except ValueError:
        print("Pilihan Error")
        pembelian()

    # Memilih jam tayang dan studio
    def studio():
        i = 0
        a = 1

        while i < len(jam_tayang):
            print(str(a) + ")", jam_tayang[i])
            i += 1
            a += 1

        try:
            pilih_jam = int(input("Jam berapa? "))
            jam_index = pilih_jam - 1
            if nonton_a == 0:
                dapat_studio = studio_a[jam_index]
            elif nonton_a == 1:
                dapat_studio = studio_b[jam_index]
            elif nonton_a == 2:
                dapat_studio = studio_c[jam_index]
            elif nonton_a == 3:
                dapat_studio = studio_d[jam_index]
            else:
                print("Pilihan Error")
                studio()

        except ValueError:
            print("Pilihan Error")
            studio()

        kode_a = str(input("Masukkan Kode Diskon : "))
        kode = kode_a.upper()

        if kode == "FOXIDAJA" and beli > 215000:
            beli_update = beli - (beli * 0.3)
        elif kode == "CUMADIFOXID" and beli > 150000:
            beli_update = beli - (beli * 0.25)
        elif kode == "NONTONBARENG" and beli > 100000:
            beli_update = beli - (beli * 0.2)
        else:
            beli_update = 0

        print("\n=========================")
        print("===informasi pembelian===")
        print("=========================")
        print("Judul Film  :", daftar_judul[nonton_a])
        print("Genre       :", informasi[nonton_a]["Jenis"])
        print("Jam Tayang  :", jam_tayang[jam_index])
        print("Studio      :", dapat_studio)
        print("Total Tiket :", orang)

        if beli_update > 0:
            print("Total Harga : Rp.", int(beli))
            print("Total Harga (update): Rp.", int(beli_update))
        else:
            print("Total Harga : Rp.", int(beli))

        time.sleep(5)
        exit()

    studio()


# Menampilkan sinopsis dari film yang dipilih
def synopsis():
    print()
    print("=========================")
    i = 0

    while i < len(daftar_judul):
        print(i + 1, daftar_judul[i])
        i += 1

    try:
        print()
        sy = int(input("Synopsis : "))

        if sy == 1:
            with open("D:\Tubes\Quiet Pt 2.txt", "r") as docs:
                print(docs.read())
        elif sy == 2:
            with open("D:\Tubes\Cruella.txt", "r") as docs:
                print(docs.read())
        elif sy == 3:
            with open("D:\Tubes\The Unholy.txt", "r") as docs:
                print(docs.read())
        elif sy == 4:
            with open("D:\Tubes\Hopes.txt", "r") as docs:
                print(docs.read())
        else:
            print("Pilihan Error")
            synopsis()

    except ValueError:
        print("Pilihan Error")
        synopsis()

    menu_utama()


# Menampilkan poster film yang dipilih
def movie_poster():
    i = 0
    a = 1
    window_name = "MOVIE POSTER"

    print()
    print("=========================")
    print("0) MENU UTAMA")

    while i < len(daftar_judul):
        print(str(a) + ")", daftar_judul[i])
        i += 1
        a += 1

    try:
        print()
        poster = int(input("Pilihan : "))

        if poster == 0:
            menu_utama()
        elif poster == 1:
            old_img = cv2.imread("D:\Tubes\P1.jpg")
        elif poster == 2:
            old_img = cv2.imread("D:\Tubes\P2.jpg")
        elif poster == 3:
            old_img = cv2.imread("D:\Tubes\P3.jpg")
        elif poster == 4:
            old_img = cv2.imread("D:\Tubes\P4.jpg")
        else:
            print("Pilihan Error")
            movie_poster()

    except ValueError:
        print("Pilihan Error")
        movie_poster()

    img = cv2.resize(old_img, (400, 600))
    cv2.imshow(window_name, img)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(1)
    time.sleep(2)
    cv2.destroyAllWindows()
    movie_poster()


print("=-=-=-=-=-=-=-=-=-=-=-=-=")
print("         FOX ID")
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
menu_utama()
