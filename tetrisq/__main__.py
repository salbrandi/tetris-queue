#!/usr/bin/env python

# ------------------- #
# Third Party Imports #
# ------------------- #

from redis import Redis
from rq import Queue
import multiprocessing as mp
import time


# ------------------- #
#    Local Imports    #
# ------------------- #
from cpustresser import simple_math, get_time_used, test_loader


print(mp.cpu_count())

redis_conn = Redis()



num_tests = 5
q = Queue(connection=redis_conn)

for num in range(num_tests):
    job = q.enqueue(get_time_used, test_loader)







