## Link

Heroku App Link : reyvan-pbp-tugas2.herokuapp.com/todolist/

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
