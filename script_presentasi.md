# Slide 1 (PEMBUKAAN)
"Bismillahirrahmanirrahim. Assalamualaikum Warahmatullahi Wabarakatuh.
Yang saya hormati Bapak dan Ibu Dosen Penguji:

Bapak Bedi Purnama, S.Si., M.T., Ph.D., selaku dosen pembimbing
Bapak Isman Kurniawan, S.Pd., M.Si., M.Sc., Ph.D., dan
Ibu Izzatul Ummah, S.T., M.T., selaku dosen penguji

Terima kasih atas kesediaan Bapak dan Ibu untuk hadir dan menguji sidang tugas akhir saya pada siang hari ini.
Perkenalkan, saya Khalifardy Miqdarsah, mahasiswa angkatan 2021. Pada kesempatan ini, saya akan mempresentasikan hasil penelitian tugas akhir saya yang berjudul 'Optimasi Hyperparameter Convolutional Neural Network (CNN) dengan Komodo Mlipir Algorithm (KMA) untuk Prediksi Parameter Stellar Bintang Tunggal'.
Penelitian ini mengusulkan pendekatan dalam mengoptimalkan hyperparameter deep learning untuk analisis astronomi, dengan menggabungkan keunggulan Convolutional Neural Network dan Komodo Mlipir Algorithm (KMA), yang diharapkan dapat meningkatkan akurasi prediksi parameter bintang tunggal secara signifikan."

#Slide 2 (Latar belakang)
"Perkembangan teknologi observasi astronomi telah menghasilkan volume data spektrum bintang yang terus meningkat secara signifikan. Data spektrum ini memiliki peran krusial dalam penentuan parameter stellar bintang, namun analisis spektrum secara konvensional menjadi semakin kompleks dan tidak efisien seiring dengan pertumbuhan data.

Terobosan dalam mengatasi tantangan ini telah dimulai melalui penelitian yang dilakukan oleh S. Fabbro et al., yang mengembangkan arsitektur Convolutional Neural Network (CNN) untuk memprediksi parameter stellar berdasarkan spektrum bintang. Meskipun pendekatan deep learning ini menjanjikan, performa model CNN sangat bergantung pada optimasi hyperparameter yang tepat.

Penentuan hyperparameter yang optimal merupakan tantangan tersendiri dalam pengembangan model deep learning. Diperlukan metode pencarian yang tidak hanya optimal tetapi juga efisien dalam menemukan kombinasi hyperparameter terbaik. Dalam konteks ini, Komodo Mlipir Algorithm (KMA) yang dikembangkan oleh Prof. Suyanto dari Telkom University menawarkan solusi yang menjanjikan.

Efektivitas KMA dalam optimasi hyperparameter CNN telah dibuktikan melalui penelitian tugas akhir K. A. Faath, yang menunjukkan peningkatan akurasi signifikan pada kasus prediksi tulisan tangan menggunakan dataset MNIST. Berdasarkan keberhasilan tersebut, penelitian ini mengimplementasikan KMA untuk mengoptimalkan hyperparameter model CNN dalam konteks prediksi parameter stellar bintang."

#slide 3 (Rumusan Masalah dan Tujuan Penelitian)
"Berdasarkan latar belakang yang telah dipaparkan, penelitian ini berfokus pada dua rumusan masalah utama. Rumusan masalah pertama berkaitan dengan aspek teknis implementasi, yaitu bagaimana mengimplementasikan Komodo Mlipir Algorithm untuk mengoptimalkan hyperparameter CNN dalam konteks prediksi parameter stellar. Hal ini mencakup proses integrasi algoritma KMA dengan arsitektur CNN yang ada, serta penentuan parameter optimasi yang sesuai.

Rumusan masalah kedua menekankan pada evaluasi kinerja, yakni bagaimana pengaruh hyperparameter yang telah dioptimalkan menggunakan KMA terhadap performa CNN dalam memprediksi parameter stellar bintang. Aspek ini penting untuk memvalidasi efektivitas pendekatan yang diusulkan dalam meningkatkan akurasi prediksi.

Sejalan dengan rumusan masalah tersebut, penelitian ini memiliki dua tujuan utama. Tujuan pertama adalah mengimplementasikan KMA untuk menemukan kombinasi hyperparameter CNN yang optimal. Implementasi ini mencakup pengembangan sistem yang mengintegrasikan KMA dengan CNN secara efektif dan efisien.

Tujuan kedua adalah meningkatkan akurasi model CNN dalam memprediksi parameter stellar bintang melalui optimasi hyperparameter. Peningkatan akurasi ini diharapkan dapat memberikan kontribusi signifikan dalam meningkatkan efisiensi analisis data astronomi, khususnya dalam konteks prediksi parameter stellar bintang tunggal."

#Slide 4 (Landasan teori spektrum)
"Spektrum bintang merupakan suatu representasi visual dari distribusi energi cahaya yang dipancarkan bintang pada berbagai panjang gelombang. Sama seperti cahaya matahari yang dapat diuraikan menjadi pelangi oleh prisma, spektrum bintang menunjukkan 'sidik jari' unik dari setiap bintang yang memungkinkan kita memahami karakteristik dan komposisinya.
Dalam studi astronomi, kita mengenal tiga jenis spektrum utama yang memiliki karakteristik berbeda. Pertama, spektrum kontinyu, yang merupakan spektrum paling dasar yang dihasilkan secara alami oleh sumber cahaya. Bayangkan seperti pelangi yang mulus tanpa garis-garis, di mana warna bergradasi dengan halus dari satu ke yang lain.
Kedua, spektrum absorpsi, yang terbentuk ketika cahaya dari sumber yang menghasilkan spektrum kontinyu melewati material yang lebih dingin. Material ini menyerap cahaya pada panjang gelombang tertentu, menciptakan garis-garis hitam pada spektrum. Pola garis hitam ini bersifat unik dan bertindak seperti 'barcode' yang mengidentifikasi unsur-unsur yang dilewati cahaya. Sebagai contoh, ketika cahaya dari fotosfer matahari melewati atmosfer yang lebih dingin, akan terbentuk garis-garis absorpsi yang karakteristik.
Ketiga, spektrum emisi, yang menampilkan garis-garis terang berwarna pada panjang gelombang tertentu. Spektrum ini terbentuk ketika atom-atom dalam keadaan tereksitasi memancarkan cahaya pada panjang gelombang spesifik. Seperti halnya spektrum absorpsi, pola garis emisi ini juga unik untuk setiap unsur, memberikan informasi tentang komposisi kimia sumber cahaya.

