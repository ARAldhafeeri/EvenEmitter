import asyncio
import timeit
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from events.emitter import EventEmitter
import tracemalloc

import httpx

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

    
async def benchmark_event_emitter(num_events):
    emitter = EventEmitter()

    # print bench mark start 
    print(f"Benchmarking {num_events}")

    async def listener(*args):
        """ asynchrounous api call"""
        res = await fetch_data("some-url")


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
    num_events = 1


    # Run the benchmark asynchronously
    asyncio.run(benchmark_event_emitter(num_events))
