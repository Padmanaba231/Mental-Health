# Submission 1: Nama Proyek Anda
Nama: Putu Padmanaba

Username dicoding: Putu Padmanaba

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Mental Health Corpus](https://www.kaggle.com/datasets/reihanenamdari/mental-health-corpus/data) |
| Masalah | Kesehatan mental merupakan masalah penting yang seringkali disertai dengan komentar yang beracun di platform daring. Identifikasi dan mitigasi komentar beracun dapat membantu menciptakan lingkungan yang lebih aman dan mendukung bagi individu dengan masalah kesehatan mental. |
| Solusi machine learning | Mengembangkan model machine learning untuk mendeteksi komentar beracun dalam lingkungan platfrom daring. Model ini akan mengklasifikasikan komentar sebagai beracun atau tidak beracun dengan tujuan untuk mengurangi dampak negatif dari komentar beracun terhadap individu yang mengalami masalah kesehatan mental. |
| Metode pengolahan | Metode pengolahan pada proyek ini berupa pemisahan dataset menjadi data training dan data evaluasi dengan rasio 80:20. Fitur teks diolah menjadi lowercase dan membersihkan urls pada teks. Teks ini lalu ditokenisasi menggunakan TextVectorization.  |
| Arsitektur model | Arsitektur model yang digunakan yaitu, layer embeding pada layer awal yang akan memproses input string dengan bantuan TextVectorization, kemudian layer Embedding untuk mencari kemiripan kata pada setiap teks pada data, kemudian layer Bidirectional LSTM yang membantu model dalam memahami konteks teks pada kalimat, 2 hiden layer dan 1 output layer.  |
| Metrik evaluasi | Metric yang digunakan pada model yaitu BinaryAccuracy, TruePositive, FalsePositive, TrueNegative, FalseNegative untuk mengevaluasi performa model dalam menentukan klasifikasi |
| Performa model | Model yang dihasilkan memiliki performa yang cukup baik. Model memperoleh BinaryAccuracy sebesar 90,2%. Selain itu hasil dari conffusion metriks menunjukan nilai sebesar 2559 untuk true positif, 2475 untuk true negatif, 303 untuk false positif, 242 untuk false negatif. |
