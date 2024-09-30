# project_klp.8_package

# Repositori Tugas Package Kelompok 8

## Requirements:
1. Buat akun GitHub (https://github.com/)
2. Download Git (https://git-scm.com/)

## Cara mengirim file ke repositori ini:

1. **Fork** repositori ini

2. **Clone** repositori hasil **fork** anda

    ```sh

    git clone https://github.com/YOUR_USERNAME/project_klp.8_package.git

    ```

3. Setelah anda **clone**, masuk ke folder hasil **clone** tersebut lalu buat **branch** dengan nama **NAMA** anda

    ```sh

    cd project_klp.8_package
    git branch NAMA_ANDA
    git checkout NAMA_ANDA
    git config user.name USERNAME_GITHUB
    git config user.email EMAIL_GITHUB

    ```

4. Setelah anda pindah ke **branch** yang telah anda buat, buat sebuah folder dengan nama **FILE** anda dan masuk ke folder tersebut.
    ```sh

    mkdir NAMA_ANDA
    cd NAMA_ANDA

    ```


5. Didalam folder tersebut, buat sebuah folder dengan nama **Package-n**, **n** = Program yang anda buat
    ```sh

    mkdir "Package-n"
    cd "Package-n"

    CATATAN: n DI SINI ADALAH NAMA PROGRAM YANG ANDA BUAT
    CONTOH: Package-Waktu

    ```

6. Semua _file_ untuk tugas Package-**n**, disimpan kedalam folder **Package-n**
7. Setiap membuat _file_ atau melakukan perubahan, lakukan proses **commit** dengan pesan yang deskriptif

8.  Setelah package anda disetujui, **push** seluruh _file_ yang telah anda buat

    ```sh

    # pastikan proses commit telah selesai terhadap setiap file
    git push origin NAMA_ANDA


    ```

9.  Masuk ke akun GitHub anda, dan buka repo yang telah anda **fork** dan **clone**. Lihat perubahan yang terjadi pada repo tersebut dan pastikan bahwa file yang 
    telah anda **push** sesuai dan berada pada repo tersebut.

10.  Pilih menu **Pull request** dan lakukan **pull request** pada tugas package anda.
