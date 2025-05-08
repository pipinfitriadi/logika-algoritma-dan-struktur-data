# Pengingat Stok Minimum

**File:** `stok_minimum.py`

Toko kelontong mencatat stok barang:

```py
items = ["Beras", "Gula", "Minyak", "Telur", "Tepung"]
stocks = [     10,     3,       5,      1,       8]
```

**Tugas:**

1. Baca integer `min_stok`.
2. Dari list, tampilkan semua barang dengan `stocks[i] ≤ min_stok`, satu per baris:
    ```
    Peringatan: Gula (3)
    ```
3. Jika tidak ada yang di bawah atau sama min, cetak:
    ```
    Semua stok mencukupi.
    ```

**Contoh:**

_Input:_

```
4
```

_Output:_

```
Peringatan: Gula (3)
Peringatan: Telur (1)
```