#slide 5 (Landasan teori spektrum, parameter stellar )
"Pemahaman tentang ketiga jenis spektrum yang telah dipaparkan sebelumnya memiliki peran fundamental dalam penelitian ini, karena spektrum bintang mengandung informasi vital tentang parameter stellar. Parameter stellar ini merupakan karakteristik fisik bintang yang dapat kita pelajari melalui analisis spektrumnya. Mari kita bahas tiga parameter utama yang menjadi fokus penelitian ini.
Parameter pertama adalah temperatur efektif, yang menggambarkan suhu permukaan bintang. Temperatur efektif ini mempengaruhi bentuk spektrum kontinyu bintang - semakin tinggi temperatur, semakin bergeser puncak spektrum ke arah panjang gelombang yang lebih pendek. Ini dikenal sebagai hukum pergeseran Wien. Sebagai contoh, bintang dengan temperatur efektif sekitar 6000K seperti Matahari akan memiliki puncak spektrum di daerah cahaya tampak, sementara bintang yang lebih panas akan cenderung ke arah biru atau ultraviolet.
Parameter kedua adalah metalisitas, yang menunjukkan kelimpahan unsur-unsur yang lebih berat dari helium dalam atmosfer bintang. Metalisitas ini tercermin dalam kekuatan garis-garis absorpsi pada spektrum bintang. Bintang dengan metalisitas tinggi akan menunjukkan garis-garis absorpsi yang lebih kuat untuk unsur-unsur logam. Ini memberikan informasi berharga tentang generasi dan evolusi bintang dalam galaksi kita.
Parameter ketiga adalah gravitasi permukaan, yang berkaitan erat dengan massa dan radius bintang. Gravitasi permukaan mempengaruhi tekanan dan kepadatan atmosfer bintang, yang pada gilirannya mempengaruhi lebar garis-garis absorpsi dalam spektrum. Bintang raksasa dengan gravitasi permukaan rendah cenderung memiliki garis spektrum yang lebih tajam dibandingkan bintang katai dengan gravitasi permukaan tinggi.
Ketiga parameter ini saling terkait dan memberikan gambaran komprehensif tentang sifat fisik bintang. Tantangan dalam memprediksi parameter-parameter ini terletak pada kompleksitas hubungan antara spektrum dan parameter stellar, yang seringkali bersifat non-linear. Inilah mengapa penggunaan deep learning, khususnya CNN yang dioptimalkan dengan KMA, menjadi pendekatan yang menjanjikan dalam penelitian ini."

#slide 6 ( Starnet)
"StarNet merupakan arsitektur Convolutional Neural Network yang inovatif, dikembangkan secara khusus oleh S. Fabbro untuk memprediksi tiga parameter stellar utama: temperatur efektif, gravitasi permukaan (log g), dan metalisitas. Keunikan arsitektur ini terletak pada desainnya yang dioptimalkan untuk mengolah data spektrum bintang.

Arsitektur StarNet terdiri dari tujuh layer yang saling terhubung, dimana setiap layer memiliki peran spesifik dalam proses ekstraksi dan pembelajaran fitur. Mari kita telusuri setiap komponen arsitektur ini:

Layer pertama adalah input layer, yang menerima data spektrum bintang dalam bentuk satu dimensi. Layer ini berfungsi sebagai pintu gerbang yang mempersiapkan data spektrum untuk diproses lebih lanjut.

Selanjutnya, terdapat dua layer konvolusi yang berperan dalam ekstraksi fitur. Layer-layer ini menggunakan filter yang bergeser sepanjang spektrum untuk mendeteksi pola-pola penting seperti garis absorpsi dan variasi intensitas yang berkaitan dengan parameter stellar.

Setelah layer konvolusi, terdapat pooling layer yang bertugas mengurangi dimensi data sambil mempertahankan informasi penting. Layer ini membantu mengurangi kompleksitas komputasi dan mencegah overfitting.

Dua fully connected layer berikutnya bertindak sebagai 'otak' dari jaringan, mengintegrasikan informasi yang telah diekstrak untuk memahami hubungan kompleks antara pola spektrum dan parameter stellar.

Akhirnya, output layer menghasilkan prediksi untuk ketiga parameter stellar yang ditargetkan.
[REFERENSI GAMBAR]
Seperti yang dapat kita lihat pada gambar, arsitektur ini menunjukkan aliran data dari input spektrum hingga menghasilkan prediksi parameter stellar. Desain berlapis ini memungkinkan StarNet untuk mempelajari representasi hierarkis dari data spektrum, mulai dari fitur-fitur sederhana hingga pola-pola kompleks yang menentukan parameter stellar."

#slide 7 (starnet hyperparameter)
hyperparameter yang akan di optimalkan berdasarkan pada arsitektur starnet adalah sebagai berikut :
- kernel size
-activation funtion
- kerne intializer
-learning rate
-epoch
-batch size
- pool size

#slide 8 (Komodo mlipir Algorithm)

"Komodo Mlipir Algorithm (KMA) adalah algoritma optimasi yang terinspirasi dari perilaku komodo dalam mencari makanan. Yang membuat algoritma ini unik adalah pendekatan tiga kelompok populasi yang masing-masing memiliki karakteristik pergerakan berbeda dalam mencari solusi optimal.
Mari kita telusuri ketiga kelompok tersebut secara mendalam:
Kelompok pertama adalah komodo jantan besar, yang merepresentasikan solusi terkuat. Kelompok ini menerapkan strategi High Exploitation, Low Exploration (HILE). Dalam implementasinya, komodo jantan terkuat memiliki dua kemungkinan pergerakan dengan probabilitas seimbang (0.5): tertarik menuju atau menjauh dari jantan lain. Sementara itu, jantan besar yang lebih lemah akan selalu bergerak mendekati jantan yang lebih kuat. Strategi ini mencerminkan eksploitasi tinggi karena sebagian besar pergerakan mengarah ke solusi yang lebih baik, dengan eksplorasi terbatas melalui probabilitas menjauh.
Kelompok kedua adalah komodo betina, mewakili solusi menengah dengan karakteristik Medium Exploitation, Medium Exploration (MEME). Betina memiliki dua pilihan dengan probabilitas sama (0.5): menikah dengan jantan terkuat atau melakukan parthenogenesis (berkembang biak tanpa perkawinan). Perkawinan dengan jantan terkuat merepresentasikan eksploitasi, sementara parthenogenesis membuka peluang eksplorasi solusi baru. Keseimbangan antara kedua pilihan ini menciptakan karakteristik medium baik untuk eksploitasi maupun eksplorasi.
Kelompok ketiga adalah komodo jantan kecil, mewakili solusi terlemah dengan strategi Low Exploitation, High Exploration (LEHE). Meskipun jantan kecil tertarik ke jantan besar, mereka tidak mengikuti semua dimensi pergerakan. Pemilihan dimensi yang diikuti menggunakan distribusi seragam berdasarkan mlipir rate. Pendekatan ini menciptakan eksplorasi tinggi karena hanya sebagian dimensi yang diikuti, sementara eksploitasi tetap terjaga melalui ketertarikan pada solusi yang lebih baik.
Dalam implementasi KMA, terdapat tiga parameter kunci yang perlu ditetapkan:

n (jumlah populasi): menentukan ukuran ruang pencarian
p (proporsi jantan besar): mempengaruhi keseimbangan antara eksploitasi dan eksplorasi
Tingkat mlipir: mengontrol seberapa ekstensif eksplorasi yang dilakukan jantan kecil

Keseimbangan unik antara eksploitasi dan eksplorasi pada ketiga kelompok ini memungkinkan KMA untuk mencari solusi optimal secara efektif, dengan masing-masing kelompok memberikan kontribusi berbeda dalam proses pencarian."

#slide 9 (metodologi penelitian)
"Penelitian ini menggunakan dataset dari APOGEE Data Release 17, yang diambil menggunakan teleskop dengan cermin berdiameter 2,5 meter. Dataset ini mencakup sekitar 3.900 data spektrum bintang tunggal beserta parameter stellarnya.

Proses pengolahan data dilakukan dalam beberapa tahap kritis. Tahap pertama adalah preprocessing data spektrum. Mengingat spektrum bintang seringkali memiliki titik-titik flux yang kosong, dilakukan interpolasi untuk mengisi kekosongan tersebut, memastikan kontinuitas data yang penting untuk proses pembelajaran model.

Selanjutnya, dilakukan normalisasi data spektrum dengan pendekatan yang unik. Spektrum dibagi menjadi tiga bagian berdasarkan panjang gelombang: red chip, green chip, dan blue chip. Setiap bagian dinormalisasi secara terpisah dengan membagi nilai flux pada setiap elemen dengan nilai median dari chip yang bersesuaian. Pendekatan ini membantu menstandarisasi data sambil mempertahankan karakteristik spektral yang penting pada setiap rentang panjang gelombang.

