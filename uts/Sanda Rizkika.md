# Pengecek Kelayakan Karyawan

**File:** `kelayakan_karyawan.py`

Sebuah perusahaan menilai karyawan berdasarkan jumlah proyek selesai dan rata-rata jam kerja per minggu. Data awal:

```py
names       = ["Arif", "Bella", "Chandra", "Dina"]
projects    = [    5,      8,         3,       10]
avg_hours   = [   35,     42,        30,       45]
```

Karyawan dianggap **berprestasi** jika telah menyelesaikan ≥ 5 proyek **dan** rata-rata jam kerja ≥ 40.

**Tugas:**

1. Baca nama karyawan (string).
2. Jika terdaftar, periksa kriteria:
    * Bila kedua syarat terpenuhi, cetak:
        ```
        X berprestasi!
        ```
    * Bila proyek cukup tapi jam kerja kurang, cetak:
        ```
        X perlu meningkatkan jam kerja.
        ```
    * Bila jam cukup tapi proyek kurang, cetak:
        ```
        X perlu menyelesaikan lebih banyak proyek.
        ```
    * Bila keduanya kurang, cetak:
        ```
        X perlu meningkatkan proyek dan jam kerja.
        ```
3. Jika nama tidak ada, cetak:
    ```
    Karyawan X tidak terdaftar.
    ```

**Contoh:**

_Input:_

```
Bella
```

_Output:_

```
Bella berprestasi!
```
