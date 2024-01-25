import asyncio
import timeit
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from EventEmitterPy.emitter import EventEmitter
import tracemalloc
import logging

logger = logging.getLogger(__name__)
#  log to a file 
logging.basicConfig(filename='benchmark.log', level=logging.DEBUG)
    
async def benchmark_event_emitter(num_events):
    emitter = EventEmitter()

    # print bench mark start 
    print(f"Benchmarking {num_events}")

    async def listener(*args):
        """ asynchrounous api call"""
        logger.info("listener called")


    # memory usage
    tracemalloc.start()
    for event in range(num_events):
        emitter.on(event, listener)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    start_time = timeit.default_timer()

    # Emit the events
    tasks = [emitter.emit(event, event) for event in range(num_events)]

    await asyncio.gather(*tasks)
    

    end_time = timeit.default_timer()

    total_time = end_time - start_time
    print(f"Emitted {num_events} in {total_time} seconds")

# Run the benchmark test with adjustable parameters
if __name__ == "__main__":
    num_events = 1000000


    # Run the benchmark asynchronously
    asyncio.run(benchmark_event_emitter(num_events))
