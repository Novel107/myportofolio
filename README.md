Nama : Muhammad Fachri Novelino

NPM : 2506618881

Kelas : PBP D

---

### Tugas 1

1. Ya, saya menggunakan elemen semantik HTML5, yaitu `<section>`, untuk menambahkan bagian skills pemrograman. Elemen ini sangat membantu saya dalam menyusun struktur halaman secara semantik. Untuk elemen lain seperti <article> dan <aside>, belum saya gunakan karena merasa belum dibutuhkan pada desain portofolio saat ini.

2. Tantangan utama saya dalam mengatur CSS agar responsif adalah memastikan elemen-elemen tersebut tidak menyempit saat ukuran layar berubah, sehingga tampilannya tetap rapi dan enak dilihat secara visual.

3. Untuk proyek selanjutnya, saya ingin lebih banyak mengeksplorasi referensi website lain untuk membantu proses pengembangan. Saat ini, sebenarnya ada banyak ide elemen dan kombinasi warna yang ingin saya tuangkan, namun karena masih kurangnya pengetahuan, saya agak takut untuk memodifikasinya sembarangan. Ke depannya, saya juga ingin belajar cara menyisipkan dan mengatur gambar agar tampilannya lebih proporsional dan menarik.

---

Deklarasi AI:
Untuk tugas ini, saya menggunakan bantuan AI seperti Gemini untuk membantu menambahkan beberapa elemen HTML/CSS serta memberikan saran terkait struktur dan tata letak website. 

------
### Tugas 2

1. Beberapa peran berkaitann dengan Proses MVT:
Peran urls.py proyek: Ketika pengguna memasukkan URL di browser, request pertama kali masuk ke urls.py
tingkat proyek. Berkas ini bertugas sebagai pintu gerbang utama yang mengarahkan routing ke urls.py,
urls.py aplikasi: Berkas ini menerima rute spesifik (seperti /education/) dan memanggil fungsi view yang bertugas menangani URL tersebut, view: View bertindak sebagai otak atau pengontrol (controller). Ia menerima request, lalu meminta data yang dibutuhkan dari Model.
Model: representasi struktur database dalam kode Python. Ia bertugas mengeksekusi pengambilan data portofolio dari database
Template: Setelah View mendapatkan data, data tersebut dibungkus dalam bentuk kamus (context dictionary) dan dikirim ke Template.

2. Alasan menyimpan dengan model agar sewaktu-waktu ketika mengubah suatu data atau mengupdate suatu data,
bisa lebih mudah sehingga kita tidak perlu pusing  memikirkan bagaimana suatu kode di ubah sehingga ketika dilakukanan
suatu pemeliharaan kita tidak perlu pusing mengenai kode dan bisa lebih fokus ke kode yang lain

3. Template: Setelah View mendapatkan data, data tersebut dibungkus dalam bentuk kamus (context dictionary) dan dikirim ke Template.
migrate: Perintah ini bertugas untuk mengeksekusi cetak biru migrasi tadi dan menerapkannya secara fisik ke dalam skema database
Contohnya: Ketika saya menambahkan model baru bernama Education di models.py, saya harus menjalankan makemigrations agar Django mencatat instruksi pembuatan model tersebut. Setelah itu, saya wajib menjalankan migrate agar tabel Education benar-benar terbuat secara fisik di dalam database

---

Deklarasi Penggunaan AI:
Untuk tugas ini, saya menggunakan bantuan AI seperti Gemini sebagai sarana diskusi untuk lebih memahami struktur kerangka kerja Django serta penulisan unit test. Sementara untuk implementasi front-end, saya sebagian besar menggunakan ulang dan memodifikasi struktur HTML serta elemen CSS yang sudah saya kerjakan sebelumnya di bagian Experience untuk diadaptasi ke bagian Education.

## Tugas 3

1. Kita menggunakan ModelForm karena fitur ini secara otomatis membuat struktur form HTML berdasarkan atribut yang sudah didefinisikan di dalam model database, sehingga kode menjadi jauh lebih ringkas odelForm juga mengotomatisasi validasi data input dan proses penyimpanan langsung ke database (melalui form.save()). Jika kita membuat form HTML manual, kita harus menulis setiap tag <input> satu per satu dan memvalidasi tipe datanya secara manual di views.py.
Sementara itu, {% csrf_token %} (Cross-Site Request Forgery) diwajibkan oleh Django pada setiap form bermetode POST sebagai lapisan keamanan. Token unik ini memastikan bahwa data yang disubmit benar-benar berasal dari website kita, mencegah serangan dari situs web berbahaya yang mencoba mengirimkan data palsu seolah-olah berasal dari pengguna yang sah.

2.JSON menjadi dominasi karena formatnya jauh lebih ringan dan ringkas dibandingkan XML yang sangat bergantung pada banyak tag pembuka dan penutup. Ukuran file yang lebih kecil membuat proses transfer dan parsing data JSON menjadi jauh lebih cepat di jaringan.

3. Client mengirim permintaan ke URL tertentu -> Django mengarahkan URL tersebut ke fungsi view terkait -> view mengambil data dari database (menghasilkan objek Python bernama QuerySet) -> QuerySet diserialisasi menjadi string JSON -> string JSON tersebut dikembalikan ke client melalui HttpResponse dengan content-type application/json.
Proses serialization mutlak diperlukan karena data yang ditarik dari database oleh Django masih berupa objek Python (Model instances) yang kompleks dan terikat dengan ekosistem backend. Protokol HTTP tidak bisa mengirim objek Python secara mentah. Oleh karena itu, serialization bertugas menerjemahkan (mengubah bentuk) objek kompleks tersebut menjadi format teks datar (seperti JSON) agar bisa ditransmisikan lewat jaringan dan dimengerti oleh aplikasi frontend.

---
Deklarasi Penggunaan AI:

Untuk tugas ini, saya menggunakan bantuan AI (Gemini) sebagai teman diskusi untuk lebih memahami materi. Berhubung tugas ini masih mirip dengan Tutorial 3 dan ada beberapa fungsi yang serupa, diskusi dengan AI sangat membantu mempermudah workflow penyelesaiannya. Sementara untuk front-end, saya menggunakan ulang dan memodifikasi kode HTML serta CSS dari bagian Education yang sudah saya buat sebelumnya untuk dipakai di bagian Experience.