Parameter stellar juga melalui proses normalisasi menggunakan nilai rata-rata dan standar deviasi. Normalisasi ini sangat penting mengingat perbedaan skala yang signifikan antar parameter. Sebagai contoh, temperatur efektif memiliki rentang nilai yang jauh lebih besar dibandingkan parameter lainnya. Normalisasi memastikan bahwa setiap parameter memberikan kontribusi yang seimbang dalam proses pembelajaran model.

Dataset yang telah dinormalisasi kemudian dibagi menjadi dua bagian: 80% untuk data training dan 20% untuk data testing. Pembagian ini memungkinkan evaluasi yang objektif terhadap performa model.

Untuk menguji efektivitas optimasi hyperparameter menggunakan KMA, dirancang empat skenario eksperimen:
Skenario 1 menjadi baseline, menggunakan model CNN standar dengan hyperparameter default tanpa optimasi. Skenario ini akan menjadi pembanding untuk mengukur peningkatan performa dari optimasi.
Skenario 2, 3, dan 4 menggunakan model CNN dengan hyperparameter yang dioptimasi menggunakan KMA, masing-masing dengan ukuran populasi 5, 10, dan 15. Variasi ukuran populasi ini memungkinkan kita menganalisis pengaruh kompleksitas pencarian terhadap kualitas optimasi.
Evaluasi performa model akan menggunakan tiga metrik:

Mean Square Error (MSE) untuk mengukur rata-rata kesalahan kuadrat
Root Mean Square Error (RMSE) untuk memberikan estimasi kesalahan dalam skala yang sama dengan data asli
Plot residu untuk analisis visual distribusi kesalahan prediksi

Kombinasi metrik ini akan memberikan pemahaman komprehensif tentang efektivitas optimasi hyperparameter dalam meningkatkan akurasi prediksi parameter stellar."

#slide 10 (encoding hyperparameter
"Dalam mengoptimasi hyperparameter menggunakan KMA, kita perlu melakukan encoding atau pemetaan nilai-nilai hyperparameter ke dalam bentuk yang dapat diproses oleh algoritma. Mari saya jelaskan bagaimana setiap hyperparameter direpresentasikan.

Learning rate, yang mengontrol seberapa besar langkah pembelajaran model, dipetakan dari range eksponensial 10^-6 hingga 10^-1 menjadi nilai diskrit 1 hingga 6. Penggunaan skala eksponensial ini memungkinkan eksplorasi learning rate dalam rentang yang luas namun tetap efisien.

Untuk kernel size atau ukuran filter konvolusi, kita menggunakan range dari 16 hingga 64 piksel yang dipetakan ke nilai 1 hingga 7. Range ini mencakup ukuran filter yang umum digunakan dalam arsitektur CNN, dari filter yang relatif kecil untuk mendeteksi fitur detail, hingga filter yang lebih besar untuk menangkap pola spektral yang lebih luas.

Kernel initializer, yang menentukan bagaimana bobot awal jaringan diinisialisasi, memiliki 13 opsi berbeda yang dipetakan ke nilai 1 hingga 13. Pilihan ini mencakup berbagai metode inisialisasi populer seperti zeros, ones, distribusi normal dan uniform, serta metode khusus seperti He initialization dan Glorot initialization. Setiap metode inisialisasi ini memiliki karakteristik unik yang dapat mempengaruhi proses pembelajaran model.

Fungsi aktivasi, yang menentukan non-linearitas dalam jaringan, memiliki lima pilihan umum: ReLU, tanh, sigmoid, ELU, dan SELU, yang dipetakan ke nilai 1 hingga 7. Masing-masing fungsi aktivasi ini memiliki karakteristik yang berbeda dalam menangani gradien dan menghadapi masalah seperti vanishing gradient.

Untuk epoch atau jumlah iterasi pembelajaran, kita menggunakan range diskrit antara 50 hingga 100. Begitu pula dengan pool size yang menggunakan range diskrit 2 hingga 9, menentukan ukuran operasi pooling dalam jaringan.

Terakhir, batch size direpresentasikan dalam bentuk 2 pangkat i, dimana i adalah bilangan bulat antara 0 hingga 6. Ini menghasilkan ukuran batch yang umum digunakan seperti 1, 2, 4, 8, 16, 32, dan 64.

Encoding ini dirancang untuk memudahkan proses optimasi sambil tetap mencakup range nilai yang relevan untuk setiap hyperparameter. Pemetaan ke nilai diskrit juga membantu KMA dalam melakukan pencarian yang lebih efisien dalam ruang hyperparameter."

#slide 11 (decoding formula)
"Setelah kita membahas encoding hyperparameter, penting untuk memahami bagaimana proses decoding dilakukan. Perlu diketahui bahwa Komodo Mlipir Algorithm (KMA) beroperasi dalam rentang bilangan real antara 0 hingga 1. Oleh karena itu, kita membutuhkan formula decoding untuk mengembalikan nilai-nilai tersebut ke range hyperparameter yang sebenarnya.
Mari kita pahami formula decoding yang digunakan:
yi = bbi + xi * (bai - bbi)
Formula ini memiliki empat komponen penting:

yi adalah nilai hyperparameter akhir yang akan kita gunakan
xi adalah bilangan real antara 0 dan 1 yang merepresentasikan posisi individu komodo dalam algoritma
bbi (batas bawah) adalah nilai minimum dari range hyperparameter
bai (batas atas) adalah nilai maksimum dari range hyperparameter

Cara kerja formula ini bisa kita ilustrasikan dengan contoh sederhana. Misalkan kita ingin mendecode nilai learning rate. Jika xi yang dihasilkan KMA adalah 0.4, batas bawah (bbi) adalah 10^-6, dan batas atas (bai) adalah 10^-1, maka:
yi = 10^-6 + 0.4 * (10^-1 - 10^-6)

Formula ini pada dasarnya melakukan interpolasi linear, dimana xi bertindak sebagai proporsi antara batas bawah dan batas atas. Ketika xi = 0, hasil decoding akan sama dengan batas bawah. Ketika xi = 1, hasil decoding akan sama dengan batas atas. Nilai xi di antara 0 dan 1 akan menghasilkan nilai yang proporsional di antara kedua batas tersebut.

Pendekatan ini memungkinkan KMA untuk melakukan optimasi dalam ruang pencarian yang dinormalisasi (0-1) sambil tetap menghasilkan nilai hyperparameter yang sesuai dengan range yang dibutuhkan oleh model CNN."

#slide 12 (fitness function)
"Dalam optimasi hyperparameter menggunakan KMA, fitness function memainkan peran krusial sebagai kompas yang mengarahkan pencarian solusi optimal. Mari saya jelaskan fitness function yang digunakan dalam penelitian ini.
Fitness function yang kita gunakan memiliki formula:
1 / (train_mse + |train_mse - valid_mse| + ε)
Formula ini dirancang dengan sangat cermat untuk mencapai dua tujuan sekaligus. Pertama, kita ingin meminimalkan error prediksi (yang diukur dengan MSE). Kedua, kita ingin menghindari overfitting dengan memastikan model memiliki performa yang seimbang antara data training dan validasi.
Mari kita breakdown setiap komponen:

train_mse adalah mean square error yang diperoleh saat training. Semakin kecil nilainya, semakin baik model dalam mempelajari pola data training.
valid_mse adalah mean square error saat validasi. Ini mengukur kemampuan model untuk melakukan prediksi pada data yang belum pernah dilihat sebelumnya.
|train_mse - valid_mse| adalah nilai absolut dari selisih kedua MSE. Komponen ini sangat penting karena mengukur seberapa konsisten performa model antara data training dan validasi. Semakin kecil selisihnya, semakin baik - ini menandakan model tidak overfitting atau underfitting.
ε (epsilon) adalah nilai yang sangat kecil mendekati nol yang ditambahkan untuk menghindari error pembagian dengan nol.

