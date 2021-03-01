from time import sleep
import random

def delay(seconds):
    print(f"Sleeping for {seconds} seconds(s)")
    sleep(seconds)

for n in range(0,5):
    print(n)
    delay(seconds=r.randint(1,5))


if __name__ == "__main__":
    main()