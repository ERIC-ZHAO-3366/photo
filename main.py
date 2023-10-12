import cv2
import numpy as np

def image_verification(image_path):
    # 读取图片
    image = cv2.imread(image_path)

    # 将图片转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用Canny边缘检测
    edges = cv2.Canny(gray_image, 100, 200)

    # 计算图片中的轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 设置阈值，过滤掉噪声
    threshold = 50
    _, filtered_contours = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

    # 遍历轮廓，检查是否存在异常区域
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示处理后的图片
    cv2.imshow('Verified Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_path = 'path/to/your/image.jpg'
    image_verification(image_path)
