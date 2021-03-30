from concurrent.futures import ThreadPoolExecutor
import threading

def action(a):
    with open('D:/python1.txt', 'a+t')as a:
        a.write(f'11111{threading.current_thread()}\n')
        print(f'{threading.current_thread()}')


def main():
    pool = ThreadPoolExecutor(max_workers=5)
    for i in range(10000):
        pool.submit(action, (i,))


if __name__ == '__main__':
    main()

