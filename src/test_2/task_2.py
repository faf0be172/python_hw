import random
from multiprocessing import Process, Pipe
from typing import List


def process_quicksort(sorting_list: List, algo_conn):
    if len(sorting_list) < 2:
        algo_conn.send(sorting_list)
        algo_conn.close()
        return

    intermediate_elm = sorting_list.pop(random.randint(0, len(sorting_list) - 1))

    local_conn_left, algo_conn_left = Pipe()
    left_process = Process(target=process_quicksort, args=([x for x in sorting_list if x < intermediate_elm], algo_conn_left))
    left_process.start()

    local_conn_right, algo_conn_right = Pipe()
    right_process = Process(target=process_quicksort, args=([x for x in sorting_list if x >= intermediate_elm], algo_conn_right))
    right_process.start()

    sorted_list = local_conn_left.recv()
    sorted_list += [intermediate_elm]
    sorted_list += local_conn_right.recv()

    algo_conn.send(sorted_list)
    algo_conn.close()

    left_process.join()
    right_process.join()


def quicksort(numbers: List):
    local_conn, algo_conn = Pipe()
    process = Process(target=process_quicksort, args=(numbers, algo_conn))

    process.start()
    numbers = local_conn.recv()
    process.join()

    return numbers
