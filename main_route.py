import asyncio
import json
from picamera import PiCamera
import numpy as np
import websockets

# async def connect():

#     # 웹 소켓에 접속을 합니다.
#     async with websockets.connect("ws://210.102.178.119:12125/ws") as websocket:

#         str = input('Python 웹소켓으로 전송할 내용을 입력하세요[종료하려면 quit 입력!]: ')     # 사용자의 입력을 변수에 저장
#         #print(str)  # 변수의 내용을 출력

#         while str != 'quit':

#             # quit가 들어오기 전까지 계속 입력받은 문자열을 전송하고 에코를 수신한다.
#             await websocket.send(str)

#             # 웹 소켓 서버로 부터 메시지가 오면 콘솔에 출력합니다.
#             data = await websocket.recv()
#             print(data)

#             str = input('Python 웹소켓으로 전송할 내용을 입력하세요[종료하려면 quit 입력!]: ')  # 사용자의 입력을 변수에 저장
#             # print(str)  # 변수의 내용을 출력


# # 비동기로 서버에 접속한다.
# asyncio.get_event_loop().run_until_complete(connect())

import asyncio
import websockets
import io
import picamera
from Freenove_Robot_Dog_Kit_for_Raspberry_Pi.Code.Server.Action import Action


# async def stream_to_websocket(url):
#     async with websockets.connect(url) as websocket:
#         with picamera.PiCamera(resolution='640x480', framerate=30) as camera:
#             stream = io.BytesIO()
#             for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
#                 stream.seek(0)
#                 frame = stream.read()
#                 await websocket.send(frame)
#                 await asyncio.sleep(0.001)
#                 stream.seek(0)
#                 stream.truncate()
            
action = Action()
async def receive_commands(websocket):
    async for message in websocket:
        # 여기서 서버로부터의 메시지를 처리합니다.
        # 예: print(message) 또는 명령에 따른 조치 수행
        print(f"행동 : {message}")
        await asyncio.sleep(1)
        if message == "0":
            action.push_ups()
        elif message == "1":
            action.helloOne()
        elif message == "2":
            action.hand()
        elif message == "3":
            action.yoga()
        elif message == "4": 
            action.swim()
        # elif message == "5": 
        #     action.coquettish()
        # elif message == "6":
        #     action.helloTwo()
        # elif message == "7":
        #     action.happy()
        # elif message == "8":
        #     action.happy_actions()
        # elif message == "9":
        #     action.wave()
        else:
            print("no action")
        print("행동 끝")

async def stream_to_websocket(url):
    async with websockets.connect(url) as websocket:
        with picamera.PiCamera(resolution='640x480', framerate=30) as camera:
            # 이미지 캡처 및 전송 작업
            capture_task = asyncio.create_task(capture_and_send_frames(camera, websocket))
            
            # 서버 명령 수신 작업
            command_task = asyncio.create_task(receive_commands(websocket))

            # 두 작업을 동시에 실행
            await asyncio.gather(capture_task, command_task)

async def capture_and_send_frames(camera, websocket):
    stream = io.BytesIO()
    for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
        stream.seek(0)
        frame = stream.read()
        await websocket.send(frame)
        await asyncio.sleep(0.001)
        stream.seek(0)
        stream.truncate()


url1 = "ws://210.102.178.119:12125/ws1"
# url2 = "ws://210.102.178.119:12125/ws2"
# async def main():
#     # 두 웹소켓 연결을 동시에 실행
#     await asyncio.gather(
#         stream_to_websocket(url1),
#         stream_to_websocket(url2)
#     )
asyncio.get_event_loop().run_until_complete(stream_to_websocket(url1))
# 이벤트 루프를 사용하여 main 함수 실행
# asyncio.get_event_loop().run_until_complete(main())