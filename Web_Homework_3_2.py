from time import time
import concurrent.futures
from multiprocessing import cpu_count


def factorize_norm(*number):
    start_time = time()
    result_list = []
    for i in range(len(number)):
        buff_list = []
        for j in range(1, number[i] + 1):
            if number[i] % j == 0:
                buff_list.append(j)
        result_list.append(buff_list.copy())
    print(f"Time of working: {time()-start_time}")
    return (
        result_list[0],
        result_list[1],
        result_list[2],
        result_list[3],
        result_list[4],
        result_list[5],
    )


def factorize_multy(*number):
    result_list = []
    for i in range(len(number)):
        buff_list = []
        for j in range(1, number[i] + 1):
            if number[i] % j == 0:
                buff_list.append(j)
        result_list.append(buff_list.copy())
    return result_list[0]


a1, b1, c1, d1, e1, f1 = 128, 255, 99999, 10651060, 19294988, 54347388


if __name__ == "__main__":
    a, b, c, d, e, f = factorize_norm(128, 255, 99999, 10651060, 19294988, 54347388)
    start_time = time()
    with concurrent.futures.ProcessPoolExecutor(2) as executor:
        executor.map(factorize_multy, (a1, b1, c1, d1, e1, f1))
    print(f"Time of working multiprocessing: {time()-start_time}")