Penggunaan pembagian 1 dengan jumlah komponen-komponen tersebut membuat fitness function ini bersifat maksimasi - semakin besar nilainya, semakin baik solusi yang ditemukan. Ini selaras dengan cara kerja KMA yang mencari nilai fitness maksimal.
Sebagai contoh, jika suatu solusi menghasilkan train_mse = 0.1 dan valid_mse = 0.12, dengan ε = 0.0001, maka:
Fitness = 1 / (0.1 + |0.1 - 0.12| + 0.0001) = 1 / 0.2201
Sedangkan jika solusi lain menghasilkan train_mse = 0.05 tetapi valid_mse = 0.2, maka meskipun train_mse-nya lebih kecil, fitness-nya akan lebih rendah karena selisih dengan valid_mse yang besar:
Fitness = 1 / (0.05 + |0.05 - 0.2| + 0.0001) = 1 / 0.2501
Dengan cara ini, fitness function mendorong algoritma untuk menemukan kombinasi hyperparameter yang menghasilkan model dengan performa tinggi dan stabil."

#slide 13 (hasil dan pembahasan training model standard)
"Mari kita analisis hasil pelatihan model CNN StarNet dengan konfigurasi standar atau default, yang merupakan bagian dari skenario pertama dalam penelitian ini.
Model ini menggunakan konfigurasi hyperparameter yang umum dalam arsitektur CNN. Pada layer konvolusi, kita menggunakan kernel size 16 untuk layer pertama dan 32 untuk layer kedua, yang memungkinkan model untuk menangkap pola spektral dari yang sederhana hingga yang lebih kompleks. Fungsi aktivasi ReLU dipilih untuk semua layer karena kemampuannya mengatasi masalah vanishing gradient dan menghasilkan aktivasi sparse yang efisien secara komputasional.

Inisialisasi kernel menggunakan metode he_normal, yang dirancang khusus untuk fungsi aktivasi ReLU, membantu mencegah gradien yang terlalu kecil atau terlalu besar di awal pelatihan. Learning rate ditetapkan pada 0.001, yang merupakan nilai default yang cukup umum digunakan sebagai titik awal. Batch size 32 dipilih untuk menyeimbangkan antara kecepatan pelatihan dan penggunaan memori.

Jika kita perhatikan grafik proses pembelajaran, ada beberapa observasi menarik. Di awal pelatihan, terlihat lonjakan error training yang sangat tinggi mencapai nilai MSE sekitar 35. Ini adalah fenomena yang normal saat model masih 'mencari-cari' pola dalam data. Yang menggembirakan, model dengan cepat mampu menurunkan error ini secara drastis dalam beberapa epoch pertama.

Setelah epoch ke-20, both training dan validation loss menunjukkan konvergensi yang stabil, ditandai dengan kurva yang relatif datar. Ini mengindikasikan bahwa model telah mencapai titik optimal dalam pembelajaran. Yang lebih penting, gap antara training loss dan validation loss sangat kecil dan konsisten sepanjang proses pelatihan, menunjukkan bahwa model tidak mengalami overfitting.

Meskipun performa model standar ini sudah cukup baik dalam hal konvergensi dan stabilitas, masih ada ruang untuk peningkatan melalui optimasi hyperparameter. Hasil ini akan menjadi baseline yang baik untuk membandingkan efektivitas optimasi menggunakan KMA pada skenario-skenario berikutnya."

#slide 14 dan 15 (hasil kma n = 5)
"Mari kita analisis hasil optimasi hyperparameter menggunakan KMA dengan populasi (n) = 5. Hasil ini menunjukkan bagaimana algoritma KMA bekerja dalam menemukan kombinasi hyperparameter optimal untuk arsitektur StarNet.

Jika kita perhatikan grafik fitness value terhadap generasi, kita dapat melihat pola yang sangat menarik. Pada dua generasi pertama, nilai fitness relatif stabil di sekitar 1.8, menunjukkan fase eksplorasi awal algoritma. Namun, terjadi peningkatan dramatis antara generasi ke-2 dan ke-4, dimana nilai fitness melonjak hingga mencapai sekitar 3.0. Setelah generasi ke-4, nilai fitness mencapai plateau dan tetap stabil hingga generasi ke-10, mengindikasikan algoritma telah menemukan solusi yang optimal.

Kombinasi hyperparameter yang ditemukan menunjukkan beberapa pola yang menarik:
Untuk layer konvolusi pertama, algoritma memilih kernel size yang cukup besar (40) dengan aktivasi tanh dan inisialisasi glorot_normal. Ini memungkinkan model untuk menangkap pola spektral yang lebih luas pada tahap awal. Sebaliknya, pada layer konvolusi kedua, kernel size yang lebih kecil (16) dipilih, memungkinkan model untuk fokus pada detail yang lebih halus, masih dengan aktivasi tanh tetapi menggunakan inisialisasi orthogonal.

Pemilihan pooling size 7 cukup agresif dalam mengurangi dimensionalitas, yang mungkin membantu model fokus pada fitur-fitur yang paling penting dalam spektrum.
Pada fully connected layer, kita melihat variasi menarik dalam fungsi aktivasi: elu untuk layer pertama dan sigmoid untuk layer kedua. Kombinasi ini memungkinkan model untuk menangkap baik pola linear maupun non-linear dalam data. Pemilihan inisialisasi yang berbeda-beda (random_uniform dan zeros) menunjukkan bahwa algoritma menemukan benefit dari keragaman ini.

Learning rate yang dipilih (0.0001) relatif kecil, menunjukkan preferensi untuk pembelajaran yang lebih hati-hati dan stabil. Batch size 32 dipertahankan, menunjukkan bahwa ini mungkin memang ukuran yang optimal untuk dataset kita. Jumlah epoch 81 menunjukkan bahwa algoritma menemukan titik optimal sebelum batas maksimum 100 epoch.

Yang menarik, output layer menggunakan aktivasi tanh dengan variance scaling initialization, yang dapat membantu dalam menormalkan output untuk prediksi parameter stellar yang telah dinormalisasi.

Konvergensi yang cepat dalam grafik fitness menunjukkan bahwa bahkan dengan populasi yang relatif kecil (n=5), KMA mampu menemukan solusi yang baik dalam waktu yang relatif singkat. Ini mengindikasikan efisiensi algoritma dalam melakukan eksplorasi ruang hyperparameter."

#slide 16 (model train n = 5)
"Mari kita analisis hasil pelatihan model CNN dengan hyperparameter yang telah dioptimasi menggunakan KMA dengan populasi n=5. Grafik ini memberikan wawasan menarik tentang proses pembelajaran model.

Pertama, perhatikan bahwa skala MSE pada grafik ini jauh lebih rendah dibandingkan dengan model standar sebelumnya. Sementara model standar memulai dengan MSE sekitar 35, model yang dioptimasi ini memulai dengan MSE hanya sekitar 1.0. Ini menunjukkan bahwa pemilihan hyperparameter oleh KMA memberikan titik awal yang jauh lebih baik untuk proses pembelajaran.

Proses pembelajaran dapat dibagi menjadi beberapa fase yang distinktif:
Fase awal (epoch 0-10):

Model memulai dengan MSE training sekitar 1.0 dan validation sekitar 0.9. Perbedaan yang relatif kecil ini menunjukkan model memiliki generalisasi yang baik sejak awal. Selama fase ini, kita melihat penurunan gradual dalam kedua nilai MSE.

Fase transisi (epoch 10-20):

Terjadi penurunan yang lebih signifikan dalam kedua nilai MSE. Ini menandakan model menemukan pola yang lebih baik dalam data. Yang menarik, validation loss tetap mengikuti training loss dengan sangat dekat, menunjukkan pembelajaran yang sehat tanpa tanda-tanda overfitting.

