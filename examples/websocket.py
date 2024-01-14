import asyncio
import sys, getopt
import logging

from pybambu import BambuClient

logging.basicConfig(level=logging.DEBUG)


def new_update(device):
    print(device.__dict__)


async def new_main(argv):
    opts, args = getopt.getopt(argv, "hd:i:a:s:", ["devicetype=", "host_ip=", "access_code=", "serial="])
    for opt, arg in opts:
        logging.debug(opt)
        if opt == '-h':
            print('websocket.py -d <device_type> -i <host_ip> -a <access_code> -s <serial>')
            sys.exit()
        elif opt in ("-d", "--devicetype"):
            device_type = arg
        elif opt in ("-i", "--host_ip"):
            host = arg
        elif opt in ("-a", "--access_code"):
            access_code = arg
        elif opt in ("-s", "--serial"):
            serial = arg

    bambu = BambuClient(device_type=device_type,
                        serial=serial,
                        host=host,
                        username="bblp",
                        access_code=access_code,
                        local_mqtt=True,
                        region=None,
                        email=None,
                        auth_token=None
                        )
    success = await bambu.try_connection()
    if success:
        print("Starting MQTT")

        def event_handler(event):
            device_instance = bambu.get_device()
            print('event:', device_instance, event)

        bambu.connect(callback=event_handler)
    else:
        print("Connection failed")


if __name__ == "__main__":
    asyncio.run(new_main(sys.argv[1:]))
