# Pengelola Absen Kelas

**File:** `absen_kelas.py`

SMA "Harapan" ingin mengolah data absen siswa hari ini. Data awal sudah tersedia sebagai list:

```py
siswa   = ["Andi", "Budi", "Citra", "Dewi", "Eka"]
status  = ["H",    "I",    "H",     "A",     "H"]  
# H = Hadir, I = Izin, A = Alpha
```

**Tugas:**

1. Baca input satu baris: nama siswa (string).
2. Cari nama di list `siswa`.
3. Jika ditemukan, tampilkan status kehadirannya:
    ```
    Status Andi: Hadir
    ```
    (ubah kode "H"→"Hadir", "I"→"Izin", "A"→"Alpha")
4. Jika tidak ditemukan, cetak:
    ```
    Siswa X tidak terdaftar.
    ```

**Contoh:**

_Input:_

```
Citra
```

_Output:_

```
Status Citra: Hadir
```
