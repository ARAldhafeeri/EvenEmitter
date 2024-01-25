import asyncio
import unittest
from EventEmitterPy.emitter import EventEmitter

class TestEventEmitterAsyncio(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.emitter = EventEmitter()
        self.result = []

    # after each test call remove all listeners for test_event
    async def asyncTearDown(self):
        self.emitter.removeAllListeners("test_event")
        self.result = []
    
    async def test_emit(self):

        async def handler():
            self.result.append("Handler called")

        self.emitter.on("test_event", handler)
        await self.emitter.emit("test_event")
        self.assertEqual(self.result, ["Handler called"])

    async def test_off(self):

        async def handler():
            self.result.append("Handler called")

        self.emitter.on("test_event", handler)
        self.emitter.off("test_event", handler)
        await self.emitter.emit("test_event")
        self.assertEqual(self.result, [])

    async def test_removeAllListeners(self):

        async def handler():
            self.result.append("Handler called")

        self.emitter.on("test_event", handler)
        self.emitter.removeAllListeners("test_event")
        await self.emitter.emit("test_event")
        self.assertEqual(self.result, [])

    async def test_event_names(self):

        async def handler():
            self.result.append("Handler called")

        self.emitter.on("test_event", handler)
        self.assertEqual(self.emitter.event_names(), ["test_event"])

    async def test_listener_count(self):

        async def handler():
            self.result.append("Handler called")

        self.emitter.on("test_event", handler)
        self.assertEqual(self.emitter.listener_count("test_event"), 1)

    async def test_once(self):

        async def handler():
            self.result.append("Handler called")

        self.emitter.once("test_event", handler)
        await self.emitter.emit("test_event")
        await self.emitter.emit("test_event")
        self.assertEqual(self.result, ["Handler called"])

    async def test_emit_with_args(self):

        async def handler(*args):
            self.result.extend(args)

        self.emitter.on("test_event", handler)
        await self.emitter.emit("test_event", 1, 2, 3)
        self.assertEqual(self.result, [1, 2, 3])

    async def test_emit_with_kwargs(self):

        async def handler(**kwargs):
            self.result.append(kwargs)

        self.emitter.on("test_event", handler)
        await self.emitter.emit("test_event", foo="bar")
        self.assertEqual(self.result, [{"foo": "bar"}])


    async def test_emit_with_args_and_kwargs(self):

        async def handler(*args, **kwargs):
            self.result.append(args)
            self.result.append(kwargs)

        self.emitter.on("test_event", handler)
        await self.emitter.emit("test_event", 1, 2, 3, foo="bar")
        self.assertEqual(self.result, [(1, 2, 3), {"foo": "bar"}])

    async def test_emit_with_any(self):

        async def handler(event, *args, **kwargs):
            self.result.append(event)
            self.result.extend(args)
            self.result.append(kwargs)

        self.emitter.on("*", handler)
        await self.emitter.emit("test_event", 1, 2, 3, foo="bar")
        self.assertEqual(self.result, ["test_event", 1, 2, 3, {"foo": "bar"}])

    async def test_emit_with_any_and_args(self):
        async def handler(event, *args, **kwargs):
            self.result.append(event)
            self.result.extend(args)
            self.result.append(kwargs)

        self.emitter.on("*", handler)
        await self.emitter.emit("test_event", 1, 2, 3, foo="bar")
        self.assertEqual(self.result, ["test_event", 1, 2, 3, {"foo": "bar"}])

    async def test_emit_with_any_and_kwargs(self):

        async def handler(event, *args, **kwargs):
            self.result.append(event)
            self.result.extend(args)
            self.result.append(kwargs)

        self.emitter.on("*", handler)
        await self.emitter.emit("test_event", 1, 2, 3, foo="bar")
        self.assertEqual(self.result, ["test_event", 1, 2, 3, {"foo": "bar"}])

    async def test_emit_with_any_and_args_and_kwargs(self):

        async def handler(event, *args, **kwargs):
            self.result.append(event)
            self.result.extend(args)
            self.result.append(kwargs)

        self.emitter.on("*", handler)
        await self.emitter.emit("test_event", 1, 2, 3, foo="bar")
        self.assertEqual(self.result, ["test_event", 1, 2, 3, {"foo": "bar"}])

    async def test_emit_with_multiple_handlers(self):
 
        async def handler1():
            self.result.append("Handler 1 called")

        async def handler2():
            self.result.append("Handler 2 called")

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        await self.emitter.emit("test_event")
        self.assertEqual(self.result, ["Handler 1 called", "Handler 2 called"])

    async def test_emit_with_multiple_handlers_and_args(self):

        async def handler1(*args):
            self.result.extend(args)

        async def handler2(*args):
            self.result.extend(args)

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        await self.emitter.emit("test_event", 1, 2, 3)
        self.assertEqual(self.result, [1, 2, 3, 1, 2, 3])

    async def test_emit_with_multiple_handlers_and_kwargs(self):
            
        async def handler1(**kwargs):
            self.result.append(kwargs)

        async def handler2(**kwargs):
            self.result.append(kwargs)

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        await self.emitter.emit("test_event", foo="bar")
        self.assertEqual(self.result, [{"foo": "bar"}, {"foo": "bar"}])


    async def test_emit_with_multiple_handlers_and_args_and_kwargs(self):

        async def handler1(*args, **kwargs):
            self.result.append(args)
            self.result.append(kwargs)

        async def handler2(*args, **kwargs):
            self.result.append(args)
            self.result.append(kwargs)

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        await self.emitter.emit("test_event", 1, 2, 3, foo="bar")
        self.assertEqual(self.result, [(1, 2, 3), {"foo": "bar"}, (1, 2, 3), {"foo": "bar"}])


    async def test_emit_with_multiple_handlers_and_any(self):

        async def handler1(event, *args, **kwargs):
            self.result.append(event)
            self.result.extend(args)
            self.result.append(kwargs)

        async def handler2(event, *args, **kwargs):
            self.result.append(event)
            self.result.extend(args)
            self.result.append(kwargs)

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        await self.emitter.emit("test_event", 1, 2, 3, foo="bar")
        self.assertEqual(self.result, [ 1, 2, 3, {"foo": "bar"}, 1, 2, 3, {"foo": "bar"}])

    async def test_off_with_multiple_handlers(self):

        async def handler1():
            self.result.append("Handler 1 called")

        async def handler2():
            self.result.append("Handler 2 called")

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        self.emitter.off("test_event", handler1)
        self.emitter.off("test_event", handler2)
        await self.emitter.emit("test_event")
        self.assertEqual(self.result, []) 

    def test_listeners(self):

        async def handler1():
            self.result.append("Handler 1 called")

        async def handler2():
            self.result.append("Handler 2 called")

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        self.assertEqual(self.emitter.listeners("test_event"), [handler1, handler2])
        
    def test_rawListeners(self):

        async def handler1():
            self.result.append("Handler 1 called")

        async def handler2():
            self.result.append("Handler 2 called")

        self.emitter.on("test_event", handler1)
        self.emitter.on("test_event", handler2)
        self.assertEqual(self.emitter.rawListeners("test_event"), [handler1, handler2])

    async def test_setMaxListeners(self):

        async def handler(name):
            self.result.append(f"Handler called {name}")

        try: 
            self.emitter.setMaxListeners("test_event", 1)
            self.emitter.on("test_event", handler)
            self.emitter.on("test_event", handler)
        except Exception as e:
            self.assertEqual(str(e), "Max listeners reached")

    async def test_onAny(self):

        async def handler(event):
            self.result.append(event)

        self.emitter.onAny(handler)
        await self.emitter.emit("test_event")
        self.assertEqual(self.result, ["test_event"])

    async def test_default_max_listeners(self):
                                            
        async def handler():
            self.result.append("Handler called")

        self.emitter.on("test_event", handler)

        max_listeners = self.emitter.getMaxListeners("test_event")

        self.assertEqual(max_listeners, 10)

        self.emitter.setMaxListeners("test_event", 20)

        max_listeners = self.emitter.getMaxListeners("test_event")
        self.assertEqual(max_listeners, 20)
        

if __name__ == "__main__":
    unittest.main()