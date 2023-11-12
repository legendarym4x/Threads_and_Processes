from time import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    total = []
    for num in numbers:
        result = []
        for i in range(1, num + 1):
            if num % i == 0:
                result.append(i)
        total.append(result)
    return total


def factorize_process(*numbers):
    pool = Pool(processes=cpu_count())
    results = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return results


if __name__ == "__main__":

    start = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(a, b, c, d, sep='\n')
    end = time()
    print(f'Time spent on synchronous work: {round((end - start), 5)} seconds')
    print('----------------------------------------------------')

    start_pr = time()
    a1, b1, c1, d1 = factorize_process(128, 255, 99999, 10651060)
    print(a1, b1, c1, d1, sep='\n')
    end_pr = time()
    print(f'Time spent on parallel operation of several cores: {round((end_pr - start_pr), 5)} seconds')
    print(f'The number of processor cores = {cpu_count()}')

