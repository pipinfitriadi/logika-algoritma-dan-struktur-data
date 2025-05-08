# Kalkulasi Total Belanja

**File:** `total_belanja.py`

Pembeli memasukkan dua baris:

* Baris pertama: list harga item (spasi)
* Baris kedua: list kuantitas masing-masing (panjang sama)

**Tugas:**

1. Hitung `total = sum(harga[i] * qty[i])`.
2. Jika `total ≥ 1_000_000`, cetak:
    ```
    Total sebelum diskon: {total}
    Diskon 10%: {diskon}
    Total bayar: {total_diskon}
    ```
3. Jika `total < 1_000_000`, cetak:
    ```
    Total bayar: {total}
    ```

**Contoh:**

_Input:_

```
200000 150000 300000
2 1 1
```

_Output:_

```
Total bayar: 850000
```
