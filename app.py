import json
from typing import List

from flask import Flask, g
from flask import request
import asyncio
from pyhon import Hon, HonAPI
from pyhon.appliance import HonAppliance
from pyhon.commands import HonCommand

app = Flask(__name__)

async_var_initialized = False
app.config['ASYNC_VAR'] = None


@app.before_request
def before_request():
    global async_var_initialized
    if not async_var_initialized:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        async_var = loop.run_until_complete(async_initialize())
        app.config['ASYNC_VAR'] = async_var
    g.hon = app.config['ASYNC_VAR']
    # print(g.hon)

    async_var_initialized = True


async def commands(command: HonCommand):
    await command.send()


async def async_initialize():
    hon = await Hon(
        email='zawadzkipiter@gmail.com',
        password='Klima4321',
        mobile_id='homassistant',
        session=None,
        test_data_path=None,
        refresh_token='refresh_token',
    ).create()
    return hon


@app.route('/status')
def status_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    print('status')
    print('g.hon.api.auth.refresh_token' + g.hon.api.auth.refresh_token)
    for device in g.hon.appliances:
        deviceLocal: HonAppliance = device
        extracted_values = {}
        for key, honValue in deviceLocal.attributes['parameters'].items():
            extracted_values[key] = str(honValue)
        print(extracted_values)
        return extracted_values
    return 'error'


@app.route('/devices')
def devices_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    acs = g.hon.appliances
    current = list()
    for ac in acs:
        current.append(ac.nick_name)
    return current


@app.route('/ping')
def ping_http():  # put
    return 'OK2'


@app.route('/settings')
def settings_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    acs = g.hon.appliances
    for ac in acs:
        if ac.nick_name == device:
            start_command: HonCommand = ac.commands['settings']
            for name, setting in start_command.parameters.items():
                # name = settings.windSpeed
                if request.args is not None and request.args.get(name) is not None:
                    setting.value = request.args.get(name)
            asyncio.run(commands(start_command))
    return 'CHANGED'



@app.route('/commands')
def commands_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    return str(asyncio.run(commands(username, password, device)))
    # return 'STOPPED'


if __name__ == '__main__':
    app.run(debug=True)
