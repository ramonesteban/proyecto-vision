import numpy as np
import cv2
import Image

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs(np.dot(d1, d2) / np.sqrt(np.dot(d1, d1)*np.dot(d2, d2)))

def find_squares(image_path):
    img = cv2.imread(image_path)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    onesquare = []
    squares = []
    preview = []

    for gray in cv2.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        onesquare.append((cnt[0][0], cnt[0][1]))
                        onesquare.append((cnt[1][0], cnt[1][1]))
                        onesquare.append((cnt[2][0], cnt[2][1]))
                        onesquare.append((cnt[3][0], cnt[3][1]))
                        squares.append(onesquare)
                        onesquare = []
                        preview.append(cnt)
    return squares, preview

def search(image_path):
    squares, preview = find_squares(image_path)
    image = cv2.imread(image_path)
    cv2.drawContours(image, preview, -1, (0, 255, 0), 3)
    newimage = Image.fromarray(image)
    newimage.save('preview.png')
    return squares

