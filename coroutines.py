"""
    Coroutines = funcs declared with async/await syntax (preferred way to write asyncio apps)
    There are three main types of awaitable objects: coroutines, Tasks, and Futures.
    Source: https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for
"""
import asyncio
import time


async def _say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return 33


async def _eternity():
    await asyncio.sleep(3600)
    print('yay!')


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


# This takes total of 3s to complete (executed sequentially)
async def main2():
    print(f"started at {time.strftime('%X')}")
    await _say_after(1, 'hello')
    await _say_after(2, 'people')
    print(f"finished at {time.strftime('%X')}")


# TASK: This takes total of 2s to complete (executed in parallel)
async def main3():
    task1 = asyncio.create_task(_say_after(1, 'hello'))
    task2 = asyncio.create_task(_say_after(2, 'Metal'))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


# FUTURE: This takes total of 2s to complete (executed in parallel)
async def main4():
    task1 = asyncio.create_task(_say_after(1, 'hello'))
    task2 = asyncio.create_task(_say_after(2, 'Voodoo'))
    all_tasks = [task1, task2]

    print(f"started at {time.strftime('%X')}")
    r1, r2 = await asyncio.gather(*all_tasks)
    print(f"finished at {time.strftime('%X')}, results {r1}, {r2}")


# TIMEOUT (seconds): cancels task and raises error (can be shielded -- read the docs)
async def main5():
    try:
        await asyncio.wait_for(_eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')


# RUNNING asyncio program
if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(main2())
    asyncio.run(main3())
    asyncio.run(main4(), debug=False)
    asyncio.run(main5())
