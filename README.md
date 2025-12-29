# 🧮 Analisis Kompleksitas Algoritma KPK (LCM)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Analysis-green?style=for-the-badge)

## 📌 Deskripsi Proyek
Aplikasi ini adalah **Kalkulator KPK (Kelipatan Persekutuan Terkecil)** yang dirancang untuk tujuan edukasi dan analisis performa algoritma. Aplikasi ini membandingkan dua pendekatan algoritma:
1.  **Iteratif (Brute Force Looping)**
2.  **Rekursif (Recursive Function)**

Tujuan utamanya bukan hanya mencari hasil KPK, melainkan **menganalisis kompleksitas waktu (Time Complexity)** dan membuktikan secara visual bahwa kedua algoritma tersebut memiliki karakteristik **Linear Time $O(n)$**.

## 👥 Tim Penyusun (Nasgor Goreng)
Proyek ini disusun untuk memenuhi Tugas Besar Analisis Kompleksitas Algoritma.
* **Abraham Shalom Nadeak** (NIM: 103022400008)
* **Nauvalky Kusfito Guci** (NIM: 103022400xxx)
* **Petrus Bramnonsas Agustino** (NIM: 103022400xxx)

---

## 🚀 Fitur Utama
* **Kalkulator KPK Dual-Mode**: Menghitung KPK menggunakan metode Iteratif dan Rekursif secara bersamaan.
* **Analisis Real-Time**: Menampilkan waktu eksekusi (ms), jumlah langkah (iterations), dan kedalaman rekursi (recursion depth).
* **Rumus T(n) Otomatis**: Menghitung total operasi dasar CPU berdasarkan input user.
* **Grafik Benchmark**: Memvisualisasikan pertumbuhan waktu eksekusi seiring bertambahnya input $N$ menggunakan `matplotlib`.
* **Crash Handling**: Menangani *Stack Overflow* pada input besar dengan `try-except` block.

---

## 🧠 Analisis Algoritma

Berdasarkan pengujian dan analisis kode, berikut adalah perbandingan kompleksitas kedua algoritma:

### 1. Iteratif (Looping)
Menggunakan pendekatan `while(True)` yang akan terus berjalan hingga kelipatan ditemukan.
* **Persamaan Waktu:** $T(n) = 8k + 4$
* **Kompleksitas:** $O(n)$
* **Karakteristik:** Lebih hemat memori ($O(1)$ Space Complexity).

### 2. Rekursif (Fungsi)
Menggunakan fungsi yang memanggil dirinya sendiri (`self-calling`) dengan parameter yang diperbarui.
* **Persamaan Waktu:** $T(n) = 11k - 1$
* **Kompleksitas:** $O(n)$
* **Karakteristik:** Memiliki *overhead* waktu lebih tinggi karena alokasi stack frame, dan rentan terhadap *Stack Overflow* pada input > 15.000 (Space Complexity $O(n)$).

> **Catatan:** $k$ adalah jumlah langkah atau solusi relatif terhadap input terbesar.

---

## 📸 Screenshots

*(Simpan screenshot aplikasimu di folder proyek, lalu ganti nama file di bawah ini)*

| Dashboard Utama | Grafik Analisis |
| :---: | :---: |
| ![Dashboard](screenshot_dashboard.png) | ![Grafik](screenshot_graph.png) |

---

## 🛠️ Instalasi & Cara Menjalankan

Pastikan kamu sudah menginstall Python.

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/username-kamu/analisis-kpk-streamlt.git](https://github.com/username-kamu/analisis-kpk-streamlt.git)
    cd analisis-kpk-streamlit
    ```

2.  **Install Library**
    Gunakan `pip` untuk menginstall dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Aplikasi**
    ```bash
    streamlit run main.py
    ```

---

## 📦 Tech Stack
* **Language:** Python 3.10+
* **Frontend Framework:** Streamlit
* **Data Visualization:** Matplotlib
* **Data Processing:** Pandas

---
*Dibuat dengan ❤️ dan ☕ oleh Tim Nasgor Goreng*
