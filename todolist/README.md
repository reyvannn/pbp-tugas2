## Link

Heroku App Link : [https://reyvan-pbp-tugas2.herokuapp.com/todolist/](https://reyvan-pbp-tugas2.herokuapp.com/todolist/)

# TUGAS 4
## Apa Kegunaan {% csrf_token %} pada <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut
Token CSRF ini dipakai untuk mencegah CSRF atau Cross Site Request Forgery, yaitu hacker melakukan tindakan pada situs yang sudah diautentikasi korban tanpa sepengetahuannya. Server akan memvalidasi token ini untuk mencegah hacker. Fitur ini wajib diimplementasikan pada Django, jika tidak diimplementasikan maka website tidak akan jalan.

## Apakah kita dapat membuat elemen <form> secara manual?
Elemen <form> bisa dibuat dengan tag input HTML

## Jelaskan proses alur data dari submisi, penyimpanan data, hingga muncul pada template!

User akan mengisi data. Kemudian menekan tombol submit, maka data akan di POST ke server. Data kemudian diolah oleh fungsi di file views.py. Terakhir, data ditampilkan sesuai dengan template HTML

## Pengimplementasian Checklist

1. Buat app todolist dengan menjalankan command python manage.py startapp todolist. 
2. Tambahkan path serta url di direktori project_django dan direktori todolist. 
3. Buat model yang sesuai kebutuhan di models.py
4. Tambahkan fitur register, login dan logout di views.py
5. Buat fungsi yang menampilkan task dan buat template htmlnya
6. Buat fungsi yang menambahkan task dan buat template htmlnya
7. Migrate dan deploy aplikasi

Akun dummy pengguna:
* username: tes1
* password: qwertytes1

* username: tes2
* password: qwertytes2

# TUGAS 5
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline: Styling dilakukan di dalam masing-masing tag HTML
      * Kelebihan: Berguna jika kita ingin mengubah style dari elemen spesifik
      * Kekurangan: Membutuhkan waktu yang lama jika file htmlnya besar 
       
Internal: Styling dilakukan di dalam file HTML, dengan menggunakan tag <style></style>
      * Kelebihan: Lebih cepat daripada inline CSS bagi proyek yang memerlukan sedikit file HTML.
      * Kekurangan: Membutuhkan banyak waktu untuk menambahkan style pada proyek berskala besar

Eksternal: Styling dilakukan di luar file HTML pada suatu file .css
      * Kelebihan: Lebih efisien untuk proyek berskala besar, karena kita bisa mengubah style dari situs hanya  
       dengan 1 file CSS, sehingga lebih scalable.
      * Kekurangan: Perlu didownload terlebih dahulu sehingga bisa memperbanyak HTTP 'GET' request jika tidak dipantau

## Jelaskan tag HTML5 yang kamu ketahui.
1. < title> untuk judul.
2. < a> untuk membuat link ke url lain.
3. < br> memunculkan line break.
4. < head> menyimpan metadata.
5. < h1> - < h6> text heading.
6. < div> generic division.
7. < form> interface untuk menerima input
8. < button> button
9. < body> menyimpan seluruh konten dari html

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* Element selector
Syntax: "namaElemen{}"
* Class selector
Syntax: ".namaClass{}"
* ID selector
Syntax: "#ID"

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Inisialisasi bootstrap pada base.html
2. Kustomisasi create-task.html, todolist.html, login.html, dan register.html
