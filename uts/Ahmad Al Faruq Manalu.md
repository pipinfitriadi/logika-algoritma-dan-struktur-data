# Restok Snack Kantin

**File:** `restok_snack.py`

Sekolah "Ceria" menjual tiga jenis snack dengan data:

```py
names  = ["Keripik", "Biskuit", "Cokok"]
prices = [  5000,     7000,    10000]
stocks = [   20,       15,       10]
```

**Tugas:**

1. Baca satu baris input: nama snack dan jumlah beli (dipisah spasi).
2. Cari snack di `names`.
3. Jika ada dan stok ≥ beli, kurangi stok dan cetak:
    ```
    Terjual {jumlah_beli} {nama_snack}. Sisa stok = {sisa}.
    ```
4. Jika ada tapi stok < beli, cetak:
    ```
    Stok {nama_snack} hanya {stok_awal}.
    ```
5. Jika nama snack tidak ada, cetak:
    ```
    Snack {nama_snack} tidak tersedia.
    ```

**Contoh:**

_Input:_

```
Biskuit 5
```

_Output:_

```
Terjual 5 Biskuit. Sisa stok = 10.
```
