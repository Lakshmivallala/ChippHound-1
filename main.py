import cv2
import numpy as np
import adv
import telepot
from telepot.loop import MessageLoop
import time
from datetime import datetime
import os
import requests;

bot = telepot.Bot("955635606:AAFeVFAP6P4ZPGDkDsWaGmQn-62PvOVkRHI")
MessageLoop(bot, adv.handle).run_as_thread()
# Pretrained classes in the model
classNames = {0: 'background',
              1: 'person'}
print('1')

canCall = True
counter = 0
# emoji
police = u'\U0001F4A8'

bUrl = 'https://cutapi.chipphound.wtf'

def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value

def adjust_gamma(image, gamma=1.0):

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)
print('2')
cap= cv2.VideoCapture(0)
#cap=cv2.VideoCapture('rtsp://192.168.43.170:8005')
address = f'rtsp://192.168.43.170:8005/h264_pcm.sdp'
# cap = cv2.VideoCapture(address)

print('3')
# Loading model
model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                      'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
print('4')
send_status = 1
i = 0

br = 0
while True:
        
        ret, image = cap.read()
        if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        if ret == False:
                break
        
        if br == 1:
                break
        image_height, image_width, _ = image.shape

        model.setInput(cv2.dnn.blobFromImage(image, size=(200, 200), swapRB=True))
        output = model.forward()


        for detection in output[0, 0, :, :]:
                confidence = detection[2]
                if confidence > 0.5:
                        class_id = detection[1]
                        if class_id == 1.0:
                                class_name=id_class_name(class_id,classNames)
                                box_x = detection[3] * image_width
                                box_y = detection[4] * image_height
                                box_width = detection[5] * image_width
                                box_height = detection[6] * image_height
                                cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
                                i += 1
                                if(send_status == 1):
                                        cv2.imwrite("img/cap_"+str(int(i/50))+".jpg", image)
                                        bot.sendPhoto(-356660400, photo=open("img/cap_"+str(int(i/50))+".jpg", 'rb'), caption=police+"*Intruder detected*" + police + "\n`Human detected`.", parse_mode='MARKDOWN')
                                        # send_status = 0
                                        test = str(datetime.now())
                                        #filePath = "static/images/cap_"+test+".jpg"
                                        filePath = "static/images/1.jpg"
                                        cv2.imwrite(filePath, image)
                                        print(datetime.now())
                                        print(filePath)
                                        img = {'file': filePath}
                                        #x = requests.get(bUrl+'/email')
                                        if(canCall):
                                            x = requests.get(bUrl+'/call')
                                            # x = requests.get(bUrl+'/email')
                                        canCall = False
                                        #time.sleep(10)
                                        #x = requests.post(bUrl, data=myObj)
                                        # br = 1
        # cv2.imshow('image', image)


cap.release()
cv2.destroyAllWindows()
#time.sleep(10)
#os.system('python3 web.py')
