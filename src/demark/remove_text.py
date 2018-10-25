# coding=utf-8
# remove text watermark
import sys
import cv2
import numpy as np


def main(path_from, path_to):
    img = cv2.imread(path_from)
    hight, width, depth = img.shape[0:3]

    # 图片二值化处理，把[220, 220, 220]~[255, 255, 255]以外的颜色变成0
    thresh = cv2.inRange(img, np.array([220, 220, 220]), np.array([255, 255, 255]))

    # 只处理右2/5, 下1/10区域
    for i in range(hight):
        for j in range(width):
            if j < (width * 3 / 5):
                thresh[i][j] = 0
            else:
                if i < hight * 9 / 10:
                    thresh[i][j] = 0

    # 创建形状和尺寸的结构元素
    kernel = np.ones((3, 3), np.uint8)

    # 扩张待修复区域
    hi_mask = cv2.dilate(thresh, kernel, iterations=10)
    specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)
    cv2.imwrite(path_to, specular)

    # test
    # cv2.namedWindow("Image", 0)
    # cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
    # cv2.imshow("Image", img)
    #
    # cv2.namedWindow("newImage", 0)
    # cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
    # cv2.imshow("newImage", specular)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python remove_text.py /data/1.jpg /data/1_result.jpg')
    else:
        path_from = sys.argv[1]
        path_to = sys.argv[2]
        main(path_from, path_to)