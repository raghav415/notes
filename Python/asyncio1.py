import asyncio


async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    # await foo('text') # This executes foo() synchronously waits for it to complete.
    # await task    # This executes foo() synchronously waits for it to complete.
    # await asyncio.sleep(2)  # If commented foo() executes at the end of main() execution.
    print('finished')


async def foo(text):
    print(text)
    await asyncio.sleep(1)  # this sends control back to main() if await was not called on foo()


asyncio.run(main())