Fase pembelajaran stabil (epoch 20-50):

Kurva pembelajaran menjadi lebih landai namun tetap menunjukkan tren penurunan yang konsisten. Pola 'zig-zag' kecil dalam validation loss menunjukkan model terus melakukan fine-tuning terhadap parameternya.

Fase akhir (epoch 50-81):

Model terus menunjukkan peningkatan bertahap hingga akhir pelatihan, mencapai MSE training sekitar 0.35 dan validation sekitar 0.3. Yang sangat menggembirakan, validation loss tetap sedikit lebih rendah dari training loss, menunjukkan model memiliki kemampuan generalisasi yang sangat baik.

#slide 17-18 (KMA n =10)
"Mari kita analisis hasil pencarian hyperparameter optimal menggunakan KMA dengan populasi n=10, yang menunjukkan pola optimasi yang sangat menarik.

Pada grafik fitness value, kita melihat pola yang berbeda dari kasus n=5 sebelumnya. Untuk enam generasi pertama, nilai fitness relatif stabil di sekitar 4.25, menunjukkan fase eksplorasi yang lebih lama. Namun, yang sangat menarik terjadi antara generasi ke-6 dan ke-8, dimana terdapat lonjakan dramatis nilai fitness hingga mencapai sekitar 6.0. Setelah itu, nilai fitness tetap stabil hingga generasi ke-10, mengindikasikan konvergensi ke solusi optimal.

Kombinasi hyperparameter yang ditemukan menunjukkan beberapa perbedaan signifikan dibanding kasus n=5:

Dalam arsitektur konvolusi, KMA memilih pendekatan yang lebih progresif. Layer konvolusi pertama menggunakan kernel size 32 dengan inisialisasi random_normal, sementara layer kedua menggunakan kernel size yang lebih besar (48) dengan inisialisasi orthogonal. Ini menciptakan hierarki ekstraksi fitur yang menarik - dari fitur menengah ke fitur yang lebih luas. Kedua layer tetap menggunakan aktivasi tanh, menunjukkan konsistensi dalam cara model menangani non-linearitas.

Berbeda dengan kasus n=5, pooling size dipilih jauh lebih konservatif (2 vs 7 sebelumnya). Ini menunjukkan preferensi untuk mempertahankan lebih banyak informasi spasial dalam proses pembelajaran.

Pada fully connected layer, kita melihat kombinasi fungsi aktivasi yang lebih bervariasi: sigmoid → tanh → elu (output). Ini menciptakan pipeline transformasi yang lebih kompleks, memungkinkan model untuk menangkap berbagai jenis pola dalam data. Pemilihan kernel initializer juga lebih sophisticated: truncated_normal → lecun_normal → glorot_normal, menunjukkan preferensi untuk metode inisialisasi yang lebih modern.

Learning rate tetap di 0.0001, konsisten dengan kasus n=5, mengkonfirmasi bahwa ini mungkin memang learning rate optimal untuk problem ini. Namun, yang sangat menarik adalah pemilihan batch size 1 (stochastic gradient descent murni) dan epoch 66, yang cukup berbeda dari kasus sebelumnya.

Peningkatan signifikan dalam nilai fitness (dari ~3.0 di n=5 menjadi ~6.0 di n=10) menunjukkan bahwa populasi yang lebih besar memungkinkan KMA untuk mengeksplorasi ruang solusi dengan lebih efektif. Meskipun fase eksplorasi awal lebih lama, algoritma akhirnya menemukan solusi yang jauh lebih optimal menurut metrik fitness yang kita gunakan."

#slide 19 (model train n =10)
"Mari kita analisis hasil pelatihan model CNN dengan hyperparameter yang dioptimasi menggunakan KMA dengan populasi n=10. Hasilnya menunjukkan perbaikan yang signifikan dibandingkan dengan konfigurasi n=5 sebelumnya.

Grafik pembelajaran menunjukkan pola yang sangat menarik. Model memulai dengan MSE sekitar 0.8, yang jauh lebih rendah dibandingkan model standar yang memulai di angka 35. Ini menunjukkan bahwa kombinasi hyperparameter yang ditemukan KMA memberikan kondisi awal yang lebih baik untuk pembelajaran.

Proses pembelajaran dapat dibagi menjadi beberapa fase yang distinktif. Pada 10 epoch pertama, kita melihat penurunan error yang sangat cepat dan dramatis, dari 0.8 menjadi sekitar 0.2. Fase pembelajaran cepat ini menunjukkan bahwa model dengan cepat menemukan pola-pola utama dalam data spektrum bintang.

Setelah epoch ke-10, proses pembelajaran memasuki fase yang lebih halus dan stabil. Error rate terus menurun tetapi dengan laju yang lebih lambat, menandakan model sedang melakukan fine-tuning terhadap pemahaman pola-pola yang lebih halus dalam data. Yang sangat menggembirakan, kurva validation loss mengikuti training loss dengan sangat dekat, dengan sedikit fluktuasi yang normal, menunjukkan model memiliki kemampuan generalisasi yang baik.

Dibandingkan dengan model standar yang mencapai error sekitar 0.1, model ini mencapai error yang sedikit lebih tinggi (sekitar 0.17-0.18). Namun, ada beberapa aspek positif yang perlu diperhatikan. Pertama, pembelajaran lebih stabil tanpa lonjakan error di awal. Kedua, gap antara training dan validation loss sangat minimal, menunjukkan model yang robust. Ketiga, kurva pembelajaran lebih smooth, menandakan proses optimasi yang lebih stabil.

Yang menarik, penggunaan batch size 1 (stochastic gradient descent) tidak menyebabkan fluktuasi yang berlebihan dalam kurva pembelajaran seperti yang mungkin dikhawatirkan. Ini mungkin karena kombinasi dengan learning rate yang kecil (0.0001) dan arsitektur yang seimbang antara layer konvolusi dan fully connected.

Meskipun performa akhir masih sedikit di bawah model standar dalam hal error absolut, hasil ini menunjukkan bahwa KMA dengan n=10 mampu menemukan konfigurasi yang menghasilkan proses pembelajaran yang lebih stabil dan terkontrol. Ini bisa menjadi trade-off yang berharga dalam beberapa skenario, terutama ketika stabilitas dan predictability proses pembelajaran menjadi prioritas."

#slide 20 (kma n = 15)
"Mari kita analisis hasil optimasi hyperparameter menggunakan KMA dengan populasi terbesar dalam penelitian ini, yaitu n=15. Grafik fitness value menunjukkan pola pencarian yang sangat informatif.

Perbaikan fitness value terjadi lebih cepat dibandingkan dengan kasus n=5 dan n=10. Pada dua generasi pertama, kita melihat peningkatan yang sangat tajam dari sekitar 4.5 menjadi 6.0. Ini menunjukkan bahwa populasi yang lebih besar memungkinkan KMA untuk menemukan solusi yang lebih baik dengan lebih cepat, karena ruang pencarian bisa dieksplorasi lebih efektif.

Setelah lonjakan awal tersebut, terjadi plateau singkat antara generasi 2 hingga 4, menandakan algoritma sedang melakukan eksplorasi lebih detail di sekitar solusi yang menjanjikan. Kemudian terjadi peningkatan kecil namun signifikan di sekitar generasi ke-6, mencapai nilai fitness sekitar 6.4, yang kemudian stabil hingga generasi ke-10.

