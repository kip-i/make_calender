import cv2
import numpy as np

def main():
    img = np.full((900, 1620, 3), (52,52,52), dtype=np.uint8)
    white = (255,255,255)
    black = (0,0,0)
    write_area = (190,190,190)
    green = (0,255,0)
    bg = (52,52,52)
    bg_re = (203,203,203)
    #===時間表===
    slash_list = [0,120,240,360,480,600,720]
    #斜め箱
    cv2.fillConvexPoly(img, np.array([[700,0],[1060,0],[580,900],[220,900]]), write_area,lineType=cv2.LINE_AA)
    cv2.fillConvexPoly(img, np.array([[1180,0],[1540,0],[1060,900],[700,900]]), write_area,lineType=cv2.LINE_AA)
    #斜め線
    for i in slash_list:
      cv2.line(img, (1540-i, 0), (1060-i, 900), bg,lineType=cv2.LINE_AA)
    #横線
    for i in range(1,12):
      cv2.line(img, (0, i*75), (1620,  i*75), bg)
      cv2.line(img, (1060-i*40, i*75), (1180-i*40,  i*75), bg_re,thickness=2)
    #時刻
    time_list=[' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ','10','11','12',' 1 ',' 2 ',' 3 ']
    for i in range(12):
      if int(time_list[i]) < 4:
        cv2.putText(img, time_list[i], (1055-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2,lineType=cv2.LINE_AA)
      elif int(time_list[i]) < 10:
        cv2.putText(img, time_list[i], (1055-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2,lineType=cv2.LINE_AA)
      else:
        cv2.putText(img, time_list[i], (1060-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2,lineType=cv2.LINE_AA)

    #10分刻み
    for i in range(7):
      if not i == 3:
        for j in range(12):
          cv2.line(img, (700+i*120-j*40, 0+j*75), (780+i*120-j*40, 75+j*75), bg,lineType=cv2.LINE_AA)

    #===左のやつ===
    #cv2.fillConvexPoly(img, np.array([[700,0],[340,0],[0,637],[360,637]]), write_area,lineType=cv2.LINE_AA)
    cv2.fillConvexPoly(img, np.array([[679, 10],[319, 10],[13,585],[373,585]]), write_area,lineType=cv2.LINE_AA)

    #横線　上2つ
    cv2.line(img, (304, 40), (664, 40), bg,lineType=cv2.LINE_AA)
    cv2.line(img, (278, 85), (640, 85), bg,lineType=cv2.LINE_AA, thickness=3)
    #斜め線　上2つ
    cv2.line(img, (439, 10), (399, 85), bg,lineType=cv2.LINE_AA)
    cv2.line(img, (559, 10), (519, 85), bg,lineType=cv2.LINE_AA)
    #上の箱
    #cv2.fillConvexPoly(img, np.array([[560, 9],[681, 9],[664,40],[544,40]]), bg,lineType=cv2.LINE_AA)
    cv2.fillConvexPoly(img, np.array([[560, 9],[681, 9],[665,39],[544,39]]), bg,lineType=cv2.LINE_AA)
    #横線
    """for i in range(8):
      cv2.line(img, (280-i*40, 85+i*75), (640-i*40,  85+i*75), bg, lineType=cv2.LINE_AA)"""
    for i in range(10):
      cv2.line(img, (278-i*27, 86+i*50), (640-i*26,  86+i*50), bg, lineType=cv2.LINE_AA)
    #斜め線　Todo
    cv2.line(img, (334, 86), (68,  585), bg, lineType=cv2.LINE_AA)



    #例文を入れる
    cv2.putText(img, ' 2 ', (320, 75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, '22', (450, 75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, '2023', (550, 75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, 'February', (325, 32), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.7, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, 'Wednesday', (440, 32), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.7, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.imwrite('opencv_draw_font.png', img)


if __name__ == '__main__':
    main()
