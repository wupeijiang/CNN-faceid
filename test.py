# import sys
#
# import pyttsx3
# engine = pyttsx3.init()
# engine.say('hello world')
# engine.say('明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间！'
#
#     +'转朱阁，低绮户，照无眠。不应有恨，何事偏向别时圆？人有悲欢离合，月有阴晴圆缺，此事古难全。但愿人长久，千里共婵娟。')
# engine.runAndWait()
# # 朗读一次
# engine.endLoop()


import cv2 as cv
import dlib

cam=cv.VideoCapture(0)
haar = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img2 = cv.imread('logo.png')   #logo图像，要往原始图像上添加
while 1:
    cat,img=cam.read()
    gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray_img, 1.3, 5)
    for f_x, f_y, f_w, f_h in faces:
        face = img[f_y:f_y + f_h, f_x:f_x + f_w]
        img = cv.rectangle(img, (f_x, f_y), (f_x + f_w, f_y + f_h), (255, 0, 0), 2)
    cv.imshow("capture", img)
    key = cv.waitKey(30) & 0xff
    if key == 27:
        break