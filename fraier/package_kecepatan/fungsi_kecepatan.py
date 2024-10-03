konversi = {
    "m/s": {"nama": "Meter per detik (m/s)", "nilai": 1},
    "km/h": {"nama": "Kilometer per jam (km/h)", "nilai": 3.6},
    "mph": {"nama": "Mil per jam (mph)", "nilai": 2.23694},
    "knot": {"nama": "Knot", "nilai": 1.94384},
    "mach": {"nama": "Mach", "nilai": 0.00291545}
}

# Garis pinggir untuk mempercantik output
garis_pinggir = "=" * 50

# Fungsi untuk mengkonversi satuan kecepatan
def kecepatan(satuan1: str, satuan2: str, nilai: float):
    try:
        # Hitung hasil konversi dengan mengalikan nilai awal dengan nilai satuan1 kemudian dibagi nilai satuan2
        hasil = nilai * konversi[satuan1]["nilai"] / konversi[satuan2]["nilai"]
        # Format output dengan garis pinggir dan nilai yang dikonversi
        return f"""{garis_pinggir}
{nilai:.2f} {konversi[satuan1]["nama"]} = {hasil:.2f} {konversi[satuan2]["nama"]}
{garis_pinggir}"""
    except KeyError:
        # Jika input tidak valid, cetak pesan kesalahan
        return "Input tidak valid"
    

# Contoh penggunaan
# print(kecepatan("km/h", "m/s", 100))
# print(kecepatan("mph", "km/h", 60))
# print(kecepatan("m/s", "knot", 20))