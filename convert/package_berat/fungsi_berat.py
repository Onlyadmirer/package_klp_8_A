# Definisikan kamus konversi satuan berat
# Kamus ini berisi pasangan key-value, di mana key adalah singkatan satuan berat
# dan value adalah dictionary yang berisi nama satuan berat dan nilai konversinya
konversi = {
    "mg": {"nama": "Miligram(mg)", "nilai": 1},
    "cg": {"nama": "Centigram(cg)", "nilai": 10},
    "dg": {"nama": "Desigram(dg)", "nilai": 100},
    "g": {"nama": "Gram(g)", "nilai": 1000},
    "dag": {"nama": "Dekagram(dag)", "nilai": 10000},
    "hg": {"nama": "Hektogram(hg)", "nilai": 100000},
    "kg": {"nama": "Kilogram(kg)", "nilai": 1000000},
    "ton": {"nama": "Ton", "nilai": 1000000000}
}
# Garis pinggir untuk mempercantik output
garis_pinggir = "=" * 44

# Fungsi untuk mengkonversi satuan berat
def berat(satuan1:str, satuan2:str, nilai:float):
    try:
        # Hitung hasil konversi dengan mengalikan nilai awal dengan nilai satuan1 kemudian dibagi dengan nilai satuan 2
        hasil = nilai * konversi[satuan1]["nilai"] / konversi[satuan2]["nilai"]
        # Format output dengan garis pinggir dan nilai yang dikonversi
        return f"""{garis_pinggir} 
    {nilai:,} {konversi[satuan1]["nama"]} = {hasil:,} {konversi[satuan2]["nama"]}
{garis_pinggir}"""
    except KeyError:
        # Jika input tidak valid, cetak pesan kesalahan
        print("input tidak valid")
        
    
