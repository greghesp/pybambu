import asyncio

import logging

from pybambu.bambulab import BambuLab

logging.basicConfig(level=logging.DEBUG)


async def main():
    async with BambuLab("192.168.1.64") as ev:
        con = await ev.connect()
        print(con.__dict__)
        print("connected")

        def new_update(device):
            print(device.__dict__)

        asyncio.create_task(ev.subscribe(callback=new_update))
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
