import streamlit as st
import pandas as pd
import time
import sys
import matplotlib.pyplot as plt

recursiveLimit = 20000

sys.setrecursionlimit(recursiveLimit)
def kpk_iteratif(a,b):
    step = 0
    kelipatan = 0
    counter = 0
    
    #Cari Nilai max dulu dan dimasukkna ke step
    if a > b:
        step = a
    else:
        step = b
        
    #Memberi nilai kelipatan dengan nilai max dari a dan b
    kelipatan = step
    
    #Iteratif mencari KPK
    while (True):
        counter += 1
        if(kelipatan % a == 0 and kelipatan % b == 0):
            return kelipatan, counter
        else:
            kelipatan += step
            
def kpk_rekursif(a,b,kelipatan=None, depth=1):
    step = 0
    
    #Cari Nilai max dulu dan dimasukkna ke step
    if a > b:
        step = a
    else:
        step = b
        
    #Memberi nilai kelipatan dengan nilai max dari a dan b saat nilai kelipatan None
    if kelipatan is None:
        kelipatan = step
    
    #Rekursif mencari KPK
    if(kelipatan % a == 0 and kelipatan % b == 0):
        return kelipatan, depth
    else:
        return kpk_rekursif(a,b, kelipatan + step, depth+1)
 
    

st.set_page_config(
    page_title="Analisis Algoritma KPK",
    page_icon="🧮",
    layout="centered"
)

st.markdown("<h1 style='text-align: center; color: #4F8BF9;'>🧮 Analisis Kompleksitas Waktu dan Algoritma Mengenai Kelipatan Persekutuan Terkecil (KPK)</h1>", unsafe_allow_html=True)
st.header("\nKelompok : Nasgor Goreng")

data_kelompok = {
    "NamaMahasiswa": ["Abraham Shalom Nadeak", "Nauvalky Kusfito Guci", "Petrus Brammonsas Agustino"],
    "NIM": ["103022400008", "103022400014", "103022400079"]
}

df_kelompok = pd.DataFrame(data_kelompok)

st.subheader("Data Anggota Kelompok")
st.dataframe(df_kelompok)

st.header("\nDefenisi KPK")
st.latex(r"KPK(a, b) = \frac{a \times b}{FPB(a, b)}")

st.subheader("\nTujuan Aplikasi")
st.write("\n\nTujuan utama landing page ini dibuat adalah untuk mencari waktu eksekusi algoritma KPK beserta kelas kompleksitasnya.")

st.write("---")
st.markdown("<h1 style='text-align: center; color: #4F8BF9;'>🧮 Kalkulator KPK & Analisis Waktu</h1>", unsafe_allow_html=True)
st.write("Membandingkan performa algoritma **Iteratif** (Looping) vs **Rekursif** (Fungsi).")
st.write(f"Note : rekursif data maksimal {recursiveLimit}")

col_input1, col_input2 = st.columns(2)

with col_input1:
    st.markdown("### Input Angka Pertama (a)")
    num_a = st.number_input("Masukkan nilai A:", min_value=1, value=12, step=1)
    
with col_input2:
    st.markdown("### Input Angka Kedua (b)")
    num_b = st.number_input("Masukkan nilai B:", min_value=1, value=15, step=1)
    
btn = st.button("Hitung KPK & Analisis Waktu")

if btn:
    
    with st.spinner("Sedang menghitung...Sabar ya, CPU lagi berusaha dengan maksimal 😅"):
        
        start_iter = time.perf_counter()
        hasil_iter, count_iter = kpk_iteratif(num_a, num_b)
        end_iter = time.perf_counter()
        waktu_iter = (end_iter - start_iter) * 1000
        
        start_rek = time.perf_counter()
        
        try:
            hasil_rek, count_rek = kpk_rekursif(num_a, num_b)
            end_rek = time.perf_counter()
            waktu_rek = (end_rek - start_rek) * 1000
            status_rek = "Success"
        except RecursionError:
            hasil_rek = "Error: Recursion Depth Exceeded"
            waktu_rek = float('inf')
            status_rek = "Stack Overflow"
            
        st.success(f"Perhitungan Selesai! KPK dari {num_a} dan {num_b} adalah {hasil_iter}.")
        
        st.write("---")
        st.subheader("⌚ Hasil Analisis Waktu")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.metric(label="Iteratif (Loop)", value=f"{waktu_iter:.5f} ms")
            st.metric(label="Jumlah Iterasi", value=count_iter)        
            if(waktu_iter < waktu_rek):
                st.caption("Iter lebih cepat dari pada Rekursif")
        
        with col_res2:
           if status_rek == "Stack Overflow":
               st.error("gagal! Limit rekursi terlampaui")
           else:
                st.metric(label="Rekursif (Fungsi)", value=f"{waktu_rek:.5f} ms")
                st.metric(label="Jumlah Iterasi", value=count_rek)
                if(waktu_rek < waktu_iter):
                    st.caption("Rekursif lebih cepat dari pada Iteratif")
                else:
                    st.caption(f"Lebih lambat {waktu_rek - waktu_iter:.5f} ms dari Iteratif")

        st.write("---")
        st.subheader("🧮 Analisis Persamaan Waktu T(n)")
        st.write("Perhitungan jumlah operasi dasar CPU (Assign, Compare, Arithmetic) berdasarkan rumus yang diturunkan.")
        
        k = count_iter
        tn_iteratif = (8*k) + 4
        
        col_tn1,col_tn2 = st.columns(2)
        
        with col_tn1:
            st.markdown("### 🔵 Iteratif (Loop)")
            st.metric("Waktu Real", f"{waktu_iter} ms")
            st.markdown(f"**Total Operasi CPU:**")
            st.markdown(f"### {tn_iteratif} instruksi")
            st.caption("Kompleksitas: **Linear O(n)**")
        
        with col_tn2:
            st.markdown("### 🔴 Rekursif (Fungsi)")
            
            if status_rek == "Stack Overflow":
                st.error("Gagal menghitung T(n)")
                st.caption("Karena proses crash, total operasi tidak valid.")
            else:
                tn_rekursif = (11 * count_rek) - 1
                
                st.metric("Waktu Real", f"{waktu_rek:.5f} ms")
                
                st.markdown(f"**Total Operasi CPU:**")
                st.markdown(f"### {tn_rekursif} instruksi")
                
                # Insight Perbedaan
                selisih = tn_rekursif - tn_iteratif
                st.caption(f"⚠️ Rekursif melakukan **{selisih} operasi lebih banyak** (Overhead).")
                st.caption("Kompleksitas: **Linear O(n)**")

