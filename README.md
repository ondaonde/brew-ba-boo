# brew-ba-boo

Link PWS : https://najwa-zarifa-brewbaboo.pbp.cs.ui.ac.id/
<details>
  <summary>Assignment 2</summary>

  ## Step-by-step Implementasi Checklist
Pertama-tama tentunya saya membuat GitHub repository, lalu melakukan cloning supaya bisa saya akses secara lokal. Setelah itu, saya langsung memulai untuk membuat project dan app Django, seperti yang sudah dilakukan saat tutorial. 
Dari tema E-commerce, saya membuat toko ramuan bernama "Brew-ba-boo Potion Shop". Di toko tersebut, setiap ramuan memiliki 4 atribut, yaitu nama, deskripsi, peringatan, dan harga. Jadi, dalam models.py saya mendefinisikan model Potion dengan name dengan tipe data CharField, description dan caution dengan TextField, dan price dengan IntegerField.
Ketika sedang menulis HTML, saya memodifikasi sedikit menggunakan CSS, alhasil saya perlu membuat static files dan membuat direktorinya sedikit berbeda. Hal ini tidak berdampak saat routing, hanya saja saya perlu memodifikasi views.py dari yang diajarkan di soal karena tadi, direktorinya sedikit berubah. 
Ada sedikit kendala dengan sistem PWS, jadi ketika menulis ini sebenarnya saya belum men-deploy ke PWS.

## Bagan Request Client ke Web App Berbasis Django
```
+--------+           +----------------+               +------+                  +----------+
| Client | --------> | URL Dispatcher | ------------> | View | ---------------> | Template |
+--------+  Request  +----------------+  Mapping URL  +------+  Mengirim data   +----------+
                                                         ^ |                         |
                                                    CRUD | | Mengakses data          | Menampilkan data
                                                         | v                         v
                                                      +-------+                  +--------+
                                                      | Model |                  | Client |
                                                      +-------+                  +--------+
```
Client(Browser) mengirimkan request ke server Django melalui URL.
URL Dispatcher(`urls.py`) menerima request dari client dan memetakan ke view yang sesuai.
View(`views.py`) menerima request dari URL dispatcher dan menjalankan logika aplikasi dan mengakses data dari model jika diperlukan. 
Model(`models.py`) menyimpan dan mengelola data aplikasi, dia bisa diakses oleh view buat melakukan operasi CRUD(Create, Read, Update, Delete). 
Kembali lagi ke view tadi, setelah mengakses data dari model, dia bakal mengembalikan response ke client dalam banyak bentuk template, salah satunya HTML.
Di HTML baru kelihatan data yang dikirimkan view tadi. Selain menampilkan data, di HTML juga bisa menggunakan template engine kayak Django Template Language(DTL) buat mengembangkannya.
 

## Fungsi git dalam Pengembangan Perangkat Lunak
Dengan git, developer jadi bisa lebih mudah melihat perubahan kode dan juga mengembalikan ke versi sebelum dirubah. Contohnya fungsi version control ada untuk melacak perubahan kode dan mengembalikannya ke versi sebelumnya jika terjadi suatu kesalahan. Fungsi backup ada jika terjadi kehilangan kode, developer bisa mengembalikannya ke versi sebelumnya. Fungsi branching ada untuk mengembangkan fitur baru atau memperbaiki bug sedemikian sehingga tidak mengganggu kode utama. Fungsi merging ada untuk menggabungkan perubahan kode dari branch yang tadi ke kode utamanya.

## Alasan Django Menjadi Permulaan Pembelajaran Pengembangan Perangkat Lunak
Menurut saya alasan besarnya ada dua, mudah dipahami dan open-source. Django merupakan framework python, yang bisa saya bilang salah satu bahasa pemrograman yang paling mudah dibaca dan dipahami. Selain itu Django merupakan web framework yang gartis dan open source, artinya banyak tutorial memperlajarinya di internet.

## Alasan Model pada Django disebut sebagai ORM
Menurut saya, jika dilihat dari namanya ORM (Object-Relational Mapping), hal ini dikarenakan ORM kerjanya adalah dengan mendefinisikan model data sebagai kelas Python yang inherit dari `models.Model`. Setiap atribut kelas tadi mewakili kolom pada tabel database. Lalu, Django menggunakan ORM tadi untuk mengkonversi objek model tersebut menjadi query database yang sesuai. Object, merujuk ke representasi data yang akan disimpan ke database. Relational, merujuk ke database yang relasional, database yang menggunakan tabel-tabel untuk menyimpan data dan hubungan antara tabel-tabel tadi. Mapping, merujuk ke proses pemetaan antara objek dalam kode program dengan tabel database relasional.
</details>
<details>
  <summary>Assignment 3</summary>

