import sys
import random
import time
from stack import Stack
from queue122 import Queue
from deque import Deque


print("Using time.perf_counter for timing.")
REZ = time.get_clock_info('perf_counter').resolution
print('Smallest unit of time is ' + str(REZ) + ' seconds')


def time_push(initial_size, n_trials, obj, do_push, operation, name, operation_name):
    """ Finds average time for pushing onto a stack of a given initial size"""

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        do_push(obj, random.randint(0, 127))

    # time some pushes
    start_time = time.perf_counter()
    for i in range(n_trials):
        operation(obj, 0)
    end_time = time.perf_counter()
    time_per_operation = (end_time - start_time)/n_trials

    template = "Initial " + name  + " size = {:,d} -> avg. time/" + operation_name + " for {:,d} " + operation_name +" is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))


push = lambda ref, item : ref.push(item)
pop = lambda ref, item: ref.pop()
enqueue = lambda ref, item: ref.enqueue(item)
dequeue = lambda ref, item: ref.dequeue()

def time_stack_push(size, n_trials):
    stack = Stack()
    time_push(size, n_trials, stack, push, push, "Stack", "push")

def time_stack_pop(size, n_trials):
    stack = Stack()
    time_push(size, n_trials, stack, push, pop, "Stack", "pop")

def time_queue_enqueue(size, n_trials):
    queue = Queue()
    time_push(size, n_trials, queue, enqueue, enqueue, "Queue", "enqueue")

def time_queue_dequeue(size, n_trials):
    queue = Queue()
    time_push(size, n_trials, queue, enqueue, dequeue, "Queue", "dequeue")


def run_tests():
    """ Runs as many or as few tests as you call,
    initially just runs the test for stack pushes
    """
    print('\n' *3)
    n_trials = 100  # run this many trials and take the average time
    trials = [time_stack_push, time_stack_pop, time_queue_enqueue, time_queue_dequeue]

    for size in [1000000, 10000000]:
        for trial in trials:
            trial(size, n_trials)

run_tests()
