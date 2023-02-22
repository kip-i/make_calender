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

    #



    cv2.imwrite('calender.png', img)

if __name__ == '__main__':
    main()
