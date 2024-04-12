'''
使用RGBA处理将将图片中白色突出显示
便于后续处理识别白线
'''
from PIL import Image


def process_image(input_image_path, output_image_path):
    # 打开图像文件
    image = Image.open(input_image_path)
    # 将图像转换为 RGBA 模式（包含透明度）
    image_rgba = image.convert("RGBA")

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
            if r > 200 and g > 200 and b > 200:
                processed_image.putpixel((x, y), (r, g, b, a))
            else:
                processed_image.putpixel((x, y), (0, 0, 0, 255))

    # 保存处理后的图像
    processed_image.save(output_image_path)


if __name__ == "__main__":
    input_path = "ColourControl\input_image.png"
    output_path = "ColourControl\output_image.png"
    process_image(input_path, output_path)
