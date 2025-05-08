# Konversi Suhu Harian

**File:** `konversi_suhu.py`

Cuaca hari ini tercatat dalam list suhu Celsius setiap jam di stasiun:

```py
suhu_c = [24, 26, 29, 31, 30, 28, 25]
```

**Tugas:**

1. Baca satu integer `n` yang menyatakan jam saat ini: Jam ke-n (0–6).
2. Konversi `suhu_c[n]` ke Fahrenheit:
    ```
    F = C * 9/5 + 32
    ```
3. Cetak:
    ```
    Jam n: C°C = F°F
    ```
4. Jika `n` di luar 0–6, cetak:
    ```
    Jam n tidak valid.
    ```

**Contoh:**

_Input:_

```
3
```

_Output:_

```
Jam 3: 31°C = 87.8°F
```
