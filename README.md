**Tahapan Implementasi Tugas 2**

1. Inisialisasi proyek Django baru
   Saya memulai dengan membuat repositori GitHub baru yang bernama galacticos-shop. Repositori ini kemudian saya
   clone ke lokal agar bisa saya kerjakan juga dari komputer saya via IDE VSCode. Kemudian, agar
   environment proyek terisolasi, saya membuat dan mengaktifkan virtual environment. Dengan cara ini,
   dependency proyek tidak bercampur dengan dependency lain di komputer saya. Selanjutnya, saya menginstall
   kebutuhan awal termasuk Django. Proyek Django dibuat dengan perintah django-admin startproject
   galacticos_shop .. Setelah itu, struktur dasar Django otomatis terbentuk. Saya juga membuat file .env
   dan .env.prod untuk menyimpan variabel environment, baik untuk development maupun deployment ke PWS.
   File .gitignore ditambahkan agar file sensitif (seperti .env) tidak ikut terupload ke GitHub saat push.
   Di bagian settings.py saya juga melakukan beberapa penyesuaian, termasuk menambahkan konfigurasi
   (PRODUCTION, ALLOWED_HOSTS, dll) yang mendukung deployment.

2. Membuat aplikasi dengan nama 'main'
   Saya menjalankan perintah python manage.py startapp main. Django otomatis membuat folder dan file dasar
   aplikasi main (models.py, views.py, dll). Supaya aplikasi dikenali, saya menambahkan "main" ke dalam list
   INSTALLED_APPS di settings.py.
   
3. Melakukan routing proyek
   Saya membuka file urls.py pada direktori proyek galacticos_shop, lalu menambahkan fungsi include. Saya
   juga menambahkan path ke aplikasi main dengan path('', include('main.urls')). Dengan begitu aplikasi
   main bisa langsung diakses pada halaman utama.
   
4. Membuat model Product pada aplikasi main
   Di dalam file models.py aplikasi main, saya membuat model bernama Product.
   Atribut wajib yang saya buat adalah:
   name = models.CharField(max_length=255)
   price = models.IntegerField()
   description = models.TextField()
   thumbnail = models.URLField()
   category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
   is_featured = models.BooleanField(default=False)

   Selain atribut wajib, saya juga menambahkan atribut tambahan:
   stock = models.PositiveIntegerField(default=0)
   brand = models.CharField(max_length=100, blank=True, null=True)
   rating = models.FloatField(default=0.0)

   Setelah itu saya menjalankan python manage.py makemigrations untuk membuat file migrasi, lalu
   python manage.py migrate untuk menerapkan perubahan ke database.
   
5. Membuat fungsi pada views.py
   Saya membuat fungsi bernama show_main di views.py. Fungsi ini mengembalikan template HTML bernama
   main.html menggunakan render. Context yang saya kirim ke template berisi identitas saya (nama, npm, dan
   kelas).
   
6. Membuat template main.html
   Saya membuat folder templates di dalam aplikasi main, lalu menambahkan file main.html. Di dalamnya
   saya menuliskan teks sederhana yang menampilkan nama aplikasi, tulisan welcome, logo Real Madrid,
   serta data identitas saya. Saya juga menambahkan sedikit styling agar tampilannya lebih rapi dan
   menarik.
   
7. Membuat routing pada urls.py pada main (aplikasi)
   Saya membuat berkas file urls.py di dalam folder aplikasi main. Di dalam urls.py, saya mengimpor
   fungsi show_main dari views.py. Saya kemudian membuat urlpatterns dengan path('', show_main,
   name='show_main') sehingga ketika aplikasi dijalankan, halaman utama menampilkan template main.html.
   
8. Melakukan deployment ke PWS
   Saya login ke PWS menggunakan SSO UI. Lalu, membuat proyek baru dengan schema tugas_individu.
   Variabel environment saya isi dengan menyalin isi dari .env.prod. Di settings.py, saya menambahkan
   URL PWS ke dalam ALLOWED_HOSTS. Setelah itu saya melakukan git add, git commit, lalu git push origin
   master agar perubahan tersimpan juga di GitHub. Untuk deployment, saya menjalankan perintah yang diberikan
   oleh PWS, yaitu add remote pws lalu git push pws master. Setelah langkah-langkah tersebut
   selesai, aplikasi saya bisa diakses melalui tautan berikut:
   https://nicholas-vesakha-galacticosshop.pbp.cs.ui.ac.id/

**Bagan Request Client dan Penjelasan**
Bagan yang sudah saya buat dapat diakses melalui tautan berikut: ristek.link/BaganTugas2

