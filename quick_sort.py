from time import process_time, sleep

def print_element(data):
    for item in data:
        print(item, end="")
    else:
        print()


def print_element_2(data):
    for item in data:
        sleep(1)
        print(item, end="")
    else:
        print()


start_time = process_time()
# print_element([2, 4, 6, 8, 10])
print_element([2])
elapsed_time = process_time() - start_time
print(f"Process time taken: {elapsed_time:.6f} seconds")

start_time = process_time()
# print_element_2([2, 4, 6, 8, 10])
print_element_2([2])
elapsed_time = process_time() - start_time
print(f"Process time taken: {elapsed_time:.6f} seconds")
