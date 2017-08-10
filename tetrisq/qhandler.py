
# ------------------- #
# Third Party Imports #
# ------------------- #
from redis import Redis
from rq import Queue
import multiprocessing as mp
from types import *


class JobBlock:

    total_blocks = 0
    queued_blocks = 0
    waiting_blocks = 0

    def __init__(self, n_cpu, t_run, delta_t_run, q_name='default'):
        self.n_cpu = n_cpu
        self.time = t_run
        self.delta_time = delta_t_run
        self.state = 'waiting'
        self.func = None
        self.func_args = ''
        self.area = n_cpu*t_run
        self.total_blocks += 1
        self.queue = q_name
        self.job = None
        if self.n_cpu > mp.cpu_count():
            self.n_cpu = mp.cpu_count()

    def set_job(self, func, args):
        if type(func) == FunctionType:
            self.func = func
            self.args = args
        else:
            raise ValueError('for setjob(func, arg): func is not a function')


    def queue_up(self):
        if self.func is not None and self.job is None:
            que = Queue(connection = Redis)
            self.job = que.enqueue(self.func, self.args)
            self.queued_blocks += 1


class BlockBox:

    total_boxes = 0

    def __init__(self, block_list, boxid):
        self.blocks = block_list
        self.id = boxid

    def add_block(self, block):
        self.blocks.append(block)

    def remove_block(self, block):
        self.blocks.remove(block)

def queue_smart(j_box):
    pass
    #
    # Pseudo code begins here
    #

    # Step 1. Set a baseline
        # check the currently queued box(s) as a list to see how what blocks are queued
            # look through the blocks in current box(s) as a list
                # find number of free cpus
                # set time to next base-line (time when all cpus are free)
                # free cpus * time_to_bl = free area
    # check if in the next box, there are blocks whose area < free area and whose required_cpus are <= free_cpus
    # append those to a list - list comprehension here

    # Step 2. Use greedy placement of smallest blocks first - that way the most jobs can fit in the smallest amount of space
        # first check if time_to_bl = 0 (at base line)
        # see if there is any configuration of blocks that fill the entire unused cpu
        # else greedy place the blocks so that the most blocks are placed.
            # check if there is a block that is smaller than the free_area - prioritize this block

    # Step 3. Keep the the blocks to be queued in the box and push the ones that won't be queued to the next box

    # Step 4. enqueue the funcs in the blocks in the box when the current job has finished

    #
    # Pseudo code ends here
    #