Berdasarkan bagan alur yang telah dibuat, proses interaksi antara pengguna dengan aplikasi Galacticos Shop 
dapat dijelaskan sebagai berikut.

Pertama, Browser (User) mengirimkan sebuah request, misalnya ketika membuka halaman utama aplikasi. 
Request ini kemudian diterima oleh Web Server (seperti Nginx atau Apache) yang bertugas meneruskan 
permintaan tersebut ke WSGI (wsgi.py). WSGI berfungsi sebagai jembatan antara web server dengan 
aplikasi Django. Pada tahap ini, sebenarnya request juga dapat melewati middleware sebelum diteruskan 
ke aplikasi main. Selanjutnya, request akan masuk ke urls.py. File ini berfungsi untuk melakukan URL 
routing, yaitu mencocokkan alamat URL yang diminta pengguna dengan pola URL (URL patterns) yang sudah 
didefinisikan. Jika tidak ditemukan kecocokan, Django akan secara otomatis mengembalikan error misalnya 
404 Page Not Found. Apabila pola URL cocok, request diteruskan ke views.py. File ini berisi logika 
aplikasi yang mengatur bagaimana data diproses dan apa yang harus ditampilkan ke pengguna. Pada kasus 
tertentu, views.py juga akan berkomunikasi dengan models.py apabila diperlukan data dari Database.
 
Model yang digunakan dalam project ini adalah Product, yang mendefinisikan struktur data seperti nama 
produk, harga, deskripsi, kategori, hingga atribut tambahan seperti stok, brand, dan rating. Proses ini 
memungkinkan aplikasi untuk mengambil, menyimpan, memperbarui, maupun menghapus data produk. Setelah data 
berhasil diproses, views.py akan memanggil template (main.html). Template ini berfungsi sebagai kerangka 
tampilan yang akan dirender menjadi halaman HTML. Dengan memanfaatkan context dari views.py, data dapat 
ditampilkan secara dinamis kepada pengguna. Tahap akhir adalah Response, yaitu hasil render template 
dalam bentuk halaman HTML. Response inilah yang kemudian dikirimkan kembali ke browser pengguna untuk ditampilkan. 
Selain itu, pada bagan juga ditunjukkan mekanisme Error Handling. Jika pada tahap urls.py tidak ditemukan URL yang 
sesuai, maka akan dikembalikan error 404 Not Found. Sementara itu, jika terjadi kesalahan logika dalam views.py atau 
ada error pada query database, maka Django akan memberikan error 500 Server Error.

**Peran settings.py**
Pada Django, settings.py berfungsi sebagai pusat konfigurasi utama yang mengatur cara kerja proyek. 
Di dalam file ini biasanya terdapat berbagai pengaturan penting mulai dari keamanan, aplikasi yang 
digunakan, hingga konfigurasi database. Pada proyek Galacticos Shop, beberapa hal yang diatur di dalam 
settings.py antara lain:
- File ini memuat SECRET_KEY yang bersifat rahasia dan digunakan untuk keamanan internal Django,
  serta pengaturan DEBUG yang biasanya hanya diaktifkan pada tahap development. Pada bagian ALLOWED_HOSTS,
  sudah ditambahkan domain proyek yaitu nicholas-vesakha-galacticosshop.pbp.cs.ui.ac.id, sehingga aplikasi
  bisa diakses melalui tautan PWS selain dari localhost.
- Melalui INSTALLED_APPS, Django mengetahui aplikasi bawaan maupun aplikasi buatan sendiri yang aktif,
  misalnya aplikasi main yang dibuat pada proyek ini. Bagian MIDDLEWARE juga terdapat di dalam settings.py,
  yang berfungsi sebagai lapisan perantara untuk memproses request dan response, seperti misalnya middleware
  keamanan, sesi, autentikasi, hingga proteksi CSRF.
- settings.py juga mendefinisikan konfigurasi routing proyek lewat ROOT_URLCONF dan sistem template yang
  digunakan untuk menampilkan halaman HTML dari aplikasi. Selain itu, ada juga pengaturan WSGI_APPLICATION
  yang menjadi pintu masuk komunikasi antara web server dengan aplikasi Django.
- Hal penting lainnya adalah konfigurasi Database. Proyek ini dibuat agar bisa berjalan di dua mode:
  development dan production. Jika variabel PRODUCTION bernilai True, maka Django seharusnya akan menggunakan
  PostgreSQL dengan kredensial yang diambil dari environment variables (.env). Namun jika tidak, maka
  Django otomatis menggunakan SQLite yang lebih sederhana untuk development. Dengan cara ini,
  pengembangan dan deployment bisa berjalan lebih fleksibel.
