def binary_search(list, item):
  result = None
  percobaan = 0
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]

    percobaan += 1
    print(f'{percobaan = } | {item = } | {guess = }')

    if guess == item:
      result = mid
      break
    elif guess > item:
      high = mid - 1
    else:
      low = mid + 1

  return result

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
