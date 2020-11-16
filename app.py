import os

from quart import Quart, websocket

app = Quart(__name__)


@app.route('/')
async def hello():
    return '<h1>hello world, my friend</h1>'

app.debug = True




