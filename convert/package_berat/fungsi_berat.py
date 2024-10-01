
print("""============================================================================
|                         KONVERSI SATUAN BERAT                            |
|           Konversi dari satuan berat ke satuan berat lainnya.            |
============================================================================""")

# Mendefinisikan sebuah dictionary konversi yang berisi nama-nama satuan berat dan nilai-nilai konversinya
konversi = {
    1: {'nama': 'Miligram(mg)', 'nilai': 1},
    2: {'nama': 'Centigram(cg)', 'nilai': 10},
    3: {'nama': 'Desigram(dg)', 'nilai': 100},
    4: {'nama': 'Gram(g)', 'nilai': 1000},
    5: {'nama': 'Dekagram(dag)', 'nilai': 10000},
    6: {'nama': 'Hektogram(hg)', 'nilai': 100000},
    7: {'nama': 'Kilogram(kg)', 'nilai': 1000000},
    8: {'nama': 'Ton', 'nilai': 1000000000}
}

# Mendefinisikan sebuah fungsi berat yang menghitung hasil konversi satuan berat
def berat(angka_satuan, angka, angka_satuan2):
    try:
        # menghitung hasil konvert
        hasil = angka * konversi[angka_satuan]['nilai'] / konversi[angka_satuan2]['nilai']
        return hasil
    except KeyError:
        # mencetak pesan error
        print("pilihan tidak valid. coba lagi")
        return None
    
# Meminta user untuk memilih satuan berat yang ingin dikonversi
angka_satuan = int(input("""1. Miligram                 5. Dekagram
2. Centigram                6. hektogram
3. Desigram                 7. kilogram
4. gram                     8. ton

* Pilih satuan berat yang ingin di konversi (Cth: pilih 1 untuk miligram) :"""))

# Meminta user untuk memasukkan nilai yang ingin dikonversi
angka = float(input("* Pilih jumlah nilai yang ingin di konversi (angka) :"))

# Meminta user untuk memilih satuan berat tujuan konversi
angka_satuan2 = int(input("* Pilih satuan berat tujuan konversi (Cth: pilih 3  untuk desigram) :"))

# Memanggil fungsi berat dengan argumen-argumen yang diinput oleh user
hasil = berat(angka_satuan, angka, angka_satuan2)

# Mencetak hasil konversi jika fungsi berat mengembalikan nilai yang tidak None
if hasil is not None:
    print(f"    => {angka:,} {konversi[angka_satuan]['nama']} = {hasil:,} {konversi[angka_satuan2]['nama']}")
    
print("""============================================================================
|                             TERIMA KASIH                                 |
============================================================================""")