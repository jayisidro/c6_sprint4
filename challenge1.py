from time import sleep

def delay(seconds):
    print(f"Sleeping for {seconds} seconds(s)")
    sleep(seconds)

def main():
    print('0')
    delay(seconds=2)
    print('1')
    delay(seconds=2)
    print('2')
    delay(seconds=2)
    print('3')
    delay(seconds=2)
    print('4')
    delay(seconds=2)

if __name__ == "__main__":
    main()