st.write("---")
st.header("📈 Grafik Benchmark (Uji Stress)")
st.write("Simulasi pertumbuhan waktu dengan menaikkan input B secara bertahap.")

range_n = st.slider("Tentukan Range :", min_value=1, max_value=1000, value=100, step=10)

if st.button("Generate Grafik"):
    
    inputs = []
    times_iter = []
    times_rek = []
    
    progress_bar = st.progress(0)
    
    fixed_a = num_a
    
    with st.spinner(f"Sedang menguji dengan A={fixed_a} dengan B= 1/sd{range_n}...Sabar ya, CPU lagi berusaha dengan maksimal 😅"):
        for i in range(1, range_n + 1):
            inputs.append(i)
        
            if i % 5 == 0:
                progress_bar.progress(int((i / range_n) * 100))
          
            start_iter = time.perf_counter()
            kpk_iteratif(fixed_a, i)
            end_iter = time.perf_counter()
            waktu_iter = (end_iter - start_iter) * 1000
            times_iter.append(waktu_iter)
            
            start_rek = time.perf_counter()
            try:
                kpk_rekursif(fixed_a, i)
                end_rek = time.perf_counter()
                waktu_rek = (end_rek - start_rek) * 1000
                times_rek.append(waktu_rek)
            except RecursionError:
                times_rek.append(None)
            
    progress_bar.empty()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(inputs, times_iter, label='Iteratif', color="Blue")

    clean_inputs = [x for x,y in zip(inputs, times_rek) if y is not None]
    clean_times = [y for y in times_rek if y is not None]
    
    ax.plot(clean_inputs, clean_times, label='Rekursif', color="Red", linestyle="--")
    
    ax.set_title(f"Benchmark: A={fixed_a} Konstan, B Berubah (1-{range_n})")
    ax.set_xlabel("B")
    ax.set_ylabel("Waktu Eksekusi (ms)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)
    st.info("💡 **Analisis:** Grafik linear menanjak membuktikan kompleksitas O(n).")
    
st.write("---")
st.header(" Source Code")

st.subheader("\nAlgoritma KPK Iteratif")
itr_kpk_code = """def kpk_iteratif(a,b):
    step = 0
    kelipatan = 0
    
    #Cari Nilai max dulu dan dimasukkna ke step
    if a > b:
        step = a
    else:
        step = b
        
    kelipatan = step
    
    #Iteratif mencari KPK
    while (True):
        if(kelipatan % a == 0 and kelipatan % b == 0):
            return kelipatan
        else:
            kelipatan += step"""
            
st.code(itr_kpk_code, language='python')

st.subheader("\nAlgoritma KPK Rekursif")
rek_kpk_code = """def kpk_rekursif(a,b,kelipatan=None):
    step = 0
    
    #Cari Nilai max dulu dan dimasukkna ke step
    if a > b:
        step = a
    else:
        step = b
        
    #Memberi nilai kelipatan dengan nilai max dari a dan b 
    #saat nilai kelipatan None
    if kelipatan is None:
        kelipatan = step
    
    #Rekursif mencari KPK
    if(kelipatan % a == 0 and kelipatan % b == 0):
        return kelipatan
    else:
        return kpk_rekursif(a,b, kelipatan + step)"""
        
st.code(rek_kpk_code, language='python')

        
            
        
        

        