Kombinasi hyperparameter yang ditemukan menunjukkan pendekatan yang menarik:
Untuk arsitektur konvolusi, KMA memilih struktur yang progresif namun lebih konservatif. Layer konvolusi pertama menggunakan kernel size 16 dengan inisialisasi variance_scaling, yang baik untuk menangani variasi dalam input. Layer kedua menggunakan kernel size 32 dengan inisialisasi lecun_normal, menciptakan hierarki ekstraksi fitur yang natural - dari detil ke pola yang lebih besar. Konsistensi penggunaan aktivasi tanh di kedua layer menunjukkan bahwa fungsi aktivasi ini mungkin memang optimal untuk kasus spektrum bintang.

Pooling size 3 merupakan pilihan moderat antara kasus n=5 (yang menggunakan 7) dan n=10 (yang menggunakan 2). Ini menyiratkan bahwa dengan populasi yang lebih besar, KMA mampu menemukan keseimbangan yang lebih baik antara reduksi dimensi dan preservasi informasi.

Yang menarik, nilai fitness akhir (6.4) lebih tinggi dari kasus n=10 (6.0) dan jauh lebih tinggi dari n=5 (3.0). Ini mengkonfirmasi hipotesis bahwa populasi yang lebih besar memungkinkan eksplorasi ruang solusi yang lebih efektif. Peningkatan yang konsisten dalam nilai fitness maksimum seiring dengan bertambahnya ukuran populasi (3.0 → 6.0 → 6.4) menunjukkan bahwa KMA mampu memanfaatkan informasi dari populasi yang lebih besar untuk menemukan solusi yang lebih optimal.

Arsitektur fully connected layer menunjukkan pola transformasi yang sangat menarik. Layer pertama menggunakan aktivasi sigmoid dengan inisialisasi variance_scaling. Pemilihan ini cerdas karena sigmoid membantu 'memadatkan' fitur-fitur yang telah diekstrak oleh layer konvolusi ke dalam range [0,1], sementara variance_scaling memastikan inisialisasi bobot yang tepat berdasarkan ukuran input, mencegah masalah vanishing atau exploding gradients.

Layer fully connected kedua menggunakan kombinasi aktivasi tanh dengan random_uniform initialization. Tanh, dengan range [-1,1], memungkinkan model untuk membuat transformasi yang lebih ekspresif dibandingkan sigmoid, sementara random_uniform memberikan titik awal yang terdistribusi merata untuk bobot-bobotnya. Ini menciptakan lapisan intermediate yang bisa menangkap pola-pola kompleks dalam data spektrum.

Yang sangat menarik adalah pemilihan SELU (Scaled Exponential Linear Unit) untuk output layer, dipasangkan dengan variance_scaling initialization. SELU adalah pilihan yang sophisticated karena memiliki sifat self-normalizing, yang berarti ia bisa membantu menjaga distribusi aktivasi tetap stabil sepanjang proses pembelajaran. Ini sangat penting untuk prediksi parameter stellar yang membutuhkan presisi tinggi.

Learning rate 0.0001 konsisten dengan konfigurasi n=5 dan n=10, semakin memperkuat bahwa ini memang learning rate optimal untuk problem ini. Batch size 8 merupakan pilihan yang seimbang - lebih besar dari kasus n=10 (yang menggunakan batch size 1) namun tetap cukup kecil untuk memungkinkan update parameter yang lebih frequent dibandingkan batch size yang lebih besar. Jumlah epoch 73 menunjukkan bahwa model membutuhkan waktu pembelajaran yang moderat untuk mencapai konvergensi.
Secara keseluruhan, konfigurasi yang ditemukan dengan n=15 menunjukkan tingkat sophistikasi yang lebih tinggi dibanding kasus sebelumnya. KMA memanfaatkan populasi yang lebih besar untuk menemukan kombinasi hyperparameter yang menciptakan pipeline pembelajaran yang lebih kompleks namun seimbang:

Konvolusi progresif untuk ekstraksi fitur (16 → 32)
Pooling moderat untuk reduksi dimensi (size 3)
Transformasi non-linear yang bertahap (tanh → sigmoid → tanh → selu)
Update parameter yang well-paced (batch size 8, learning rate 0.0001)

Peningkatan nilai fitness yang konsisten (3.0 → 6.0 → 6.4) mengindikasikan bahwa populasi yang lebih besar membantu KMA menemukan solusi yang lebih optimal. Sekarang, akan sangat menarik untuk melihat bagaimana konfigurasi ini mempengaruhi performa aktual model dalam prediksi parameter stellar."

#slide 22 (model train n = 15)

"Mari kita analisis hasil pelatihan model CNN dengan hyperparameter yang dioptimasi menggunakan KMA dengan populasi n=15. Grafik pembelajaran ini menunjukkan beberapa karakteristik yang sangat menarik.

Model memulai dengan MSE sekitar 1.0, dan menunjukkan pola pembelajaran yang sangat bersih dan efisien. Dalam 10 epoch pertama, kita melihat penurunan error yang cepat dan konsisten, dari 1.0 menjadi sekitar 0.2. Fase pembelajaran awal yang cepat ini menunjukkan bahwa kombinasi hyperparameter yang ditemukan KMA sangat efektif dalam membantu model menemukan pola-pola utama dalam data spektrum bintang.

Setelah epoch ke-20, proses pembelajaran memasuki fase yang lebih halus. Error rate terus menurun dengan laju yang lebih gradual, yang merupakan indikasi bahwa model sedang melakukan fine-tuning terhadap pola-pola yang lebih subtle dalam data. Yang sangat menggembirakan, kurva validation loss mengikuti training loss dengan sangat dekat sepanjang proses pembelajaran, dengan fluktuasi minimal. Kedekatan ini menunjukkan bahwa model memiliki kemampuan generalisasi yang sangat baik - apa yang dipelajari dari data training dapat diterapkan dengan baik pada data yang belum pernah dilihat sebelumnya.

Jika kita bandingkan dengan hasil sebelumnya, model ini menunjukkan beberapa keunggulan. Dibandingkan dengan n=10 yang mencapai error sekitar 0.17-0.18, model ini mencapai error yang sedikit lebih rendah di kisaran 0.15. Kurva pembelajaran juga lebih smooth dan stabil, menunjukkan bahwa kombinasi batch size 8 dengan learning rate 0.0001 memberikan keseimbangan yang baik antara kecepatan pembelajaran dan stabilitas.

Meskipun error akhir masih sedikit lebih tinggi dibandingkan model standar (yang mencapai 0.1), model ini menunjukkan karakteristik pembelajaran yang lebih diinginkan: konvergensi yang stabil, generalisasi yang baik, dan tidak ada tanda-tanda overfitting. Arsitektur yang ditemukan KMA dengan n=15 telah menciptakan pipeline pembelajaran yang sangat efektif, dimana setiap komponen - dari layer konvolusi hingga output layer dengan aktivasi SELU - bekerja sama dengan harmonis untuk mengekstrak dan memproses informasi dari spektrum bintang.

Hasil ini menunjukkan bahwa meningkatkan ukuran populasi dalam KMA dari 5 ke 15 memang menghasilkan perbaikan dalam performa model. Meskipun peningkatan dari n=10 ke n=15 tidak sedramatis dari n=5 ke n=10, setiap peningkatan ukuran populasi telah menghasilkan konfigurasi yang semakin baik, menunjukkan bahwa KMA mampu memanfaatkan informasi dari populasi yang lebih besar untuk menemukan solusi yang lebih optimal."


#slide 24 (hasil keseluruhan)
"Mari kita lakukan analisis komprehensif terhadap hasil evaluasi keempat model yang telah kita kembangkan. Evaluasi ini memberikan gambaran yang sangat menarik tentang efektivitas berbagai konfigurasi yang telah kita uji.

Model Standar, dengan RMSE 45.383 dan MSE 2059.595, ternyata menunjukkan performa terbaik di antara semua konfigurasi. Ini adalah temuan yang sangat informatif karena menunjukkan bahwa konfigurasi default StarNet telah didesain dengan sangat baik untuk kasus prediksi parameter stellar. Hal ini masuk akal mengingat arsitektur StarNet memang dikembangkan secara khusus untuk analisis spektrum bintang.

