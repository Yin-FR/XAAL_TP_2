#!/usr/bin/env python3
# -*-coding: utf-8-*-


import aioesphomeapi
import asyncio
from esp.dev import MyRelay, MySensor
from xaal.lib import Device, Engine, tools, AsyncEngine, helpers
import logging

KEY_RELAY_0 = 3671421699             
KEY_RELAY_1 = 3671421696
KEY_SENSOR = 2281838442

realy_0 = MyRelay(key=3671421699, addr=tools.get_uuid("6a50b2f8-9edf-11ec-a664-acde48001122"), info="relay 0")  #set the key and uuid for new devices
realy_1 = MyRelay(key=3671421696, addr=tools.get_uuid("6128fd1e-9ed2-11ec-87f8-acde48001122"), info="relay 1")
sensor = MySensor(addr=tools.get_uuid("d0cee8b0-9edf-11ec-b0cd-acde48001122"))

logging.getLogger('aioesphomeapi').setLevel(logging.INFO)


async def task(devices): 
    cli = aioesphomeapi.APIClient("sonoff1", 6053, password="MyPassword")
    await cli.connect(login=True)

    def change_callback(state):         
        """Print the state changes of the device.."""
        print("{}: {}".format(state.key, state.state))
        if state.key == 2281838442:
            devices[0].attributes["sensor"] = state.state
        elif state.key == 3671421699:
            devices[1].attributes["pypower"] = state.state
        elif state.key == 3671421696:
            devices[2].attributes["power"] = state.state

    # Subscribe to the state changes
    await cli.subscribe_states(change_callback)

# last step, create an engine and register the new devices
helpers.setup_console_logger()
eng = AsyncEngine()
eng.add_devices([realy_0, realy_1, sensor])
eng.new_task(task([sensor, realy_0, realy_1]))

eng.run()
