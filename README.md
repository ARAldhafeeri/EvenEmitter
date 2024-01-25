# EvenEmitter
Python library for event driven programming built on top of asyncio.


## Overview

The `EventEmitter` class allows you to create and manage events and event handlers in an asynchronous environment. It provides a simple mechanism to emit events and notify registered handlers.


## benchmark
The  benchmark.py file contains a simple benchmarking script that compares the performance of the EventEmitter class to the built-in asyncio.Event class. The benchmarking script creates 1000 events and 1000 handlers for each event. It then emits all events and measures the time it takes to complete. The benchmarking script can be run with the following command:

```bash
$ python benchmark.py
```
results: 
1. 1 event 1 handler
```bash
    Benchmarking 1
    Current memory usage is 0.00052MB; Peak was 0.000592MB
    Emitted 1 in 0.4999799 seconds
```
The benchmark for 1 event and 1 handler shows memory usage of 0.00052MB and a time of 0.4999799 seconds. This means that the event emitter is using 0.00052MB of memory and it took 0.4999799 seconds to emit 1 event with 1 handler. Inside the handler asynchrouns  api  call made to simulate the real world scenario.

2. 1000 events 1 handler
```bash
    Benchmarking 1000
    Current memory usage is 0.183028MB; Peak was 0.1831MB
    Emitted 1000 in 8.076447499999999 seconds
```
The benchmark for 1000 events and 1 handler shows memory usage of 0.183028MB and a time of 8.076447499999999 seconds. This means that the event emitter is using 0.183028MB of memory and it took 8.076447499999999 seconds to emit 1000 events with 1 handler. Inside the handler asynchrouns  api  call made to simulate the real world scenario.

This means 
### Installation

```bash
pip install asyncio
```

### Example

```python
import asyncio
from collections import defaultdict

class EventEmitter:
    # ... (Your existing implementation)

# Example Usage
async def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

emitter = EventEmitter()
emitter.on('my_event', my_handler)
await emitter.emit('my_event', 1, 2, key='value') # Prints: Event 'my_event' received with arguments: (1, 2) and kwargs: {'key': 'value'}
```

## API Documentation

### `emit(event, *args, **kwargs)`

Emit an event and call all registered handlers.

- `event`: The name of the event.
- `args`: Additional positional arguments for the event handlers.
- `kwargs`: Additional keyword arguments for the event handlers.

### `on(event, handler)`

Register an event handler.

- `event`: The name of the event.
- `handler`: The function to be called when the event is emitted.

### `off(event, handler)`

Unregister an event handler.

- `event`: The name of the event.
- `handler`: The function to be unregistered.

### `removeAllListeners(event)`

Remove all listeners for the given event.

- `event`: The name of the event.

### `event_names()`

Return a list of all registered event names.

### `listener_count(event)`

Return the number of listeners for the given event.

- `event`: The name of the event.

### `once(event, handler)`

Register a handler that will be called at most once.

- `event`: The name of the event.
- `handler`: The function to be called once.

### `listeners(event)`

Return a list of all listeners for the given event.

- `event`: The name of the event.

### `rawListeners(event)`

Return a copy of the handlers for the given event.

- `event`: The name of the event.

### `prependListener(event, handler)`

Register a handler to be called before all others.

- `event`: The name of the event.
- `handler`: The function to be called first.

### `setMaxListeners(event, n)`

Set the maximum number of listeners for all events.

- `event`: The name of the event.
- `n`: The maximum number of listeners.

### `getMaxListeners(event)`

Return the maximum number of listeners for all events.

- `event`: The name of the event.

### `onAny(handler)`

Register a handler for all events.

- `handler`: The function to be called for all events.