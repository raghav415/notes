import asyncio


async def fetch_data():
    print('fetch started')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)   # increase time to see flow execution.


# async def main():
#     task = asyncio.create_task(print_numbers())
#     await fetch_data()    # this starts event loop execution
#
#     await task

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # to get value from coroutine we need to await it.
    a = await task1  # this starts event loop execution
    await task2

asyncio.run(main())
