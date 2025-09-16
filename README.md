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

------------------------------------------------------------------------------------------------------------------------------
**[Tugas Individu 3]**

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Dalam mengimplementasikan sebuah platform, konsep data delivery sangat diperlukan karena data delivery merupakan proses bagaimana 
data dikirim atau didistribusikan hingga dapat digunakan oleh user maupun sistem lain dengan cara yang tepat, cepat, dan aman. 
Data delivery memastikan agar platform dapat menyajikan dan menerima data dari user dengan lancar, contohnya pada platform 
Galacticos Shop saya yang menampilkan data produk, seperti jersey dan bola resmi Real Madrid yang sudah di add product sebelumnya. 
Dalam pengembangan sebuah platform biasanya ada banyak komponen yang saling membutuhkan data, misalnya data produk diambil oleh views.py 
lalu dikirim ke halaman HTML, atau bisa juga diakses dalam format JSON dan XML untuk keperluan integrasi. Dengan adanya data delivery, 
semua komponen bisa menerima data yang sama, terbaru, dan konsisten. Jika data delivery tidak berjalan baik, tentu saja distribusi informasi 
dapat menjadi lambat, tidak sinkron, atau bahkan salah, terutama pada platform yang membutuhkan data secara real-time, sehingga bisa 
menurunkan pengalaman pengguna. Selain itu, pengiriman data yang terstruktur juga membantu menghindari redundansi dan meminimalkan 
beban sistem akibat data yang dikirim berulang-ulang. Data delivery juga memungkinkan platform terhubung dengan sistem eksternal 
seperti layanan pembayaran, karena sistem tersebut memerlukan data yang konsisten dan tepat waktu agar transaksi dapat berhasil. 

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
XML dan JSON sama-sama merupakan format yang digunakan untuk mengirim dan menyimpan data, tetapi keduanya memiliki karakteristik yang 
agak berbeda. XML menggunakan struktur berbasis tag seperti HTML, sehingga bersifat lebih verbose (panjang dan banyak simbol). 
JSON menggunakan struktur berbasis pasangan key-value yang lebih sederhana, ringkas, dan menurut saya lebih mudah dipahami. 
Lalu, setahu saya JSON lebih ringan, ukuran data yang dikirim juga menjadi lebih kecil, sehingga proses transfer data menjadi lebih cepat. 
Selain itu, JSON lebih mudah dibaca oleh manusia dan dapat langsung diproses oleh JavaScript tanpa perlu parsing tambahan, sedangkan XML 
butuh parser khusus untuk mengolah datanya. JSON juga memiliki sintaks yang lebih sederhana sehingga memudahkan proses ketika debugging 
dan proses development, sedangkan XML dipakai kalau data rumit (banyak atribut) dan harus patuh pada aturan format tertentu. Namun, dalam 
webdev modern, JSON jauh lebih populer karena efisien, cepat, dan sudah didukung secara native oleh hampir semua bahasa pemrograman modern 
dan API web. Akibat alasan-alasan itulah JSON umumnya dianggap lebih baik untuk kebutuhan pertukaran data antar sistem dalam pengembangan 
platform saat ini.

