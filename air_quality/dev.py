#!/usr/bin/env python3
# -*-coding: utf-8-*-


from xaal.lib import Device, Engine, tools
import requests
import datetime

# create and configure the air measure quality device, with a random address
dev = Device("air.basic", tools.get_random_uuid())
dev.product_id = 'brest air'
dev.url = 'http://www.acme.org'
dev.info = 'My fake lamp'

# add an xAAL attribute 'code_quality'
code_quality = dev.new_attribute('code_quality')


def update_data():
    date = "{}-{}-{}".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    url = "https://data.airbreizh.asso.fr/geoserver/ind_bretagne/ows?service=WFS&version=1.0.0&request=GetFeature" \
          "&typeName=ind_bretagne:ind_bretagne&outputFormat=application%2Fjson&CQL_FILTER=date_ech%20%3E%20%27{" \
          "}%27%20and%20code_zone=%27242900314%27".format(date)                   #public data url, to achieve today's climate data   
    r = requests.get(url)
    result = r.json()
    code_quality.value = result["features"][0]["properties"]["lib_qual"]


# last step, create an engine and register the air quality monitor
update_data()
eng = Engine()
eng.add_timer(func=update_data, period=3600)
eng.add_device(dev)
eng.run()
