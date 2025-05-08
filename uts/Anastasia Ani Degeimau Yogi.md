# Kalkulator Diskon

**File:** `kalkulator_diskon.py`

Toko "DigiMart" memiliki data:

```py
categories = ["Elektronik", "Pakaian", "Buku", "Mainan"]
prices     = [500000,      150000,     80000,   120000]
discounts  = [      10,          20,        5,        15]
```

**Tugas:**

1. Baca satu baris input: nama kategori.
2. Jika kategori valid, tampilkan:
    ```
    Harga normal: {harga}
    Diskon: {diskon}%
    Harga bayar: {harga_diskon}
    ```
3. Jika tidak valid, cetak:
    ```
    Kategori {kategori} tidak valid.
    ```

**Contoh:**

_Input:_

```
Pakaian
```

_Output:_

```
Harga normal: 150000
Diskon: 20%
Harga bayar: 120000
```