**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Method is_valid() pada form Django memiliki fungsi utama untuk mengecek apakah data yang dikirimkan ke form sudah sesuai dengan aturan 
validasi yang telah ditentukan sebelumnya pada form atau model. Ketika pengguna memasukkan data, developer biasanya sudah mendefinisikan 
terlebih dahulu field apa saja yang diperbolehkan, tipe data yang benar, serta batasan-batasan tertentu. Misalnya, untuk sebuah form produk, 
developer dapat menentukan bahwa field name wajib diisi dengan teks, price harus berupa angka, dan description tidak boleh kosong. Saat method 
is_valid() dijalankan, Django akan melakukan serangkaian pemeriksaan mulai dari memastikan bahwa semua field yang wajib diisi tidak dibiarkan 
kosong, memvalidasi kesesuaian tipe data yang dimasukkan dengan tipe data yang diharapkan, hingga memeriksa aturan tambahan yang diberikan 
melalui validator, seperti panjang minimal suatu input atau rentang nilai tertentu. Apabila semua validasi berhasil dipenuhi, maka is_valid() 
akan mengembalikan nilai True dan data tersebut dianggap sah untuk diproses lebih lanjut, sedangkan jika ada kesalahan maka akan mengembalikan 
nilai False dan Django secara otomatis menghasilkan pesan error yang dapat ditampilkan kepada user via browser agar mereka mengetahui letak 
kesalahan input yang mereka lakukan. Keberadaan method ini sangat penting karena membantu menjaga kualitas dan konsistensi data yang masuk ke 
sistem, mencegah adanya kerusakan atau error pada DB akibat input data yang tidak valid, serta meningkatkan pengalaman pengguna karena mereka 
akan mendapatkan umpan balik langsung apabila data yang dikirimkan tidak sesuai dengan aturan. 

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
csrf_token pada Django adalah mekanisme keamanan yang berfungsi untuk melindungi aplikasi dari serangan yang bernama CSRF (Cross-Site Request Forgery). 
Token ini berupa nilai unik, rahasia, dan tidak bisa ditebak yang dibuat oleh server lalu disimpan di sesi pengguna. Setiap kali pengguna mengirimkan 
form, token ini ikut dikirim bersama data form sehingga server bisa memverifikasi apakah request benar-benar berasal dari pengguna yang sedang login, 
bukan dari pihak lain. Jika token yang dikirim sesuai dengan token yang tersimpan di sisi server, maka request dianggap valid, sedangkan jika tidak 
sesuai maka request otomatis ditolak. Dengan cara ini, Django dapat memastikan bahwa setiap aksi sensitif yang dilakukan pengguna seperti login, mengubah 
profil, atau melakukan transaksi hanya bisa diproses jika permintaan tersebut benar-benar sah. Jika kita tidak menambahkan csrf_token ke dalam form Django, 
tentu aplikasi akan terbuka terhadap serangan CSRF. Dalam serangan semacam ini, penyerang memanfaatkan fakta bahwa browser secara otomatis mengirimkan 
cookie sesi pada setiap request ke domain tertentu. Artinya, jika seorang pengguna sedang login di sebuah aplikasi web tanpa perlindungan CSRF, penyerang 
bisa membuat halaman berbahaya yang diam-diam mengirimkan request ke aplikasi tersebut menggunakan cookie milik korban. Server akan salah mengira bahwa request 
tersebut berasal dari korban padahal sebenarnya dipicu oleh penyerang. Akibatnya, korban bisa saja tanpa sadar melakukan aksi yang tidak diinginkan, misalnya 
mengganti password email, mengirim pesan, atau bahkan melakukan transaksi finansial. Kondisi ini dapat dimanfaatkan penyerang dengan menyisipkan form tersembunyi 
atau script otomatis di sebuah situs jebakan. Ketika korban yang sedang login ke aplikasi target mengunjungi situs jebakan tersebut, browser korban akan secara 
otomatis mengirimkan request ke server aplikasi target lengkap dengan cookie sesi korban. Tanpa adanya csrf_token, server tidak memiliki mekanisme untuk membedakan 
apakah request itu benar-benar dibuat oleh korban atau dimanipulasi oleh pihak lain. Hal ini bisa berujung pada pencurian hak akun, perubahan data penting, 
hingga kerugian secara finansial (pembobolan e-bank, aplikasi saham, dll). Penggunaan csrf_token sangat penting dalam Django karena berfungsi sebagai pengaman 
tambahan yang memastikan hanya request sah dari pengguna yang benar-benar diproses. Tanpa lapisan ini, aplikasi web akan sangat rentan dieksploitasi melalui 
serangan CSRF yang dapat menimbulkan dampak serius bagi pengguna dan juga sistem.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**
Pertama, saya melihat kembali model Product di models.py yang menyimpan data produk bertema Real Madrid (Galacticos Shop). Model ini memiliki beberapa field 
seperti name, price, description, thumbnail, category, is_featured, stock, brand, dan rating. Model ini menjadi dasar dari data yang akan ditampilkan atau 
ditambahkan pada platform yang saya kembangkan.

