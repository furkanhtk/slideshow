import numpy as np
import cv2
import time
from datetime import datetime
import glob
from random import randint

data=[" "," "," "," "]
stime = int(str(time.gmtime().tm_min))
cexit=0
imagesname = []
for img in glob.glob("images/*.jpg"):
    n= cv2.imread(img)
    imagesname.append(img)

size=len(imagesname)
rnumber=randint(0,size-1)


def caltime():
    now = datetime.now()
    second=(datetime(2019,9,17,8)-now).total_seconds()
    minute=second//60
    hour=minute//60
    day=(hour//24)

    leftday=str(round(day))
    lefthour=str(round((hour-(24*day))))
    leftminute=str(round((minute-(60*hour))))
    leftsecond=str(round((second-(60*minute))))
    data = [leftday, lefthour, leftminute, leftsecond ]

    return data

data=caltime()

font = cv2.FONT_HERSHEY_TRIPLEX #font for displaying text (below)
img = cv2.imread(imagesname[rnumber])
dimensions = img.shape
scale_percent = 70 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


while(True):

    ctime = int(str(time.gmtime().tm_min))
    x=ctime-stime
    while (x%2)==0:
            img = cv2.imread(imagesname[rnumber])
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            cv2.putText(resized, data[0] + " days " + data[1] + " hour " + data[2] + " minute " + data[3] + "  second ", (150, 500), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.namedWindow("Slide Show", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Slide Show", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Slide Show',resized)
            data=caltime()
            ctime = int(str(time.gmtime().tm_min))
            x = ctime - stime
            cv2.waitKey(1)
            #cv2.destroyAllWindows()
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cexit=1
                break
    if cexit==1:
        break
    rnumber = randint(0, size - 1)
    print(rnumber)
    while (x % 2) != 0:
            img = cv2.imread(imagesname[rnumber])
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            cv2.putText(resized, data[0] + " days " + data[1] + " hour " + data[2] + " minute " + data[3] + "  second ", (150, 500), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.namedWindow("Slide Show", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Slide Show", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Slide Show', resized)
            data = caltime()
            ctime = int(str(time.gmtime().tm_min))
            x = ctime - stime
            cv2.waitKey(1)
            #v2.destroyAllWindows()
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cexit=1
                break
    if cexit==1:
        break






    if cv2.waitKey(1) & 0xFF == ord('a'):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()

