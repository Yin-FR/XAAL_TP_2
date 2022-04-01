#!/usr/bin/env python3
# -*-coding: utf-8-*-
import aioesphomeapi
from xaal.lib import Device


class MyRelay(Device):               #create new relay device and new function
    def __init__(self, key, info, addr=None):
        super().__init__(dev_type="powerrelay.basic", addr=addr)
        self.new_attribute("power", False)
        self.product_id = "relay yin"
        self.info = info
        self.add_method("turn_on", self.turn_on)
        self.add_method("turn_off", self.turn_off)
        self.key = key

    async def turn_on(self):
        cli = aioesphomeapi.APIClient("sonoff1", 6053, password="MyPassword")
        await cli.connect(login=True)
        await cli.switch_command(self.key, True)      #change key value to true

    async def turn_off(self):
        cli = aioesphomeapi.APIClient("sonoff1", 6053, password="MyPassword")
        await cli.connect(login=True)
        await cli.switch_command(self.key, False)    #change key value to false


class MySensor(Device):         #create new sensor device       
    def __init__(self, dev_type="mysensor.basic", addr=None):
        super().__init__(dev_type=dev_type, addr=addr)
        self.new_attribute("sensor", 0)
        self.product_id = "sensor"
        self.info = "sensor"

# a test of presence sensor, but we did not use in this TP
# class MySensorZone(Device):        
#     def __init__(self, dev_type="motion.basic", addr=None):
#         super().__init__(dev_type=dev_type, addr=addr)
#         self.new_attribute("presence", default=False)