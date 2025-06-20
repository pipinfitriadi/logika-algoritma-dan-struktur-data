from time import sleep

def countdown(i):
    print(i)

    if i <= 0:
        return
    else:
        sleep(0.5)
        countdown(i - 1)

countdown(5)
