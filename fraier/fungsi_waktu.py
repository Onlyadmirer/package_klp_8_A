#Mengubah Satuan Detik ke Satuan yang diinginkan
def detikToMenit(detik): # Mengubah Detik ke Menit
    return detik / 60
    
def detikToJam(detik): # Mengubah Detik ke Jam
    return detik / 3600
    
def detikToHari(detik): # Mengubah Detik ke Hari
    return detik / 86400

#Mengubah Satuan Menit ke Satuan yang diinginkan
def menitToDetik(menit): # Mengubah Menit ke Detik
    return menit * 60
    
def menitToJam(menit): # Mengubah Menit ke Jam
    return menit / 60
    
def menitToHari(menit): # Mengubah Menit ke Hari
    return menit / 1440

#Mengubah Satuan Jam ke Satuan yang diinginkan
def jamToDetik(jam): # Mengubah Jam ke Detik
    return jam * 3600
    
def jamToMenit(jam): # Mengubah Jam ke Menit
    return jam * 60
    
def jamToHari(jam): # Mengubah Jam ke Hari
    return jam / 24

#Mengubah Satuan Hari ke Satuan yang diinginkan
def hariToDetik(hari): # Mengubah Hari ke Detik
    return hari * 86400
    
def hariToMenit(hari): # Mengubah Hari ke Menit
    return hari * 1440
    
def hariToJam(hari): # Mengubah Hari ke Jam
    return hari * 24
