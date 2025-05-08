# Penukaran Poin Hadiah

**File:** `tukar_poin.py`

Sebuah aplikasi belanja memberikan poin untuk setiap transaksi, lalu bisa ditukar dengan voucher belanja. Data awal:

```py
users   = ["Ani", "Beni", "Cici", "Dedi"]
points  = [ 1200,   850,    430,    1600]
# Satu voucher bernilai 1000 poin
```

**Tugas:**

1. Baca input satu baris: nama pengguna (string).
2. Cari nama di list `users`.
3. Jika ditemukan, hitung berapa banyak voucher (integer pembagian poin // 1000) dapat ditukar, lalu kurangi poin pengguna sesuai jumlah voucher, dan tampilkan:
    ```
    Halo Ani, Anda mendapat 1 voucher. Sisa poin = 200.
    ```
4. Jika poin < 1000, tampilkan:
    ```
    Maaf Beni, poin Anda belum cukup untuk ditukar.
    ```
5. Jika nama tidak terdaftar, tampilkan:
    ```
    Pengguna X tidak ditemukan.
    ```

**Contoh:**

_Input:_

```
Cici
```

_Output:_

```
Maaf Cici, poin Anda belum cukup untuk ditukar.
```
