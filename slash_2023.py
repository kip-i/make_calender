img = np.full((900, 1620, 3), (52,52,52), dtype=np.uint8)
white = (255,255,255)
black = (0,0,0)
write_area = (190,190,190)
green = (0,255,0)
bg = (52,52,52)
bg_re = (203,203,203)
slash_list = [0,120,240,360,480,600,720]
#斜め箱
cv2.fillConvexPoly(img, np.array([[700,0],[1060,0],[580,900],[220,900]]), write_area)
cv2.fillConvexPoly(img, np.array([[1180,0],[1540,0],[1060,900],[700,900]]), write_area)
#斜め線
for i in slash_list:
  cv2.line(img, (1540-i, 0), (1060-i, 900), bg)
#横線
for i in range(13):
  cv2.line(img, (0, i*75), (1620,  i*75), bg)
  cv2.line(img, (1060-i*40, i*75), (1180-i*40,  i*75), bg_re,thickness=2)
#時刻
time_list=[' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ','10','11','12',' 1 ',' 2 ',' 3 ']
for i in range(12):
  if int(time_list[i]) < 4:
    cv2.putText(img, time_list[i], (1055-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2)
  elif int(time_list[i]) < 10:
    cv2.putText(img, time_list[i], (1050-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2)
  else:
    cv2.putText(img, time_list[i], (1060-i*40, 60+i*75), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, white, thickness=2)

#10分刻み
for i in range(7):
  if not i == 3:
    for j in range(12):
      cv2.line(img, (700+i*120-j*40, 0+j*75), (780+i*120-j*40, 75+j*75), bg)

cv2.imwrite('opencv_draw_font.png', img)
