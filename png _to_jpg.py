import os
from PIL import Image

# 定义输入和输出目录
input_dir = r'D:\NanJing\cityspace\leftImg8bit\train'  # Cityscapes 图像路径
output_dir = r'D:\GitHub\yuyifenge\PSPNet\VOCdevkit\VOCdevkit\VOC2007\JPEGImages/'  # VOC格式的输出路径

# 如果输出目录不存在，创建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入文件夹的所有子文件夹
for city in os.listdir(input_dir):
    city_dir = os.path.join(input_dir, city)

    if os.path.isdir(city_dir):  # 确保是子文件夹
        for filename in os.listdir(city_dir):
            if filename.endswith('.png'):  # 确认是 PNG 文件
                # 构造原始图片路径
                img_path = os.path.join(city_dir, filename)

                # 打开 PNG 图像
                img = Image.open(img_path).convert('RGB')  # 转换为 RGB 以确保没有 alpha 通道

                # 生成新的 JPG 文件名，将原有子文件夹名加入文件名避免重名
                ##
                #注意这里有误，后缀不应该有数据集名称
                jpg_filename = city + '_' + filename.replace('.png', '.jpg')
                output_path = os.path.join(output_dir, jpg_filename)

                # 保存为 JPG 格式
                img.save(output_path, 'JPEG')
                print(f"保存 {output_path}")