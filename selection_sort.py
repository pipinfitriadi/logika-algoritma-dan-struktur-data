def find_smallest(data: list[tuple[str, int]]) -> int:
    smallest_index = 0
    smallest = data[smallest_index]

    for i in range(1, len(data)):
        if data[i][1] > smallest[1]:
            smallest_index = i
            smallest = data[smallest_index]

    return smallest_index

def selection_sort(data: list) -> list:
    new_data = []

    for _ in range(len(data)):
        smallest = find_smallest(data)
        new_data.append(data.pop(smallest))

    return new_data


for musician, play_count in selection_sort(
    [
        ("RADIOHEAD", 156),
        ("KISHORE KUMAR", 141),
        ("THE BLACK KEYS", 35),
        ("NEUTRAL MILK HOTEL", 94),
        ("BECK", 88),
        ("THE STROKES", 61),
        ("WILCO", 111)
    ]
):
    print(f"{musician}: {play_count}")