## Pentingnya Data Delivery dalam Implementasi Platform
Data Delivery berperan penting dalam implemetasi platform karena dialah yang memungkinkan untuk pengumpulan data, memprosesnya, lalu menganalisis dari berbagai sumber dalam real-time. Aplikasi langsungnya di assignment 3 PBP ini ada di data delivery-nya yang menggunakan template HTML ke format XML dan JSON. Di dalam template `create_potion.html` terdapat form yang berisi beberapa field untuk menginput data Potion dan akan dikirim ke server melalui request POST seusai mengisi form dan mengklik tombol "Finish Potion". Setelah itu `views.py` akan menerima request POST dan memproses data yang dikirim. Setelah data selesai diproses dan sebelum dikirim ke format XML atau JSON, view create_potion melakukan validasi data menggunakan `form.is_valid()`. Jika data valid maka view akan `show_xml` atau `show_json` akan dipanggil untuk mengirim data ke format XML atau JSON dan dikirim ke klien melalui response HTTP. Tanpa adanya data delivery, maka kita tidak bisa mengakses data potion yang telah mereka buat dalam format yang berbeda-beda, yang dalam tugas ini dalam format XML dan JSON.

## Perbandingan XML dan JSON
Sebenarnya, baik XML maupun JSON pasti memiliki kelebihan dan kekurangannya masing-masing, namun saya pribadi setuju dengan mayoritas bahwa JSON lebih baik. Alasan utama saya berkata demikian adalah karena struktur datanya yang lebih sederhana dan readability-nya. JSON lebih mudah dibaca karena dia tidak menggunakan JSON tidak menggunakan tag sehingga terlihat lebih ringkas dan dia lebih terlihat saja antara nama property dengan valuenya karena menggunakan satu tanda titik dua `:`.

## Peran method is_valid() dalam Form Django
Seperti yang saya sebutkan sebelumnya, setelah data selesai diproses dan sebelum dikirim ke format XML atau JSON, view create_potion melakukan validasi data menggunakan `form.is_valid()`. Intinya method ini berfungsi untuk memeriksa apakah data yang dikirimkan sesuai dengan aturan yang telah ditentukan pada form. Jika data yang dikirimkan valid, maka akan dilanjutkan prosesnya, namun jika tidak, akan menampilkan pesan error. Dengan adanya method is_valid(), kita dapat menghindari data yang tidak valid masuk ke dalam database atau sistem kita sehingga mengurangi risiko kesalahan yang dapat terjadi. Selain itu method is_valid() juga berperan dalam meningkatkan keamanan sistem dengan menghindari data yang tidak valid yang dapat digunakan untuk melakukan serangan keamanan.

## Peran csrf_token dalam Pembuatan Form Django
CSRF (Cross-Site Request Forgery) token adalah suatu fitur keamanan di Django yang  dapat membantu kita mencegah serangan pada situs web yang kita buat. Dengan menambahkan `{% csrf_token %}` dalam form, Django akan generate token unik untuk setiap submission-nya dan akan di-verify oleh server untuk memastikan bahwa request tersebut legitimate. Di sisi lain, jika kita tidak menambahkannya, penyerang dapat mengelabui pengguna agar mengirimkan formulir palsu, yang akan mengirimkan permintaan ke situs web kita. Karena permintaan tersebut berasal dari situs web lain, Django tidak akan dapat memverifikasi keaslian permintaan tersebut. Lalu, jika permintaan itu berhasil, penyerang dapat melakukan tindakan di situs web kita, seperti misalnya membuat pengguna baru, menghapus data, atau membuat perubahan yang tidak sah. 

## Step-by-step Implementasi Checklist
Pertama-tama saya membuat directory baru, yaitu `templates` di ROOT dan membuat `base.html`. Karena main.html memiliki footer, maka saya perlu menambahkan footer di sana dan template tags block footer. Setelah itu saya menambahkan directory untuk templates dengan menambahkan line `'DIRS': [BASE_DIR / 'templates']` di `settings.py` milik proyek brew-ba-boo. Karena sebelumnya di `main.html` saya sudah membuat object di sana, maka saya perlu menghapusnya dan memodifikasi supaya ketika form diisi, dia akan mengembalikan isi formnya dengan bentuk sesuai seperti sebelumnya. Contohnya saya menggunakan container untuk menyimpan semua objek bernama "card-container" dan "card" sebagai container dari satu objek itu sendiri. Setelahnya kurang lebih saya mengikuti instruksi dari tutorial 2 dan memodifikasinya sesuai dengan projek saya.

