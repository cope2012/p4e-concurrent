import threading
from time import sleep


def dummy():
    print('start doing things...')
    sleep(3)
    print('finish doing things...')


if __name__ == '__main__':
    t1 = threading.Thread(target=dummy)
    t1.start()
    # t1.setDaemon(True)
    # t1.join(timeout=99)
    print('continue with main program...')
    print('more things to do in main program...')
