# import threading
# from time import sleep
#
#
# def reverse_count(number, time = 1):
#     print(f'start count')
#     for i in reversed(range(number+1)):
#         print(i)
#         sleep(time)
#     print(f'count is done')
#
#
# t1 = threading.Thread(target = reverse_count, args=[5]).start()
# t2 = threading.Thread(target = reverse_count, args=[5]).start()
# t3 = threading.Thread(target = reverse_count, args=[5]).start()
# t4 = threading.Thread(target = reverse_count, args=[9]).start()
# t5 = threading.Thread(target = reverse_count, args=[3]).start()


import asyncio


async def reverse_count(number, time = 1):
    print(f'start count')
    for i in reversed(range(number+1)):
        print(i)
        await asyncio.sleep(time)
    print(f'count is done')

async def main():
    t1 = asyncio.create_task(reverse_count(5))
    t2 = asyncio.create_task(reverse_count(5))
    t3 = asyncio.create_task(reverse_count(5))

    await t1
    await t2
    await t3

asyncio.run(main())

