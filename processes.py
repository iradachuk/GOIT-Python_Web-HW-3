from time import time, sleep
from multiprocessing import Pool, cpu_count


def factorize(*number):
    result = []
    for num in number:
        res_num = []
        for i in range(1, num + 1):
            if num % i:
                continue
            else:
                res_num.append(i)
        result.append(res_num)
    return result

    # a, b, c, d = factorize(128, 255, 99999, 10651060)

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
    #              380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
if __name__ == '__main__':
    timer = time()
    print('Start of simple calc')
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f'Results: \n a = {a}, \n b = {b}, \n c = {c} \n d = {d}')
    print(f'Calculate time = {time() - timer}')

    sleep(2)

    timer = time()
    print('Start of multiprocessing calc')

    with Pool(cpu_count()) as executor:
        a, b, c, d = executor.map(factorize, (128, 255, 99999, 10651060))

    print(f'Results: \n a = {a}, \n b = {b}, \n c = {c} \n d = {d}')
    print(f'Multiprocessing calculate time = {time() - timer}')
