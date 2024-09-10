# brew-ba-boo

Link PWS : 
## Step-by-step Implementasi Checklist
Pertama-tama tentunya saya membuat GitHub repository, lalu melakukan cloning supaya bisa saya akses secara lokal. Setelah itu, saya langsung memulai untuk membuat project dan app Django, seperti yang sudah dilakukan saat tutorial. 
Dari tema E-commerce, saya membuat toko ramuan bernama "Magic Mixie Potion Shop". Di toko tersebut, setiap ramuan memiliki 4 atribut, yaitu nama, deskripsi, peringatan, dan harga. Jadi, dalam models.py saya mendefinisikan model Potion dengan name dengan tipe data CharField, description dan caution dengan TextField, dan price dengan IntegerField.
Ketika sedang menulis Html, saya memodifikasi sedikit menggunakan CSS, alhasil saya perlu membuat static files dan membuat direktorinya sedikit berbeda. Hal ini tidak berdampak saat routing, hanya saja saya perlu memodifikasi views.py dari yang diajarkan di soal karena tadi, direktorinya sedikit berubah. 
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
URL Dispatcher(urls.py) menerima request dari client dan memetakan ke view yang sesuai.
View(views.py) menerima request dari URL dispatcher dan menjalankan logika aplikasi dan mengakses data dari model jika diperlukan. 
Model(models.py) menyimpan dan mengelola data aplikasi, dia bisa diakses oleh view buat melakukan operasi CRUD(Create, Read, Update, Delete). 
Kembali lagi ke view tadi, setelah mengakses data dari model, dia bakal mengembalikan response ke client dalam banyak bentuk template, salah satunya HTML.
Di HTML baru kelihatan data yang dikirimkan view tadi. Selain menampilkan data, di HTML juga bisa menggunakan template engine kayak Django Template Language(DTL) buat mengembangkannya.
 

## Fungsi git dalam Pengembangan Perangkat Lunak
Dengan git, developer jadi bisa lebih mudah melihat perubahan kode dan juga mengembalikan ke versi sebelum dirubah. Contohnya fungsi version control ada untuk melacak perubahan kode dan mengembalikannya ke versi sebelumnya jika terjadi suatu kesalahan. Fungsi backup ada jika terjadi kehilangan kode, developer bisa mengembalikannya ke versi sebelumnya. Fungsi branching ada untuk mengembangkan fitur baru atau memperbaiki bug sedemikian sehingga tidak mengganggu kode utama. Fungsi merging ada untuk menggabungkan perubahan kode dari branch yang tadi ke kode utamanya.

## Alasan Django Menjadi Permulaan Pembelajaran Pengembangan Perangkat Lunak
Menurut saya alasan besarnya ada dua, mudah dipahami dan open-source. Django merupakan framework python, yang bisa saya bilang salah satu bahasa pemrograman yang paling mudah dibaca dan dipahami. Selain itu Django merupakan web framework yang gartis dan open source, artinya banyak tutorial memperlajarinya di internet.

## Alasan Model pada Django disebut sebagai ORM
Menurut saya, jika dilihat dari namanya ORM (Object-Relational Mapping), hal ini dikarenakan ORM kerjanya adalah dengan mendefinisikan model data sebagai kelas Python yang inherit dari models.Model. Setiap atribut kelas tadi mewakili kolom pada tabel database. Lalu, Django menggunakan ORM tadi untuk mengkonversi objek model tersebut menjadi query database yang sesuai. Object, merujuk ke representasi data yang akan disimpan ke database. Relational, merujuk ke database yang relasional, database yang menggunakan tabel-tabel untuk menyimpan data dan hubungan antara tabel-tabel tadi. Mapping, merujuk ke proses pemetaan antara objek dalam kode program dengan tabel database relasional.