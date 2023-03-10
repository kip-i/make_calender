import cv2
import numpy as np

img = np.full((900, 1620, 3), (52,52,52), dtype=np.uint8)
white = (255,255,255)
black = (0,0,0)
write_area = (190,190,190)
green = (0,255,0)
bg = (52,52,52)
bg_re = (203,203,203)
slash_list = [0,120,240,360,480,600,720]
#斜め箱
cv2.fillConvexPoly(img, np.array([[560,0],[920,0],[440,900],[80,900]]), write_area,lineType=cv2.LINE_AA)
cv2.fillConvexPoly(img, np.array([[1040,0],[1400,0],[920,900],[560,900]]), write_area,lineType=cv2.LINE_AA)
#斜め線
for i in slash_list:
  cv2.line(img, (1400-i, 0), (920-i, 900), bg,lineType=cv2.LINE_AA)
#横線
for i in range(13):
  cv2.line(img, (0, i*75), (1620,  i*75), bg)
  cv2.line(img, (920-i*40, i*75), (1040-i*40,  i*75), bg_re,thickness=2)
#時刻
time_list=[' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ','10','11','12',' 1 ',' 2 ',' 3 ']
for i in range(12):
  if int(time_list[i]) < 4:
    cv2.putText(img, time_list[i], (915-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2,lineType=cv2.LINE_AA)
  elif int(time_list[i]) < 10:
    cv2.putText(img, time_list[i], (915-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2,lineType=cv2.LINE_AA)
  else:
    cv2.putText(img, time_list[i], (920-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2,lineType=cv2.LINE_AA)

#10分刻み
for i in range(7):
  if not i == 3:
    for j in range(12):
      cv2.line(img, (560+i*120-j*40, 0+j*75), (640+i*120-j*40, 75+j*75), bg,lineType=cv2.LINE_AA)

cv2.imwrite('opencv_draw_font.png', img)
