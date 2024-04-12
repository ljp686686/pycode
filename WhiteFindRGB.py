'''
使用OpenCV的RGNA处理将将视频中白色突出显示
便于后续处理识别白线
'''
import cv2
from PIL import Image
import numpy as np

def process_image(img):
    # 将图像转换为 RGBA 模式（包含透明度）
    image_rgba = img.convert("RGBA")

    # 获取图像的宽度和高度
    width, height = image_rgba.size

    # 创建一个新的图像对象，用于存储处理后的图像
    processed_image = Image.new("RGBA", (width, height), (0, 0, 0, 255))

    # 遍历每个像素
    for x in range(width):
        for y in range(height):
            # 获取像素的 RGB 和 Alpha 值
            r, g, b, a = image_rgba.getpixel((x, y))
            # 如果像素为白色（RGB 值均大于 200），则保留，否则设为黑色
            if r > 180 and g > 180 and b > 180:
                processed_image.putpixel((x, y), (r, g, b, a))
            else:
                processed_image.putpixel((x, y), (0, 0, 0, 255))

    return processed_image


if __name__ == "__main__":
    # 摄像头捕获
    cap = cv2.VideoCapture(0)

    while True:
        # 从摄像头捕获一帧
        ret, frame = cap.read()
        if not ret:
            break

        # 将图像转换为 Pillow 的 Image 对象
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)

        # 处理图像
        processed_img = process_image(pil_img)

        # 将处理后的图像转换为 OpenCV 格式
        processed_img_cv2 = cv2.cvtColor(
            np.array(processed_img), cv2.COLOR_RGBA2BGR)

        # 显示图像
        cv2.imshow('Processed Image', processed_img_cv2)

        # 按下 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