Ketika kita melihat hasil optimasi menggunakan KMA, kita menemukan pola yang sangat menarik. Dengan populasi n=5, model menghasilkan RMSE 102.422 dan MSE 10490.3572, yang merupakan performa terlemah dari semua konfigurasi. Ini menunjukkan bahwa populasi yang terlalu kecil mungkin tidak memberikan ruang eksplorasi yang cukup bagi KMA untuk menemukan kombinasi hyperparameter yang optimal.

Peningkatan ukuran populasi menjadi n=10 menghasilkan perbaikan yang signifikan, dengan RMSE menurun menjadi 86.742 dan MSE 7524.1088. Penurunan error ini mengkonfirmasi bahwa populasi yang lebih besar memungkinkan KMA untuk melakukan eksplorasi yang lebih efektif dalam ruang hyperparameter.

Hasil paling menjanjikan dari optimasi KMA dicapai dengan populasi n=15, yang menghasilkan RMSE 58.339 dan MSE 3403.4551. Meskipun masih di atas model standar, peningkatan performa ini sangat signifikan dibandingkan dengan konfigurasi n=5 dan n=10. Ini menunjukkan tren positif dimana peningkatan ukuran populasi secara konsisten menghasilkan model yang lebih baik.
Beberapa pembelajaran kunci yang dapat kita ambil dari hasil ini:

Arsitektur default StarNet terbukti sangat robust untuk kasus prediksi parameter stellar, menunjukkan pentingnya domain expertise dalam desain arsitektur neural network.
KMA menunjukkan potensi yang menjanjikan, dengan performa yang terus meningkat seiring bertambahnya ukuran populasi. Tren ini mengindikasikan bahwa populasi yang lebih besar lagi mungkin bisa menghasilkan performa yang lebih baik lagi.

Trade-off antara kompleksitas komputasi dan peningkatan performa perlu dipertimbangkan. Meskipun populasi yang lebih besar menghasilkan performa yang lebih baik, peningkatan dari n=10 ke n=15 tidak sedramatis dari n=5 ke n=10.
Meskipun belum melampaui model standar, optimasi dengan KMA berhasil menghasilkan model dengan karakteristik pembelajaran yang lebih stabil dan proses konvergensi yang lebih terstruktur.

Hasil ini membuka beberapa arah potensial untuk penelitian lanjutan, seperti eksperimen dengan ukuran populasi yang lebih besar, modifikasi fitness function, atau kombinasi dengan teknik optimasi lainnya. Yang paling penting, penelitian ini telah memberikan wawasan berharga tentang dinamika optimasi hyperparameter dalam konteks prediksi parameter stellar."

#slide 25 -26
"Mari kita analisis secara mendalam hasil evaluasi untuk parameter temperatur efektif (Teff) dari keempat model yang telah dikembangkan.
Model Standar menunjukkan performa yang paling baik dalam memprediksi temperatur efektif, dengan RMSE 90.738 Kelvin dan presisi ±4% dari rentang temperatur. Rata-rata error yang relatif rendah (15.71) dan standar deviasi 89.37 menunjukkan bahwa prediksi model sangat konsisten. Jika kita perhatikan plot residunya, terlihat distribusi error yang cukup merata di sekitar nol, dengan sedikit kecenderungan underestimation pada temperatur yang lebih tinggi.

Ketika kita beralih ke model dengan optimasi KMA n=5, kita melihat penurunan performa yang signifikan. RMSE meningkat menjadi 204.820 K dengan presisi ±10.24% dari rentang. Rata-rata error yang tinggi (49.02) dan standar deviasi yang besar (198.87) mengindikasikan prediksi yang kurang stabil. Plot residu menunjukkan pola linear yang jelas, mengindikasikan bias sistematis dalam prediksi - model cenderung overestimate pada temperatur rendah dan underestimate pada temperatur tinggi.
Model dengan KMA n=10 menunjukkan perbaikan dibandingkan n=5, namun masih di bawah model standar. RMSE 173.476 K dengan presisi ±8.64% menunjukkan peningkatan akurasi, meskipun rata-rata error (37.17) dan standar deviasi (169.31) masih cukup tinggi. Plot residunya menunjukkan pola yang mirip dengan n=5 tetapi dengan dispersi yang lebih kecil.

Peningkatan signifikan terlihat pada model dengan KMA n=15, yang menghasilkan RMSE 116.668 K dan presisi ±5.83%. Rata-rata error menurun drastis menjadi 19.68, mendekati performa model standar. Plot residunya menunjukkan distribusi yang lebih merata dibandingkan n=5 dan n=10, meskipun masih ada sedikit pola sistematis.
Yang menarik untuk dicatat adalah bagaimana distribusi error (ditunjukkan oleh histogram di sebelah kanan setiap plot) berevolusi dari satu model ke model lainnya. Model standar menunjukkan distribusi yang paling mendekati normal dengan peak yang tajam di sekitar nol. Seiring dengan peningkatan n dalam KMA, kita melihat distribusi error yang secara bertahap menjadi lebih terkonsentrasi, menunjukkan peningkatan konsistensi dalam prediksi.

Tren perbaikan performa seiring dengan peningkatan ukuran populasi KMA (dari n=5 ke n=15) menunjukkan bahwa algoritma ini mampu menemukan konfigurasi yang lebih baik ketika diberikan ruang pencarian yang lebih luas. Meskipun belum melampaui model standar, perbaikan yang konsisten ini mengindikasikan potensi untuk optimasi lebih lanjut, mungkin dengan ukuran populasi yang lebih besar atau modifikasi pada fitness function yang lebih spesifik untuk prediksi temperatur."

#slide 27-28
"Mari kita analisis secara mendalam hasil evaluasi untuk parameter gravitasi permukaan (log g) dari keempat model yang dikembangkan. Parameter ini sangat penting karena memberikan informasi tentang massa dan radius bintang.

Model Standar menunjukkan performa yang sangat baik dalam memprediksi log g, dengan RMSE 0.1353 dan presisi ±8.46% dari rentang nilai. Rata-rata error yang sangat kecil (-0.02) dan standar deviasi 0.13 menunjukkan prediksi yang sangat konsisten. Plot residunya menunjukkan distribusi error yang relatif merata di sekitar nol, dengan sedikit penyebaran pada nilai log g yang lebih tinggi.

Ketika beralih ke model dengan KMA n=5, kita melihat sedikit penurunan performa. RMSE meningkat menjadi 0.1887 dengan presisi ±11.87% dari rentang. Meskipun rata-rata error (0.03) masih cukup kecil, peningkatan standar deviasi menjadi 0.19 mengindikasikan prediksi yang lebih bervariasi. Plot residunya menunjukkan pola yang lebih tersebar dengan kecenderungan underestimate pada nilai log g yang lebih tinggi.

Model dengan KMA n=10 menunjukkan performa yang sedikit lebih baik dari n=5, namun masih belum melampaui model standar. RMSE 0.1622 dengan presisi ±10.14% menunjukkan perbaikan, dan rata-rata error yang mendekati nol (-0.00) sangat menggembirakan. Namun, standar deviasi 0.17 masih menunjukkan variabilitas yang cukup tinggi dalam prediksi.

Yang sangat menarik terjadi pada model dengan KMA n=15, yang justru menunjukkan performa sedikit lebih baik dari model standar. RMSE 0.1248 dengan presisi ±7.8% merupakan hasil terbaik di antara semua model. Rata-rata error yang sangat kecil (-0.00) dan standar deviasi 0.13 yang setara dengan model standar menunjukkan prediksi yang sangat akurat dan konsisten.

