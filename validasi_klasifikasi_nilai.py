# validasi_klasifikasi_nilai.py

print("=== Program Validasi dan Klasifikasi Nilai Ujian ===")

# Penerimaan input dari pengguna
input_nilai = input("Masukkan nilai akhir (skor 0 - 100): ")

# Tahap 1: Validasi Data Terlebih Dahulu
try:
    # Mengonversi input ke tipe data float
    nilai = float(input_nilai)
    
    # Memeriksa apakah nilai berada dalam rentang valid (0 sampai 100)
    if nilai < 0 or nilai > 100:
        print("Error: Nilai tidak valid! Harap masukkan angka antara 0 hingga 100.")
    else:
        # Tahap 2: Rangkaian Seleksi if-elif-else untuk Klasifikasi
        if nilai >= 85:
            kategori = "A (Sangat Baik)"
        elif nilai >= 75:
            kategori = "B (Baik)"
        elif nilai >= 65:
            kategori = "C (Cukup)"
        elif nilai >= 50:
            kategori = "D (Kurang)"
        else:
            kategori = "E (Sangat Kurang / Tidak Lulus)"
            
        # Penampilan Output
        print("\n--- HASIL KLASIFIKASI ---")
        print(f"Nilai Angka : {nilai}")
        print(f"Kategori    : {kategori}")

except ValueError:
    # Menangani error jika input bukan berupa angka (misalnya huruf atau simbol)
    print("Error: Input tidak valid! Harap masukkan format angka yang benar.")