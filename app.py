from flask import Flask
from flask import request
import asyncio
from pyhon import Hon, HonAPI
from pyhon.appliance import HonAppliance
from pyhon.commands import HonCommand

app = Flask(__name__)


@app.route('/status')
def status_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    return str(asyncio.run(status(username, password, device)))


@app.route('/devices')
def devices_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    return str(asyncio.run(devices(username, password)))


@app.route('/ping')
def ping_http():  # put
    return 'OK2'


@app.route('/start')
def start_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    start_action(username, password, device, request.args)
    return 'STARTED'


@app.route('/settings')
def settings_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    str(asyncio.run(settings_action(username, password, device)))
    return 'CHANGED'


@app.route('/stop')
def stop_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    stop_action(username, password, device)
    return 'STOPPED'


@app.route('/commands')
def commands_http():  # put
    username = request.args.get('username')
    password = request.args.get('password')
    device = request.args.get('device')
    return str(asyncio.run(commands(username, password, device)))
    # return 'STOPPED'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)


def start_action(username, password, device, args):
    asyncio.run(run('startProgram', username, password, device, args))


def settings_action(username, password, device):
    asyncio.run(run('settings', username, password, device))


def stop_action(username, password, device):
    asyncio.run(run('stopProgram', username, password, device, None))


async def commands(username, password, device):
    print('status')
    async with HonAPI(username, password) as api:
        appl = await api.load_appliances()
        for appliance in appl:
            if appliance['nickName'] == device:
                att2 = await api.load_commands(HonAppliance(api, appliance))
                return att2['settings']['setParameters']['parameters']


async def status(username, password, device):
    print('status')
    async with HonAPI(username, password) as api:
        appl = await api.load_appliances()
        for appliance in appl:
            if appliance['nickName'] == device:
                att2 = await api.load_attributes(HonAppliance(api, appliance))
                return att2['shadow']['parameters']


async def devices(username, password):
    async with Hon(username, password) as hon:
        acs = hon.appliances
        current = list()
        for ac in acs:
            current.append(ac.nick_name)
        return current


async def run(command, username, password, device, args):
    async with Hon(username, password) as hon:
        acs = hon.appliances
        for ac in acs:
            if ac.nick_name == device:
                start_command: HonCommand = ac.commands[command]
                for name, setting in start_command.parameters.items():
                    # name = settings.windSpeed
                    if args is not None and args.get(name) is not None:
                        setting.value = args.get(name)
                await start_command.send()
