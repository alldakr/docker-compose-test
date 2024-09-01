import asyncio
import websockets
import json
import time

async def send_data():
    while True:
        try:
            async with websockets.connect('ws://localhost:8000/ws/ai_server') as websocket:
                while True:
                    # 전송할 데이터를 생성합니다.
                    data = {
                        "msgID": "from ai_server",
                        "data": "hello"
                    }
                    
                    # 데이터를 JSON으로 변환하여 웹소켓으로 전송합니다.
                    await websocket.send(json.dumps(data))
                    print(f"Sent data: {data}")
                    
                    # 1초 후에 다음 데이터를 전송합니다.
                    await asyncio.sleep(1)
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed, reconnecting in 3 seconds...")
            await asyncio.sleep(3)
            continue

asyncio.get_event_loop().run_until_complete(send_data())