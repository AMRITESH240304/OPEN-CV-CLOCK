import cv2 as cv 
import datetime
import math
from constant import COLORS
from constant import RADIUS
from constant import CENTER 


def getDigitalTime(h,m,s):
	time = ""
	hour = ""
	minute = ""
	second = ""
	if(h<10):
		hour = "0{}:".format(h)
	else:
		hour = "{}:".format(h)
	if(m<10):
		minute = "0{}:".format(m)
	else:
		minute = "{}:".format(m)
	if(s<10):
		second = "0{}".format(s)
	else:
		second = "{}".format(s)
	time = hour+minute+second
	return time

def draw_time(img):
    time = datetime.datetime.now().time()
    hour = math.fmod(time.hour,24)
    min = time.minute
    sec = time.second
    
    second_angle = math.fmod(sec*6+270,360)
    minute_angle = math.fmod(min*6+270,360)
    hour_angle = math.fmod((hour*30) + (min/2)+ 270, 360)
    
    second_x = int(CENTER[0] + (RADIUS)*math.cos(second_angle*math.pi/180))
    second_y = int(CENTER[0] + (RADIUS)*math.sin(second_angle*math.pi/180))
    cv.line(img, CENTER, (second_x, second_y), COLORS['black'], 2)
    
    minute_x = int(CENTER[0] + (RADIUS-60)*math.cos(minute_angle*math.pi/180))
    minute_y = int(CENTER[0] + (RADIUS-60)*math.sin(minute_angle*math.pi/180))
    cv.line(img, CENTER, (minute_x, minute_y), COLORS['green'], 2)
    
    hour_x = int(CENTER[0] + (RADIUS-120) * math.cos(hour_angle * math.pi / 180))
    hour_y = int(CENTER[1] + (RADIUS-120) * math.sin(hour_angle * math.pi / 180))
    cv.line(img, CENTER, (hour_x, hour_y), COLORS['amber'], 2)
    
    cv.circle(img, CENTER, 5, COLORS['dark_gray'], -1)
    
    time = getDigitalTime(int(hour),min,sec)

    cv.putText(img,time, (200,390), cv.FONT_HERSHEY_DUPLEX, 1.6, COLORS['red'], 1, cv.LINE_AA)
    return img