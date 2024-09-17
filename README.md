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


