import io
import os
import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import Response
from pyhon import Hon
from pyhon.appliance import HonAppliance
from pyhon.commands import HonCommand

app = FastAPI()

g = {}


async def async_initialize():
    hon = await Hon(
        email=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        mobile_id=os.getenv("MOBILE_ID", 'loxone'),
        session=None,
        test_data_path=None,
        refresh_token='refresh_token',
    ).create()
    return hon


async def run(command, device, args):
    acs = g["hon"].appliances
    for ac in acs:
        if ac.nick_name == device:
            start_command: HonCommand = ac.commands[command]
            for name, setting in start_command.parameters.items():
                # name = settings.windSpeed
                print(args)
                if args is not None and args.get(name) is not None:
                    print(args.get(name))
                    setting.value = args.get(name)
            await ac.commands[command].send()


@app.on_event("startup")
async def startup_event():
    g["hon"] = await async_initialize()
    print("done")


@app.get("/status")
def get_image(device: str):
    extracted_values = {}
    for acc in g["hon"].appliances:
        if acc.nick_name == device:
            deviceLocal: HonAppliance = acc
            for key, honValue in deviceLocal.attributes['parameters'].items():
                extracted_values[key] = str(honValue)
            print(extracted_values)
    return {"result": extracted_values}


@app.get("/settings")
async def settings(device: str, request: Request):
    await run('settings', device, request.query_params)
    return {"result": 'done'}


@app.get('/devices')
def devices_http():  # put
    acs = g["hon"].appliances
    current = list()
    for ac in acs:
        current.append(ac.nick_name)
    return current

