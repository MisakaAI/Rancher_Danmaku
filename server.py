#!/usr/bin/env python3

import asyncio
import ssl
import websockets

connected = set()

async def counter(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            print(message)
            if connected:
                for user in connected:
                    await user.send(message)
    except websockets.ConnectionClosed as e:
        pass
    finally:
        connected.remove(websocket)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('/etc/letsencrypt/live/live.mineraltown.net/fullchain.pem', '/etc/letsencrypt/live/live.mineraltown.net/privkey.pem')
start_server = websockets.serve(counter, "0.0.0.0", 5678, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
