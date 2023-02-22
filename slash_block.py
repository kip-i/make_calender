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

    #ずらす値　40で前ページと一致
    x_slide = 37
    #時間表
    for i in range(12):
        #書く箱
        cv2.fillConvexPoly(img, np.array([[700-i*x_slide,0+i*75],[1500-i*x_slide,0+i*75],[1500-i*x_slide,75+i*75],[700-i*x_slide,75+i*75]]), write_area,lineType=cv2.LINE_AA)
        #時刻箱
        cv2.fillConvexPoly(img, np.array([[1060-i*x_slide, 0+i*75],[1140-i*x_slide, 0+i*75],[1140-i*x_slide, 75+i*75],[1060-i*x_slide, 75+i*75]]), bg,lineType=cv2.LINE_AA)
        #時刻
        time_list=[' 4',' 5',' 6',' 7',' 8',' 9','10','11','12',' 1',' 2',' 3']
        if int(time_list[i]) < 10:
            cv2.putText(img, time_list[i], (1062-i*x_slide, 60+i*75), cv2.FONT_HERSHEY_COMPLEX, 1.5, white,lineType=cv2.LINE_AA)
        elif int(time_list[i]) == 11:
            cv2.putText(img, time_list[i], (1070-i*x_slide, 60+i*75), cv2.FONT_HERSHEY_COMPLEX, 1.5, white,lineType=cv2.LINE_AA)
        else:
            cv2.putText(img, time_list[i], (1067-i*x_slide, 60+i*75), cv2.FONT_HERSHEY_COMPLEX, 1.5, white,lineType=cv2.LINE_AA)
        #分刻み線
        for j in range(1,6):
            cv2.line(img, (700+j*60-i*x_slide,i*75),(700+j*60-i*x_slide,20+i*75), bg_re,thickness=2)
            cv2.line(img, (1140+j*60-i*x_slide,i*75),(1140+j*60-i*x_slide,20+i*75), bg_re,thickness=2)
        if not i == 0:
            #仕切り線
            cv2.line(img, (700-i*x_slide, i*75), (1500-i*x_slide,  i*75), bg)
            #時刻箱の仕切り線
            cv2.line(img, (1060-i*x_slide, i*75), (1180-i*x_slide,  i*75), bg_re,thickness=2)
        
        #上下区切り線
        cv2.line(img, (700-i*x_slide, 20+i*75), (1500-i*x_slide,  20+i*75), bg)


    cv2.imwrite('calender.png', img)

if __name__ == '__main__':
    main()