Setelah itu, saya menambahkan empat fungsi views baru di views.py untuk menampilkan data dalam format XML dan JSON.
Sebelum membuat fungsi, saya mengimpor Product, HttpResponse, dan serializers dari Django. Saya membuat fungsi show_xml untuk mengembalikan semua data produk 
dalam format XML, dan show_json untuk mengembalikan semua data produk dalam format JSON. Kemudian saya membuat fungsi show_xml_by_id dan show_json_by_id untuk 
menampilkan data produk berdasarkan id yang diberikan, masing-masing dalam format XML dan JSON.

Langkah berikutnya adalah membuat routing URL di urls.py. Saya mengimpor keempat fungsi views yang sudah dibuat, kemudian menambahkan keempat path baru (show_xml/, 
show_json/, show_xml/<id>, show_json/<id>) ke dalam urlpatterns. Dengan begitu, setiap fungsi view tersebut bisa diakses melalui URL masing-masing.

Setelah data bisa diakses, saya membuat halaman utama yang menampilkan semua produk dan memiliki tombol untuk menambahkan produk baru (+ Add Product) serta melihat 
detail produk (View Detail). Saya membuat folder templates dan menambahkan file base.html sebagai kerangka umum tampilan HTML. Kemudian,saya menambahkan path 
templates ke dalam TEMPLATES di settings.py agar dikenali oleh Django.

Lalu, saya membuat file forms.py di direktori main untuk membuat ProductForm yang mendefinisikan struktur form saat pengguna ingin menambah produk baru. Di views.py, 
saya mengimpor redirect, get_object_or_404, dan ProductForm. Setelah itu, saya membuat fungsi create_product yang akan menambahkan data produk baru. Fungsi ini akan 
mengecek validitas form menggunakan is_valid(), dan jika valid akan menyimpan data ke database.

Saya juga membuat fungsi show_product untuk menampilkan halaman detail dari satu produk. Di fungsi show_main, saya menambahkan variabel products_list yang berisi semua 
produk dari database dan menampilkannya di halaman main.html.

Agar fungsi-fungsi tersebut bisa diakses, saya mengimpornya ke dalam urls.py lalu menambahkan path() untuk create_product dan show_product ke dalam urlpatterns. 
Kemudian saya menyesuaikan tampilan main.html agar menampilkan semua produk dalam bentuk card, dan menambahkan tombol "Add Product" yang mengarah ke create_product 
serta tombol "View Detail" yang mengarah ke halaman detail produk berdasarkan id.

Untuk form penambahan produk, saya membuat file create_product.html yang menampilkan form input dan meng-extend base.html. Untuk halaman detail, saya membuat 
product_detail.html yang menampilkan informasi lengkap satu produk dan juga meng-extend base.html.

Terakhir, saya menambahkan URL proyek PWS ke dalam CSRF_TRUSTED_ORIGINS di settings.py agar permintaan POST dari form dianggap aman oleh Django. Dengan seluruh 
langkah ini, platform dapat menampilkan data produk, menambahkan produk baru, menampilkan detail produk, serta menyediakan endpoint data dalam format XML dan JSON.

**Feedback untuk Asisten Dosen pada Tutorial 2**
Menurut saya, asisten dosen pada tutorial 2 sudah sangat baik dan membantu, khususnya Kak Danniel dan Kak Scafi. Semua penjelasan jelas, interaktif, dan 
kehadiran asisten dosen juga memudahkan sayauntuk bertanya kapan saja. Overall, saya merasa terbantu dan belum ada kendala yang signifikan sejauh ini.

Berikut adalah bukti screenshot Postman saya: 
https://drive.google.com/drive/folders/1oIL8Mcmd5dTl4N5tn-foEcWEJk9jilds?usp=sharing