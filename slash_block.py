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
        cv2.fillConvexPoly(img, np.array([[700-i*x_slide,0+i*75],[1500-i*x_slide,0+i*75],[1500-i*x_slide,74+i*75],[700-i*x_slide,74+i*75]]), write_area)
        #時刻箱
        cv2.fillConvexPoly(img, np.array([[1060-i*x_slide, 0+i*75],[1140-i*x_slide, 0+i*75],[1140-i*x_slide, 74+i*75],[1060-i*x_slide, 74+i*75]]), bg)
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
            cv2.line(img, (700+j*60-i*x_slide,i*75+1),(700+j*60-i*x_slide,20+i*75-1), bg_re,thickness=2)
            cv2.line(img, (1140+j*60-i*x_slide,i*75+1),(1140+j*60-i*x_slide,20+i*75-1), bg_re,thickness=2)
        if not i == 0:
            #仕切り線
            cv2.line(img, (700-i*x_slide, i*75), (1500-i*x_slide,  i*75), bg)
            #時刻箱の仕切り線
            cv2.line(img, (1060-i*x_slide, i*75), (1177-i*x_slide,  i*75), bg_re)
        
        #上下区切り線
        cv2.line(img, (700-i*x_slide, 20+i*75), (1500-i*x_slide,  20+i*75), bg)

    #日付表
    day_box = [206,586,40,140] #lx,rx,uy,dy
    cv2.fillConvexPoly(img, np.array([[day_box[0],day_box[2]],[day_box[1],day_box[2]],[day_box[1],day_box[3]],[day_box[0],day_box[3]]]), write_area)
    day_line1 = [day_box[0],day_box[1],80] #xs,xf,y
    cv2.line(img, (day_line1[0], day_line1[2]), (day_line1[1],  day_line1[2]), bg)
    day_line2 = [336,day_box[2],day_box[3]] #x,ys,yf
    cv2.line(img, (day_line2[0], day_line2[1]), (day_line2[0],  day_line2[2]), bg)
    day_line3 = [466,day_box[2],day_box[3]]
    cv2.line(img, (day_line3[0], day_line3[1]), (day_line3[0],  day_line3[2]), bg)
    cv2.fillConvexPoly(img, np.array([[466,39],[587,39],[587,80],[466,80]]), bg)

    x_slide_day = 74
    for i in range(3):
        #Todo枠3個ずつ
        cv2.fillConvexPoly(img, np.array([[206-i*x_slide_day,150+i*150],[586-i*x_slide_day,150+i*150],[586-i*x_slide_day,198+i*150],[206-i*x_slide_day,198+i*150]]), write_area)
        cv2.fillConvexPoly(img, np.array([[181-i*x_slide_day,200+i*150],[561-i*x_slide_day,200+i*150],[561-i*x_slide_day,248+i*150],[181-i*x_slide_day,248+i*150]]), write_area)
        cv2.fillConvexPoly(img, np.array([[156-i*x_slide_day,250+i*150],[536-i*x_slide_day,250+i*150],[536-i*x_slide_day,298+i*150],[156-i*x_slide_day,298+i*150]]), write_area)
        #Todo縦線3個ずつ
        cv2.line(img,(256-i*x_slide_day,150+i*150),(256-i*x_slide_day,198+i*150),bg)
        cv2.line(img,(231-i*x_slide_day,200+i*150),(231-i*x_slide_day,248+i*150),bg)
        cv2.line(img,(206-i*x_slide_day,250+i*150),(206-i*x_slide_day,298+i*150),bg)

    #含有時間
    time_box = [1214,1574,722,822] #lx,rx,uy,dy
    #day_box = [1168,1528,676,820]
    cv2.fillConvexPoly(img, np.array([[time_box[0],time_box[2]],[time_box[1],time_box[2]],[time_box[1],time_box[3]],[time_box[0],time_box[3]]]), write_area)
    time_line1 = [time_box[0],time_box[1],762] #xs,xf,y
    cv2.line(img, (time_line1[0], time_line1[2]), (time_line1[1],  time_line1[2]),bg)
    time_line2 = [1334,time_box[2],time_box[3]] #x,ys,yf
    cv2.line(img, (time_line2[0], time_line2[1]), (time_line2[0],  time_line2[2]), bg)
    time_line3 = [1454,time_box[2],time_box[3]]
    cv2.line(img, (time_line3[0], time_line3[1]), (time_line3[0],  time_line3[2]), bg)

    cv2.putText(img, 'game', (1239, 752), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, 'sleep', (1359, 752), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, '2', (1469, 752), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, '4', (1483, 752), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, 'sleep', (1500, 752), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)

    #例文を入れる
    cv2.putText(img, ' 2', (246, 130), cv2.FONT_HERSHEY_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, '22', (381, 130), cv2.FONT_HERSHEY_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, '2023', (486, 130), cv2.FONT_HERSHEY_COMPLEX, 1, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, 'February', (216, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, bg, thickness=1,lineType=cv2.LINE_AA)
    cv2.putText(img, 'Wednesday', (346, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, bg, thickness=1,lineType=cv2.LINE_AA)


    cv2.imwrite('calender.png', img)

if __name__ == '__main__':
    main()
