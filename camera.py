from picamera import PiCamera
from time import sleep

camera = PiCamera()

# 이미지 저장
camera.start_preview()
sleep(5)
camera.capture("/home/white/gw/image/capture.jpg")
camera.stop_preview()

# 동영상 저장
camera.start_preview()
sleep(2)
camera.start_recording('/home/white/gw/image/vid.h264')
sleep(60)
camera.stop_recording()
camera.stop_preview()