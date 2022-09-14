## Link

Heroku App Link : https://reyvan-pbp-tugas2.herokuapp.com/katalog/

## Keterkaitan antara urls.py, views.py, models.py, dan berkas html

![BAGAN](/katalog/bagan.png)

Dalam mengakses app Django, browser akan mengirim request ke server Django dan server Django akan mengambil urls.py untuk menentukan path selanjutnya. Dalam urls.py akhirnya terdapat path yang menunjuk ke fungsi yang terdapat pada views.py yang akan memunculkan file html. models.py menyimpan atribut dan perilaku penting dari data yang kita simpan, dan pada umumnya views.py menyimpan satu table database berdasarkan models.py untuk dipetakan ke file html. Terakhir, file html dikirim kembali ke client.

## Implementasi poin 1 sampai dengan 4

1. Pada views.py, menginisialisasi fungsi show_katalog yang menerima parameter request dan akan me-return render(request, "katalog.html", context), dan mengimport CatalogItem dari models.py untuk memghasilkan html.

2. Me-routing pada url.py dengan membuat fungsi show_katalog dari views.py agar dapat menampilkan katalog.html pada browser. Routing dilakukan dengan menambahkan path show_katalog pada urlpatterns

3. Dilakukan mapping data katalog pada katalog.html yang dirender pada views. Ini dibuat dalam bentuk table dengan mengubah template dari katalog.html .

4. Melakukan deployment pada Heroku setelah menambahkan API dan app name dari aplikasi Heroku ke dalam repository secret github.

## Kenapa menggunakan virtual environment?

Virtual environtment dapat membuat environment yang terisolasi dari environment lainnya. Ini berguna karena mampu mencegah terjadinya tabrakan antar package yang diinstall yang umumnya disebabkan oleh perbedaan versi dependency/library