Distribusi error yang ditunjukkan oleh histogram di sebelah kanan setiap plot juga menunjukkan evolusi yang menarik. Model standar dan KMA n=15 menunjukkan distribusi yang sangat mirip - berbentuk bell curve yang tajam dan simetris di sekitar nol. Ini mengindikasikan bahwa kedua model memiliki karakteristik error yang sangat serupa dan well-behaved.

Temuan ini sangat signifikan karena menunjukkan bahwa untuk parameter log g, optimasi dengan KMA n=15 berhasil menemukan konfigurasi yang tidak hanya setara tetapi bahkan sedikit lebih baik dari model standar. Ini mungkin mengindikasikan bahwa prediksi gravitasi permukaan lebih responsif terhadap optimasi hyperparameter dibandingkan temperatur efektif yang kita lihat sebelumnya.

Tren perbaikan performa seiring peningkatan ukuran populasi KMA (dari n=5 ke n=15) juga sangat konsisten, menunjukkan bahwa algoritma ini sangat efektif dalam menemukan konfigurasi optimal untuk prediksi log g ketika diberikan ruang pencarian yang cukup. Keberhasilan ini membuka kemungkinan menarik untuk pengembangan lebih lanjut, mungkin dengan fokus khusus pada optimasi untuk parameter-parameter stellar spesifik."

#slide 29-30
"Mari kita analisis hasil evaluasi untuk parameter metalisitas ([M/H]), yang merupakan indikator penting tentang kelimpahan unsur-unsur berat dalam bintang relatif terhadap hidrogen.

Model Standar menunjukkan performa yang sangat baik dalam memprediksi metalisitas, dengan RMSE 0.0500 dan presisi ±4% dari rentang nilai. Rata-rata error yang sangat kecil (0.01) dan standar deviasi 0.05 menunjukkan prediksi yang sangat akurat dan konsisten. Jika kita perhatikan plot residunya, kita melihat distribusi error yang merata di sekitar nol dengan pola yang menyerupai awan titik, menandakan tidak adanya bias sistematis yang signifikan.

Ketika beralih ke model dengan KMA n=5, kita melihat penurunan performa yang cukup signifikan. RMSE meningkat hampir dua kali lipat menjadi 0.0950 dengan presisi ±7.5% dari rentang. Meskipun rata-rata error (0.00) terlihat baik, peningkatan standar deviasi menjadi 0.09 mengindikasikan prediksi yang lebih tidak stabil. Plot residunya menunjukkan pola linear yang jelas, mengindikasikan adanya bias sistematis dalam prediksi - model cenderung overestimate pada metalisitas rendah dan underestimate pada metalisitas tinggi.

Model dengan KMA n=10 menunjukkan perbaikan dibandingkan n=5, namun masih belum mencapai performa model standar. RMSE 0.0758 dengan presisi ±6.32% menunjukkan langkah perbaikan yang signifikan. Rata-rata error 0.00 sangat baik, meskipun standar deviasi 0.08 masih lebih tinggi dari model standar. Plot residunya menunjukkan pola bias yang masih ada namun lebih ringan dibandingkan n=5.

Yang sangat menarik terjadi pada model dengan KMA n=15, yang mencapai performa yang hampir identik dengan model standar. RMSE 0.0508 dan presisi ±4.23% sangat mendekati nilai model standar. Rata-rata error yang sangat kecil (-0.00) dan standar deviasi 0.05 yang sama dengan model standar menunjukkan tingkat akurasi dan konsistensi yang setara. Plot residunya juga menunjukkan pola yang sangat mirip dengan model standar, dengan distribusi error yang lebih merata dan tidak menunjukkan bias sistematis yang signifikan.

Distribusi error yang ditunjukkan oleh histogram di sebelah kanan setiap plot menunjukkan evolusi yang sangat informatif. Model standar dan KMA n=15 menunjukkan distribusi yang hampir identik - berbentuk bell curve yang tajam dan simetris, sementara n=5 dan n=10 menunjukkan distribusi yang lebih lebar dan kurang simetris.
Hasil ini sangat menarik karena menunjukkan bahwa untuk parameter metalisitas, optimasi dengan KMA n=15 berhasil menemukan konfigurasi yang hampir sempurna menyamai performa model standar. Tren perbaikan yang konsisten dari n=5 ke n=15 juga mengindikasikan bahwa algoritma KMA sangat efektif dalam menemukan konfigurasi optimal ketika diberikan ruang pencarian yang cukup besar.

Temuan ini, bersama dengan hasil untuk parameter log g sebelumnya, menunjukkan bahwa KMA memiliki potensi yang sangat baik untuk optimasi hyperparameter dalam konteks prediksi parameter stellar, terutama ketika menggunakan ukuran populasi yang cukup besar."

#slide 31-32
Model Standar menunjukkan performa yang cukup baik dengan RMSE 2.2330 dan presisi ±4.5% dari rentang nilai. Namun, yang menarik adalah rata-rata error yang cukup signifikan (-0.62) dan standar deviasi 2.15, menunjukkan bahwa prediksi kecepatan rotasi memang lebih menantang dibandingkan parameter stellar lainnya. Plot residunya menunjukkan pola yang menyebar dengan kecenderungan underestimasi pada kecepatan rotasi yang lebih tinggi.

Ketika kita melihat model dengan KMA n=5, kita melihat penurunan performa yang cukup signifikan. RMSE meningkat menjadi 3.1494 dengan presisi ±6.3% dari rentang. Rata-rata error yang lebih besar (-0.79) dan standar deviasi yang meningkat menjadi 3.05 mengindikasikan prediksi yang kurang stabil. Plot residunya menunjukkan pola bias yang sangat jelas, dengan kecenderungan error yang meningkat seiring dengan meningkatnya kecepatan rotasi.

Namun, sesuatu yang sangat menarik terjadi pada model dengan KMA n=10. Terjadi peningkatan performa yang dramatis, bahkan melampaui model standar. RMSE menurun menjadi 1.504 dengan presisi ±3% dari rentang, yang merupakan hasil terbaik di antara semua model. Rata-rata error yang sangat kecil (-0.02) dan standar deviasi 1.5 menunjukkan prediksi yang lebih akurat dan konsisten. Plot residunya menunjukkan distribusi error yang lebih merata dan terkontrol.

Model dengan KMA n=15 mempertahankan performa yang sangat baik, dengan RMSE 1.5204 dan presisi ±2.98% dari rentang. Meskipun rata-rata error (0.30) sedikit lebih tinggi dari n=10, standar deviasi 1.49 yang hampir identik menunjukkan tingkat konsistensi yang serupa. Plot residunya sangat mirip dengan n=10, menunjukkan stabilitas dalam prediksi.

Yang sangat menarik dari hasil ini adalah bahwa untuk parameter kecepatan rotasi, optimasi KMA dengan n=10 dan n=15 justru menghasilkan performa yang lebih baik dari model standar. Ini adalah temuan yang signifikan karena menunjukkan bahwa optimasi hyperparameter dengan KMA sangat efektif untuk parameter yang lebih menantang seperti kecepatan rotasi.

Distribusi error yang ditunjukkan oleh histogram mengkonfirmasi perbaikan ini. Model KMA n=10 dan n=15 menunjukkan distribusi yang lebih tajam dan terpusat dibandingkan model standar, mengindikasikan prediksi yang lebih presisi.

Hasil ini memberikan wawasan penting bahwa efektivitas optimasi KMA dapat bervariasi tergantung pada parameter yang diprediksi. Untuk kecepatan rotasi, algoritma ini berhasil menemukan konfigurasi yang lebih optimal dibandingkan setting standar, menunjukkan potensi KMA dalam menangani parameter-parameter yang lebih kompleks dalam analisis spektral bintang."
