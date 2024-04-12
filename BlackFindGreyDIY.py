'''
使用灰度处理将视频中的黑色突出显示
便于后续处理识别黑色台阶
其中RGB自定义权重红色排除影响
'''

import cv2


def keep_black(image, r_weight=0, g_weight=0.7, b_weight=0.3):
    # 将图像转换为灰度图
    gray = r_weight * image[:, :, 2] + g_weight * \
        image[:, :, 1] + b_weight * image[:, :, 0]

    # 将灰度图转换为二值图像，阈值设为 50
    _, binary = cv2.threshold(gray.astype('uint8'), 50, 255, cv2.THRESH_BINARY)

    # 创建一个掩码，黑色部分（像素值为 0）保留为黑色，其他部分设为白色
    mask = cv2.merge([binary, binary, binary])

    result = mask

    return result


if __name__ == "__main__":
    # 摄像头捕获
    cap = cv2.VideoCapture(0)

    while True:
        # 从摄像头捕获一帧
        ret, frame = cap.read()
        if not ret:
            break

        # 处理图像，默认权重为红色最低，绿色次之，蓝色最高
        processed_img = keep_black(frame)

        # 显示图像
        cv2.imshow('Processed Image', processed_img)

        # 按下 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