- Di bagian AUTH_PASSWORD_VALIDATORS, settings.py juga mengatur aturan validasi password agar sistem
  login lebih aman. Sementara itu, Internationalization diatur melalui LANGUAGE_CODE dan TIME_ZONE.
  Pada proyek ini digunakan bahasa Inggris (en-us) dan zona waktu UTC.
- Terakhir, settings.py juga mengatur path untuk file statis seperti CSS, JavaScript, atau gambar
  melalui STATIC_URL, serta menentukan tipe default primary key field menggunakan DEFAULT_AUTO_FIELD.
  
Secara keseluruhan, tanpa settings.py Django tidak akan mengetahui bagaimana aplikasi dijalankan,
database mana yang digunakan, aplikasi apa saja yang aktif, serta bagaimana request dari pengguna harus
diproses.

**Cara Migrasi Database Django**
Migrasi database di Django berfungsi untuk menjembatani perubahan yang dibuat pada file models.py 
dengan struktur database yang sebenarnya. Dengan adanya mekanisme ini, setiap penambahan, penghapusan, 
atau modifikasi atribut pada model dapat langsung diterapkan ke dalam tabel database tanpa perlu menulis 
perintah SQL secara manual.

Prosesnya dimulai dengan menjalankan perintah python manage.py makemigrations. Perintah ini membuat 
file migrasi baru yang berisi catatan perubahan terhadap model, misalnya menambahkan field baru, 
mengubah tipe data, atau membuat tabel produk. File migrasi tersebut pada dasarnya berisi instruksi 
yang nantinya akan diterjemahkan Django menjadi perintah SQL.

Setelah file migrasi terbentuk, perintah python manage.py migrate dijalankan untuk benar-benar menerapkan 
perubahan tersebut ke database. Pada tahap ini Django akan membaca file migrasi yang sudah ada, lalu 
mengeksekusi perintah SQL agar struktur database sesuai dengan definisi model yang terbaru.

Django juga menyimpan catatan setiap migrasi yang berhasil dijalankan dalam sebuah tabel khusus bernama 
django_migrations. Catatan ini penting karena dengan begitu Django dapat mengetahui migrasi mana saja 
yang sudah diterapkan dan migrasi baru apa yang masih perlu dieksekusi. Dengan sistem ini, proses 
pengembangan menjadi lebih fleksibel dan aman, terutama ketika bekerja dalam tim atau saat memindahkan 
aplikasi ke lingkungan berbeda.

**Mengapa Framework Django Dijadikan Permulaan Pembelajaran**
Menurut saya, Django adalah framework yang sangat cocok digunakan untuk memulai perjalanan 
dalam web development karena memberikan kemudahan bagi pemula maupun developer yang
sudah berpengalaman. Django dilengkapi dengan banyak fitur bawaan yang siap pakai, seperti sistem 
autentikasi, manajemen URL, Object-Relational Mapping (ORM), hingga dukungan untuk membuat API. 

Hal ini membuat proses pengembangan lebih cepat karena pengembang tidak perlu membangun semuanya 
dari awal. Selain itu, Django menggunakan bahasa Python yang terkenal lebih sederhana, mudah dibaca, 
serta memiliki library yang sangat lengkap sehingga logika aplikasi dapat ditulis dengan lebih ringkas 
dan jelas.

Sebagai framework open source, Django didukung oleh komunitas yang sangat aktif. Kehadiran 
komunitas ini membuat pengguna lebih mudah menemukan dokumentasi, tutorial, maupun solusi jika 
menghadapi kendala/bug. Django juga menerapkan pola arsitektur MVT (Model-View-Template) yang rapi sehingga 
alur kerja proyek menjadi lebih terstruktur dan mudah dipahami. Dari sisi keamanan, Django juga sudah memiliki 
proteksi bawaan terhadap ancaman umum seperti SQL injection, XSS, dan CSRF, sehingga developer dapat lebih 
fokus membangun fitur inti aplikasi. Fleksibilitas Django pun menjadi nilai tambah karena mendukung 
berbagai jenis database dan mampu diandalkan, baik untuk proyek kecil dengan sedikit pengguna maupun 
aplikasi besar dengan trafik yang cukup tinggi.

**Feedback untuk Asisten Dosen pada Tutorial 1**
Menurut saya, asisten dosen pada tutorial 1 sudah sangat baik dan membantu, khususnya Kak Danniel. Semua penjelasan jelas, 
interaktif, dan kehadiran asisten dosen di Discord juga memudahkan untuk bertanya kapan saja. Overall, saya merasa terbantu 
dan tidak ada kendala yang signifikan sejauh ini.
