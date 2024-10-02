# Project Kelompok 8

   Project ini adalah sebuah unit converter.
   Unit converter adalah sebuah alat yang membantu mengubah satuan pengukuran yang berbeda untuk berbagai kuantitas fisik. Dalam kasus Project ini, unit converter dapat mengubah satuan untuk:

   1. **Kecepatan** (misalnya dari km/jam ke hm/jam)
   2. **Berat** (misalnya dari kilogram ke gram)
   3. **Suhu** (misalnya dari Celsius ke Fahrenheit)
   4. **Jarak** (misalnya dari kilometer ke meter)
   5. **Waktu** (misalnya dari jam ke menit)

   Tujuannya adalah untuk memudahkan pengguna dalam mengubah satuan pengukuran yang berbeda, sehingga menjadi alat yang berguna untuk kehidupan sehari-hari atau untuk aplikasi ilmiah dan teknik.

# Cara penggunaanya

   1. **Satuan Berat**
   
       Untuk mengkonversi berat, Anda dapat menggunakan fungsi 'berat' dari modul 'convert'. Berikut adalah contoh cara penggunaannya:
       1. Import modul 'convert'

          ```python
              import convert
           ```
          
       2. Tentukan nilai berat yang ingin dikonversi,    
          serta satuan asli dan satuan yang akan dikonversi.
          Contoh:

          ```python
             from_unit = "g"  # satuan asli (gram):str
             to_unit = "kg"  # satuan yang akan dikonversi (kilogram):str
             nilai = 50  # nilai berat dalam gram yang akan dikonversi ke kilogram:float
           ```
          
       3. Panggil fungsi berat dengan parameter 'from_unit', 'to_unit', dan 'nilai':

          ```python
             hasil = convert.berat(from_unit, to_unit, nilai)
           ```
          
       4. Cetak hasil konversi:

          ```python
              print(f"{nilai} {from_unit} adalah {hasil} {to_unit}")

              Output:
              50 g adalah 0.05 kg
           ```

