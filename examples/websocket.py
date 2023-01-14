import asyncio

import logging

from pybambu import BambuClient

logging.basicConfig(level=logging.DEBUG)


def new_update(device):
    print(device.__dict__)


async def new_main():
    client = BambuClient("192.168.1.64")
    serial = await client.try_connection()
    client.connect(callback=new_update)
    client.subscribe(serial)
    await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(new_main())
