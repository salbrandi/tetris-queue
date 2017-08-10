import time
import random
import subprocess
import multiprocessing as mp

def simple_math(x):
    ilist = []
    for i in range(x*2):
        ilist.append(i-x)
    return ilist[x]



def get_time_used(func, *args):
    start_time = time.perf_counter()
    func( *args )
    return time.perf_counter()-start_time


def test_loader(rand_list=[], cpuse = True):
    machine_available_cores = mp.cpu_count()

    num_tests = 1

    if not rand_list:
        rand_list = [(random.randint(1, machine_available_cores), random.randint(1, 3) ) for _ in range(num_tests)]

    bash_commands = ['stress -c {0} -t {1}s'.format(i, n) for i, n in rand_list]


    if cpuse:
        tused = [get_time_used(lambda: subprocess.call(command, shell=True)) for command in bash_commands]

        total = 0
        for it in tused:
            print('time used ', it)
            total += it
        print('total time for entire queue ', total)
    else:
        return rand_list