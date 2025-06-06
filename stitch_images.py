import os
from PIL import Image
from pathlib import Path

def stitch_images(input_dir, output_file, columns=19):
    # 获取所有JPG文件并按数字顺序排序
    image_files = sorted(
        [f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')],
        key=lambda x: int(Path(x).stem)
    )

    if not image_files:
        raise ValueError("未找到JPG图片文件")

    # 打开第一张图片获取尺寸
    with Image.open(os.path.join(input_dir, image_files[0])) as img:
        width, height = img.size

    # 计算画布尺寸
    rows = (len(image_files) + columns - 1) // columns
    canvas = Image.new('RGB', (width * columns, height * rows))

    # 拼接图片
    for index, img_file in enumerate(image_files):
        with Image.open(os.path.join(input_dir, img_file)) as img:
            x = (index % columns) * width
            y = (index // columns) * height
            canvas.paste(img, (x, y))

    # 保存结果
    canvas.save(output_file)
    print(f"成功生成拼接图片：{output_file}")

if __name__ == '__main__':
    input_dir = r'C:\Users\HP\Desktop\images\5014'
    output_file = r'C:\Users\HP\Desktop\stitched_output2.jpg'
    
    try:
        stitch_images(input_dir, output_file)
    except Exception as e:
        print(f"错误发生：{str(e)}")
