## Link

Heroku App Link : https://reyvan-pbp-tugas2.herokuapp.com/katalog/

## Bagan

![BAGAN](/katalog/bagan.png)

## Implementasi poin 1 sampai dengan 4

1. Pada views.py, menginisialisasi fungsi show_katalog yang menerima parameter request dan akan me-return render(request, "katalog.html", context), dan mengimport CatalogItem dari models.py untuk memghasilkan html.

2. Me-routing pada url.py dengan membuat fungsi show_katalog dari views.py agar dapat menampilkan katalog.html pada browser. Routing dilakukan dengan menambahkan path show_katalog pada urlpatterns

3. Dilakukan mapping data katalog pada katalog.html yang dirender pada views. Ini dibuat dalam bentuk table dengan mengubah template dari katalog.html .

4. Melakukan deployment pada Heroku setelah menambahkan API dan app name dari aplikasi Heroku ke dalam repository secret github.
