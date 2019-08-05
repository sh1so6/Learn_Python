import asyncio
import sys


async def msec_five():
    print("{} start".format(sys._getframe().f_code.co_name))
    asyncio.sleep(0.5)
    print("{} end".format(sys._getframe().f_code.co_name))
    return True


async def msec_one():
    print("{} start".format(sys._getframe().f_code.co_name))
    asyncio.sleep(0.1)
    print("{} end".format(sys._getframe().f_code.co_name))
    return True


async def sec_dynamic(time: float):
    print("{} start".format(sys._getframe().f_code.co_name))
    asyncio.sleep(time)
    print("{} end".format(sys._getframe().f_code.co_name))
    return True


async def sleep_loop():
    for _ in range(5):
        pass


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete()


if __name__ == "__main__":
    main()