## Screenshots Hasil Akses URL pada Postman
- Screenshot XML
![Screenshot XML](https://github.com/user-attachments/assets/8e4e5d84-08b0-4b71-afe0-516eb997682d)
- Screenshot JSON
![Screenshot JSON](https://github.com/user-attachments/assets/0e868829-6190-490f-a28c-5bc84e288eeb)
- Screenshot XML by ID
![Screenshot XML by ID](https://github.com/user-attachments/assets/c438c834-d0fb-4762-9f6c-ca98dab9c487)
- Screenshot JSON by ID
![Screenshot JSON by ID](https://github.com/user-attachments/assets/65100dcd-1fcb-4a7d-9e3a-70e53360e1ae)
</details>
<details>
  <summary>Assignment 4</summary>

## Perbedaan HttpResponseRedirect() dengan redirect()
`HttpResponseRedirect()` dan `redirect()` sama-sama digunakan untuk redirect user ke url di django, namun perbedannya adalah `HttpResponseRedirect()` adalah suatu class yang return HTTP response dengan redirect status code(302), sedangkan `redirect()` adalah fungsi yang mengembalikan objek `HttpResponseRedirect`. Dengan begitu bisa kita simpulkan bahwa `redirect()` adalah wrapper-nya `HttpResponseRedirect`.
## Cara kerja penghubungan model Product dengan User
Di app seperti e-commerce, setiap produk yang ada di dalamnya pasti diasosiasikan dengan seorang user yang membuat produk tersebut. Dalam app ini, dengan menghubungkan `Potion` dan `User` model, kita bisa mengasosiasikan potion itu dengan creator-nya, mengambil list of potions yang dibuat oleh masing-masing user, dan menampilkan nama user dengan potion yang dibuatnya. 
- Di Django, kita bisa menghubungkan produk tersebut dengan user yang sesuai menggunakan foreign key. Foreign key adalah suatu field di model yang akan reference ke primary key model lain. Contoh langsung untuk menghubungkan suatu produk ke user terkait di kode yang sudah ditulis, adalah di `Potion` memiliki field foreign key yang disebut user yang mana akan me-referensi langsung ke `User` model. Selain itu ada argumen `on_delete=models.CASCADE`, yang akan membuat user dihapus, maka semua produk yang terkait dengan user tersebut juga akan dihapus.  
- Di atas fungsi `show_main()` pada `views.py` ada decorator `@login_required` yang fungsinya adalah memastikan bahwa hanya pengguna yang diautentikasi yang dapat mengakses tampilan tersebut
- Di fungsi `show_main()` pada `views.py` juga ada argumen `potions = Potion.objects.filter(user=request.user)`. Argumen tersebut akan mengembalikan queryset dari `Potion` yang berhubungan dengan user yang sesuai.

## Perbedaan Authentication and Authoritation pada Django
- Autentichation adalah tentang verification dari  identitas pengguna. Di app ini, contoh authentication ada di `AuthenticationForm` di fungsi `login_user()` . `AuthenticationForm` digunakan untuk memvalidasi kredensial pengguna (nama pengguna dan kata sandi). Jika formulir valid, maka fungsi login akan dipanggil untuk memasukkan pengguna.
- Authorization adalah tentang bagaimana akses ke resources dikontrol berdasarkan identitas dan izin yang dimiliki pengguna. Di app ini, contoh authorization ada di `@login_required` decorator di atas fungsi `show_main()`. Decorator ini ada untuk memeriksa apakah pengguna telah diautentikasi sebelum mengizinkan akses ke tampilan show_main. Jika pengguna tidak diautentikasi, mereka akan diarahkan ke halaman login.

## Pengelolaan Cookies pada Django
Ketika user logs ke aplikasi Django, Django akan membuat random session ID dan menyimpannya ke user session database dab sistem authetication akan set session cookie di browser-nya user. Isi cookie ini isinya unique session ID yang mengidentifikasi sesi user. Pada request berikutnya, browser akan mengirimkan cookie kembali ke server lalu Django akan memeriksa session ID di cookie dengan sesi database yang akan memeriksa identitas user. Selain authetication, cookies juga digunakan untuk menyimpan preferensi pengguna dan track behaviour user.

Tidak semua cookie aman digunakan. Cookie bisa saja dicuri, dimanipulasi, dirubah maupun dihapus oleh malicious person. Jadi, untuk mengurangi risiko tersebut, kita bisa menggunakan secure protocols(HTTPS) untuk mengenkripsi data cookie. 

## Step-by-step Implementasi Checklist
Dalam pengerjaan assignment kali ini, saya pertama-tama runserver terlebih dahulu untuk memastikan bahwa assignment saya sebelum-sebelumnya tidak ada masalah dan saya bisa fokus mengerjakan assignment yang sekarang, assignment 4. Setelah itu saya membuat fungsi dan form registrasi dengan mengimport `UserCreationForm`, menambahkan fungsi `register.py`, membuat templates `register.html` lalu menambahkan path url nya di `urls.py`. Selanjutnya saya membuat mekanisme login dan logout yang kurang lebih sama dengan register, hanya saja untuk login, ada satu step tambahan yaitu menambahkan authenticate. Setelah selesai dengan mekanisme register, login, logout, yang selanjutnya saya lakukan adalah merestriksi akses halaman main menggunakan decorator `@login_required`. Setelah runserver dan memastikan register, login, logout sudah berjalan semestinya saya kemudian mengimplementasi cookies untuk `last_login`. Lalu yang terakhir saya menghubungkan model dengan user supaya product yang tampil akan sesuai dengan user yang membuatnya.
</details>
<details>
  <summary>Assignment 5</summary>

## CSS Selector dan Prioritasnya
CSS Selector adalah suatu pattern untuk memilih elemen HTML untuk diaplikasian styles. Selector ada beberapa tipe, yaitu:
1. Element selectors
Digunakan untuk memilih element berdasarkan tag-nya (ex:// `h1`, `p`, `div`) dan bisa juga inline (ex://`<p style="color: red;">`)
2. Class selectors
Digunakan untuk memilih element berdasarkan class atribute yang dimiliki element (ex:// `.header`, `.radio-button`)
3. ID selectors
Digunakan untuk memilih element berdasarkan ID attribute yang dimiliki element (ex://`#header`, `#radio-button`)
4. Combinators
Menggabungkan multiple selectors untuk memilih element berdasarkan hubungannya (ex://`>` untuk target direct children)

Ketika banyak tipe selector yang digunakan di saat yang bersamaan, maka urutan prioritasnya adalah seperti ini: Inline > ID > Class > Attribute
## Peran Responsive Design dalam Pengembangan Aplikasi Web
Responsive Design umumnya ada untuk website yang kita gunakan setiap hari bisa beradaptasi dengan ukuran layar, perangkat, dan orientasi yang berbeda. Dengan responsive web design, kita sebagai pengguna dapat mengakses website di beragai perangkat dengan berbagai ukuran layar dengan tingkat fungsionalitas yang sama. Untuk contoh aplikasi yang sudah mengaplikasikan responsive web design, kita ambil contohnya, yaitu Youtube. Ketika kita membuka website Youtube di Laptop, di Mobile, dan di Tab akan menunjukkan tampilan video dengan ukuran berbeda-beda. Sedangkan untuk yang belum mengaplikasikannya adalah Siak-NG.
## Perbedaan margin, border, dan padding
Mudahnya margin adalah ruang di luar elemen, border adalah batas yang terlihat di sekitar elemen, dan padding adalah ruang di dalam elemen. Ketiganya adalah properti CSS, jadi untuk aplikasinya bisa kita lakukan menggunakan keempat CSS Selector yang sudah disebutkan di atas.
## Konsep flex box dan grid layout
Flex box adalah CSS Layout Mode untuk membuat layout yang flexible dan responsive. Flex box biasanya mencakup atau menggunakan container yang menjadi parent element-element di bawahnya. Flex box juga menggunakan sumbu utama(horizontal atau vertical) dan sumbu silang, sumbu yang tegak lurus dengan sumbu utama. Sedangkan, grid layout adalah layout 2 dimensi untuk membuat layout yang lebih kompleks. Sama seperti flex box, grid layout juga menggunakan container untuk menampung children, tapi yang membedakan flex box dengan grid layout adalah grid layout memiliki grid tracks dan grid cells yang membuat grid itu sendiri.
## Step-by-step Implementasi Checklist
Karena sebelum-sebelumnya saya sudah mengimplementasikan responsive design di aplikasi Brew-ba-boo ini, jadi kali ini saya kurang lebih hanya menambahkan fitur-fitur baru saja seperti Navigation Bar, Create Potion dan Delete Potion. Pertama-tama saya menambahkan Tombol Create Potion dan Delete Potion di container yang menampung card itu sendiri karena card saya memiliki dua bagian, depan dan belakang, dan jika di-hover akan otomatis berbalik. Jika tombol itu akan terus-terus ter-hover nanti akan menyulitkan user. Jadi, karena itu button edit dan delete ada di atas kanan card. Setelah itu saya menambahkan navigation bar yang hanya berisi logo Brew-ba-boo dan `Welcome, user {{user.username}}` dan button untuk logout di kanannya. Navigation Bar hanya sedikit fungsinya karena memang fungsi dari aplikasi itu sendiri belum begitu banyak, mungkin selanjutnya akan ditambahkan seiring bertambahnya fitur.
</details>
<details>
  <summary>Assignment 6</summary>

## Manfaat JS dalam Pengembangan Web
JavaScript atau JS merupakan salah satu bahasa paling populer dalam pengembangan web. Hal ini tentuntya didasari oleh keunggulan dari JS itu sendiri seperti dapat membuat web pages yang dapat berinteraksi dengan user, memungkinkan untuk berjalan di hampir semua browser tanpa melakukan instalasi tambahan, dan banyak hal lainnya. Dalam assignment kali ini saya menerapkan AJAX sehingga memungkinkan website untuk melakukan pembaruan konten secara sebagian (tanpa reload halaman penuh), misalnya saat memuat data tambahan di halaman tanpa menyegarkan seluruh halaman. Ini bisa dilakukan karena dengan AJAX, data bisa dikirim ke server dan diambil dari server secara asinkron.

## Fungsi `await` ketika menggunakan `fetch()`
Fungsi `fetch()` ada untuk mengembalikan promise, yang berarti operasi tersebut berjalan secara asinkron. Saat menggunakan `fetch()` untuk membuat permintaan HTTP, `await` ada untuk menghentikan sementara eksekusi kode hingga promise yang dikembalikan oleh `fetch() ` diselesaikan atau ditolak. Dengan begitu memudahkan kita sebagai developer untuk mengelola kode asynchronous. Namun, jika kita tidak menggunakan await, kode akan terus dieksekusi tanpa menunggu janji diselesaikan, yang dapat menyebabkan perilaku dan kesalahan yang tidak diharapkan.

## Urgensi `csrf_exempt` pada AJAX POST
`csrf_exempt` digunakan untuk menonaktifkan perlindungan Cross-Site Request Forgery (CSRF) pada endpoint tertentu. Dalam kasus AJAX POST, jika view tidak menggunakan token CSRF yang valid, request dari frontend akan ditolak oleh server. Maksud dari ditolak oleh server adalah request tersebut bisa gagal karena server secara default memblokir request POST tanpa token CSRF yang benar. Dengan menggunakan csrf_exempt, kita mengizinkan request POST untuk dikirim tanpa perlindungan CSRF.

## Pembersihan Data Input Pengguna di Backend
Sebenarnya pembersihan data atau validasi bisa kita lakukan di frontend, terutama jika kita berbicara soal efisien karena umpan balik yang diberikan akan lebih cepat. Namun, validasi di frontend tidak bisa menjadi penjamin keamanan situs web, ada beberapa hal yang perlu diperhatikan, antara lain:
- Data dari frontend dapat dimanipulasi oleh malicious user menggunakan alat seperti developer tools atau intercepting proxies. Oleh karena itu, backend perlu memastikan bahwa semua data yang diterima aman dan valid.
- Tidak semua pengguna mengakses aplikasi dengan JavaScript aktif atau melalui antarmuka yang sama. Validasi di backend memastikan bahwa semua data yang masuk melalui berbagai cara tetap diperiksa dengan benar.
- Beberapa validasi lebih kompleks atau memerlukan akses ke sumber daya backend, misalnya pengecekan ketersediaan nickname user.

## Step-by-step Implementasi Checklist
Hal yang pertama kali saya lakukan adalah mengubah kode card saya supaya bisa mendukung AJAX. Jadi, saya membuka `views.py` lalu menambahkan fungsi baru bernama `create_potion_by_ajax` lalu membuat routing-nya di `urls.py`. Setelah itu saya menghapus beberapa baris di `main.html` yang dinilai tidak perlu karena kita sudah bisa mendapatkan objek dari endpoint `/json`. Setelah itu saya menambahkan inline JavaScript dan menambahkan beberapa fungsi seperti `getPotions()`, `refreshPotions()`, dan `addPotions()`. Setelah melakukan testing bahwa objek bisa dibuat dengan AJAX dengan benar, selanjutnya saya menambahkan `strip_tags` untuk membersihkan input data user di bagian `name`, `description`, dan `caution`.  
</details>
